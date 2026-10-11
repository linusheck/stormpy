"""Transformations of models, e.g. bisimulation minimization or the construction of submodels."""

from __future__ import annotations

from collections.abc import Iterable

from stormpy import developer, storage
from stormpy.core._common import _formulas, _value_type_of_model
from stormpy._config import Interval, Rational, RationalInterval
from stormpy.developer import (
    AddUncertainty,
    BisimulationOptions,
    BisimulationType,
    DdBisimulationOptions,
    EliminationLabelBehavior,
    EndComponentEliminator,
    EndComponentEliminatorReturnType,
    Property,
    QuotientFormat,
    SubsystemBuilderOptions,
    SubsystemBuilderReturnType,
)
from stormpy.exceptions import StormError


def perform_bisimulation(
    model,
    properties: Iterable[Property],
    *,
    bisimulation_type: BisimulationType = BisimulationType.STRONG,
    options: BisimulationOptions | None = None,
    quotient_format: QuotientFormat = QuotientFormat.DD,
):
    """
    Minimize a model via bisimulation while preserving the given properties.

    :param model: The model (sparse or symbolic).
    :param properties: Properties which are preserved by the minimization.
    :param bisimulation_type: Type of bisimulation (strong or weak).
    :param options: (optional) Further options for the bisimulation of sparse models.
        If given, its bisimulation type takes precedence over the bisimulation_type argument.
    :param quotient_format: Format of the quotient for symbolic models (DD for a symbolic quotient, SPARSE for a sparse quotient).
    :return: The minimized model.
    """
    formulas = _formulas(properties)
    if model.is_sparse_model:
        if options is None:
            options = BisimulationOptions()
            options.bisimulation_type = bisimulation_type
        return developer.perform_bisimulation_minimization(model, formulas, options)
    if options is not None:
        raise StormError("Bisimulation options are only supported for sparse models.")
    quotient = developer.perform_bisimulation_minimization(
        model, formulas, bisimulation_type=bisimulation_type, quotient_format=quotient_format, bisimulation_options=DdBisimulationOptions()
    )
    return quotient


def transform_to_sparse_model(model, properties: Iterable[Property] | None = None):
    """
    Transform a model in symbolic representation into a model in sparse representation.

    :param model: Symbolic model.
    :param properties: (optional) Properties which should be preserved. If None, all labels and reward models are preserved.
    :return: The model in sparse representation.
    """
    return developer.transform_symbolic_to_sparse_model(model, _formulas(properties))


def transform_to_discrete_time_model(model, properties: Iterable[Property]) -> tuple:
    """
    Transform a continuous-time model (CTMC or MA) into a discrete-time model (DTMC or MDP).

    :param model: Sparse continuous-time model.
    :param properties: Properties which are transformed accordingly.
    :return: Tuple of the discrete-time model and the transformed formulas.
    """
    discrete_model, formulas = developer.transform_continuous_to_discrete_time_sparse_model(model, _formulas(properties))
    return discrete_model, formulas


def eliminate_non_markovian_chains(ma, properties: Iterable[Property], label_behavior: EliminationLabelBehavior) -> tuple:
    """
    Eliminate chains of non-Markovian states in a Markov automaton if possible.

    :param ma: Sparse Markov automaton.
    :param properties: Properties which are transformed accordingly.
    :param label_behavior: How labels of eliminated states are handled.
    :return: Tuple of the resulting model (an MA or a CTMC) and the transformed formulas.
    """
    model, formulas = developer.eliminate_non_markovian_chains(ma, _formulas(properties), label_behavior)
    return model, formulas


def build_submodel(
    model,
    states: storage.BitVector,
    actions: storage.BitVector,
    *,
    keep_unreachable_states: bool = True,
    options: SubsystemBuilderOptions | None = None,
) -> SubsystemBuilderReturnType:
    """
    Build the submodel restricted to the given states and actions.

    :param model: Sparse model.
    :param states: States which are kept.
    :param actions: Actions (choices) which are kept.
    :param keep_unreachable_states: If False, states which become unreachable are removed as well.
    :param options: (optional) Options for building the submodel.
    :return: Result containing the submodel (attribute ``model``) and the mappings to the original model.
    """
    return developer.build_subsystem(
        model, states, actions, keep_unreachable_states=keep_unreachable_states, options=options if options is not None else SubsystemBuilderOptions()
    )


