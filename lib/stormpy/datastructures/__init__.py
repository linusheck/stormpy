"""Matrices, labels, schedulers, valuations and memory structures.

``SparseMatrixBuilder[ValueType]`` builds a matrix by adding entries in row and
column order, then calling ``build()``. The value type defaults to ``float``.
``build_sparse_matrix[ValueType](array)`` constructs the same representation
from a NumPy array. Row groups associate several action rows with one state.

``BitVector`` supports indexed Boolean access; iteration yields the indices of
set bits. State and choice labelings associate named labels with such indices.
``Scheduler`` and ``SchedulerChoice`` describe the decisions resolved during
model checking, while memory structures describe finite scheduler memory.

Valuations are constructed using ``ValuationDescriptionBuilder`` to declare
variables and their storage encoding, then ``Valuations(description, manager,
num_entities)``. ``get_value``, ``write_value`` and ``get_values_states`` dispatch
by variable type; double-encoded rationals and large integers have explicit
accessors. ``ValuationTransformer`` evaluates expressions to derive new variables.

The raw Storm bindings are available in :mod:`stormpy.developer.storage`."""

from stormpy.developer import storage as _bindings

BitVector = _bindings.BitVector
SparseMatrixEntry = _bindings.SparseMatrixEntry.publish_as("stormpy.datastructures.SparseMatrixEntry")
SparseMatrixBuilder = _bindings.SparseMatrixBuilder.publish_as("stormpy.datastructures.SparseMatrixBuilder")
SparseMatrix = _bindings.SparseMatrix.publish_as("stormpy.datastructures.SparseMatrix")
SparseMatrixRows = _bindings.SparseMatrixRows.publish_as("stormpy.datastructures.SparseMatrixRows")
StateLabeling = _bindings.StateLabeling
ChoiceLabeling = _bindings.ChoiceLabeling
Scheduler = _bindings.Scheduler.publish_as("stormpy.datastructures.Scheduler")
SchedulerChoice = _bindings.SchedulerChoice.publish_as("stormpy.datastructures.SchedulerChoice")
Distribution = _bindings.Distribution.publish_as("stormpy.datastructures.Distribution")
Valuations = _bindings.Valuations
ValuationClassDescription = _bindings.ValuationClassDescription
ValuationDescriptionBuilder = _bindings.ValuationDescriptionBuilder
ValuationTransformer = _bindings.ValuationTransformer
SimpleValuation = _bindings.SimpleValuation
MemoryStructure = _bindings.MemoryStructure
MemoryStructureBuilder = _bindings.MemoryStructureBuilder.publish_as("stormpy.datastructures.MemoryStructureBuilder")
ChoiceOrigins = _bindings.ChoiceOrigins
JaniChoiceOrigins = _bindings.JaniChoiceOrigins
PrismChoiceOrigins = _bindings.PrismChoiceOrigins
MaximalEndComponent = _bindings.MaximalEndComponent
MaximalEndComponentDecomposition = _bindings.MaximalEndComponentDecomposition.publish_as("stormpy.datastructures.MaximalEndComponentDecomposition")

__all__ = [
    "BitVector",
    "SparseMatrixEntry",
    "SparseMatrixBuilder",
    "SparseMatrix",
    "SparseMatrixRows",
    "StateLabeling",
    "ChoiceLabeling",
    "Scheduler",
    "SchedulerChoice",
    "Distribution",
    "Valuations",
    "ValuationClassDescription",
    "ValuationDescriptionBuilder",
    "ValuationTransformer",
    "SimpleValuation",
    "MemoryStructure",
    "MemoryStructureBuilder",
    "ChoiceOrigins",
    "JaniChoiceOrigins",
    "PrismChoiceOrigins",
    "MaximalEndComponent",
    "MaximalEndComponentDecomposition",
]

from . import _convenience, _valuations
from ._matrix import build_sparse_matrix


def get_maximal_end_components(model):
    """Compute the maximal end components of a nondeterministic sparse model.

    :param model: Sparse MDP, POMDP, Markov automaton or stochastic game.
    :return: An iterable decomposition into maximal end components.
    """
    return MaximalEndComponentDecomposition(model)


__all__ += ["build_sparse_matrix", "get_maximal_end_components"]
