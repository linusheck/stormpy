"""Construction of sparse matrices from NumPy arrays."""

from operator import index as _index

from stormpy import Rational, RationalFunction, RationalFunctionCoefficient, Polynomial, Interval, RationalInterval
from stormpy.developer.storage import SparseMatrixBuilder
from stormpy._template import _deduce_default, _template_function


@_template_function(
    "stormpy.datastructures.build_sparse_matrix",
    parameters=("ValueType",),
    instantiations=(float, Rational, RationalFunction, Interval, RationalInterval),
    deduce=_deduce_default(float),
)
def build_sparse_matrix(value_type: type, array, row_group_indices=None):
    """Build a sparse matrix from a two-dimensional NumPy array.

    Zero entries are skipped. The value type is selected by subscription, e.g.
    ``build_sparse_matrix[stormpy.Rational](array)``. It defaults to ``float``.
    Explicit row groups include empty rows and groups.

    :param array: Two-dimensional array containing matrix values.
    :param row_group_indices: Optional ascending starting row indices of row groups.
    :return: Sparse matrix with the shape of the input array.
    :raises ValueError: If the array shape or row group indices are invalid.
    """
    if array.ndim != 2:
        raise ValueError("Expected a two-dimensional array")
    rows, columns = array.shape
    try:
        groups = [] if row_group_indices is None else [_index(index) for index in row_group_indices]
    except TypeError:
        raise ValueError("Row group indices must be integers") from None
    if any(index < 0 or index >= rows for index in groups):
        raise ValueError("Row group indices must be integers within the matrix rows")
    if any(left >= right for left, right in zip(groups, groups[1:])):
        raise ValueError("Row group indices must be strictly increasing")
    nz_rows, nz_columns = array.nonzero()
    builder = SparseMatrixBuilder[value_type](rows=rows, columns=columns, entries=len(nz_rows), has_custom_row_grouping=bool(groups), row_groups=len(groups))
    # Insert empty groups as well as groups containing non-zero entries.
    group_index = 0
    entry_index = 0
    for row in range(rows):
        if group_index < len(groups) and groups[group_index] == row:
            builder.new_row_group(row)
            group_index += 1
        while entry_index < len(nz_rows) and nz_rows[entry_index] == row:
            column = int(nz_columns[entry_index])
            value = array[row, column]
            if hasattr(value, "item"):
                value = value.item()
            if not isinstance(value, value_type):
                if value_type is RationalFunction:
                    value = RationalFunction(Polynomial(RationalFunctionCoefficient(value)))
                elif value_type is RationalInterval:
                    value = RationalInterval(Rational(value))
                else:
                    value = value_type(value)
            builder.add_next_value(row, column, value)
            entry_index += 1
    return builder.build()
