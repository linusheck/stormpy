"""Python conveniences on the public classes; native methods retain Storm's names.

Public and developer classes share their native type, so these conveniences also
work on objects returned by the native engines.
"""

from stormpy.developer import storage
from stormpy._template import _TemplateClass

_ALIASES = {
    "BitVector": {
        "number_of_set_bits": "get_number_of_set_bits",
        "as_int": "get_as_int",
        "number_of_set_bits_before_index": "get_number_of_set_bits_before_index",
    },
    "SparseMatrixEntry": {"value": "get_value"},
    "Valuations": {"get_string": "to_string", "get_nr_of_entities": "get_number_of_entities"},
    "StateLabeling": {"has_state_label": "get_state_has_label"},
    "SchedulerChoice": {"get_choice": "get_choice_as_distribution"},
}

for _name, _aliases in _ALIASES.items():
    _family = getattr(storage, _name)
    _classes = _family.instantiations.values() if isinstance(_family, _TemplateClass) else (_family,)
    for _class in _classes:
        for _alias, _method in _aliases.items():
            setattr(_class, _alias, getattr(_class, _method))


def _submatrix(self, row_constraint, column_constraint, insert_diagonal_entries=False, use_groups=True):
    """Select a submatrix.

    :param row_constraint: Selected rows or row groups.
    :param column_constraint: Selected columns.
    :param insert_diagonal_entries: Whether to retain a diagonal entry in each row.
    :param use_groups: Whether row_constraint selects row groups.
    :return: The selected sparse matrix.
    """
    return self.get_submatrix(use_groups, row_constraint, column_constraint, insert_diagonal_entries)


for _class in storage.SparseMatrix.instantiations.values():
    _class.submatrix = _submatrix


def _to_value_type(self, value_type=float):
    """Convert a scheduler's choice probabilities to another value type.

    :param value_type: Target numeric type, such as float or stormpy.Rational.
    :return: A new scheduler using the requested numeric type.
    :raises TypeError: If conversion between the selected types is unsupported.
    """
    return storage.to_value_type[value_type](self)


for _class in storage.Scheduler.instantiations.values():
    _class.to_value_type = _to_value_type


def _conversion(value_type):
    def convert(self):
        return _to_value_type(self, value_type)

    convert.__doc__ = "Return a copy of the scheduler with converted choice probabilities."
    return convert


# Existing public convenience spellings are implemented in Python.
from stormpy import Rational as _Rational, RationalFunction as _RationalFunction, Interval as _Interval, RationalInterval as _RationalInterval

for _name, _value_type in (
    ("cast_to_double_datatype", float),
    ("cast_to_exact_datatype", _Rational),
    ("cast_to_parametric_datatype", _RationalFunction),
    ("cast_to_interval_datatype", _Interval),
    ("cast_to_exact_interval_datatype", _RationalInterval),
):
    for _parameters, _class in storage.Scheduler.instantiations.items():
        if _parameters[0] not in (_Interval, _RationalInterval) and not (_parameters[0] is _RationalFunction and _value_type in (_Interval, _RationalInterval)):
            setattr(_class, _name, _conversion(_value_type))