def eliminate_end_components(
    matrix: storage.SparseMatrix,
    subsystem: storage.BitVector,
    possible_ec_rows: storage.BitVector,
    add_sink_row_states: storage.BitVector,
    add_self_loop_at_sink_states: bool = False,
) -> EndComponentEliminatorReturnType:
    """
    Eliminate the end components of a matrix.

    Each maximal end component in the subsystem is replaced by a new state.
    All incoming and outgoing transitions of the end component are redirected to (and from) this state.

    :param matrix: Transition matrix.
    :param subsystem: States which are kept (one entry per state).
        Transitions leading to a state outside the subsystem are removed (but the corresponding row is kept, possibly yielding empty rows).
    :param possible_ec_rows: Rows which can be part of an end component (one entry per row).
        Rows containing a transition leaving the subsystem are never considered.
    :param add_sink_row_states: States for which a row is added to the new state, representing the choice to stay in the end component forever (one entry per state).
    :param add_self_loop_at_sink_states: If True, the added rows contain a self-loop. Otherwise, they remain empty.
    :return: Result containing the new matrix (attribute ``matrix``) and the mappings to the original matrix.
    """
    if matrix.nr_columns != subsystem.size():
        raise StormError("The subsystem must have an entry for every state.")
    if matrix.nr_rows != possible_ec_rows.size():
        raise StormError("The possible end component rows must have an entry for every row.")
    if matrix.nr_columns != add_sink_row_states.size():
        raise StormError("The sink row states must have an entry for every state.")
    eliminator = EndComponentEliminator[storage.SparseMatrix.parameters_of(matrix)]
    return eliminator.transform(matrix, subsystem, possible_ec_rows, add_sink_row_states, add_self_loop_at_sink_states)


def add_uncertainty(model, additive_uncertainty: float | Rational, minimal_value: float | Rational | None = None, max_successors: int | None = None):
    """
    Transform a model into an interval model by adding uncertainty to all transition probabilities.

    Each probability p becomes the interval [max(minimal_value, p - additive_uncertainty), min(1, p + additive_uncertainty)].

    :param model: Sparse model with float or Rational values.
    :param additive_uncertainty: Uncertainty added to each probability.
    :param minimal_value: (optional) Lower bound of each interval. Defaults to 0.0001.
    :param max_successors: (optional) Only states with at most this many successors are made uncertain.
    :return: The interval model (with Interval or RationalInterval values).
    """
    value_type = _value_type_of_model(model)
    if value_type not in (float, Rational):
        raise StormError("Uncertainty can only be added to models with float or Rational values.")
    transformer = AddUncertainty[value_type](model)
    if minimal_value is None:
        minimal_value = 0.0001 if value_type is float else Rational("1/10000")
    return transformer.transform(additive_uncertainty, minimal_value, max_successors)


def set_state_valuations(model, valuations: storage.Valuations):
    """
    Create a copy of the model with the given state valuations.

    :param model: Sparse DTMC or MDP.
    :param valuations: The new state valuations.
    :return: Copy of the model with the new state valuations.
    """
    if model.model_type not in [storage.ModelType.DTMC, storage.ModelType.MDP]:
        raise StormError(f"Only DTMCs and MDPs are supported, got {model.model_type}.")
    components = storage.SparseModelComponents(
        transition_matrix=model.transition_matrix, state_labeling=model.labeling, reward_models=model.reward_models, rate_transitions=False
    )
    components.state_valuations = valuations
    if model.has_choice_labeling():
        components.choice_labeling = model.choice_labeling
    if model.has_choice_origins():
        components.choice_origins = model.choice_origins
    return type(model)(components)
