"""Qualitative and quantitative analysis of sparse models."""

from __future__ import annotations

from collections.abc import Iterable

from stormpy import developer, storage
from stormpy.core._common import _formula, _value_type_of_model
from stormpy.developer import CheckResult, CheckTask, Environment, PcaaWeightVectorChecker, Property
from stormpy.exceptions import StormError


def topological_sort(model, forward: bool = True, initial: Iterable[int] | None = None) -> list[int]:
    """
    Sort the states of a sparse model topologically.

    :param model: Sparse model.
    :param forward: If True, the states are sorted along the transitions. Otherwise, the states are sorted along the backward transitions.
    :param initial: (optional) States from which the sorting starts.
    :return: List of states in topological order.
    """
    if not model.is_sparse_model:
        raise StormError("Topological sorting is only supported for sparse models.")
    matrix = model.transition_matrix if forward else model.backward_transition_matrix
    return storage._storage._topological_sort(matrix, list(initial) if initial is not None else [])


def compute_expected_number_of_visits(model, environment: Environment | None = None) -> CheckResult:
    """
    Compute the expected number of visits of each state, starting from the initial states.

    :param model: Sparse deterministic model (DTMC or CTMC). Parametric models are not supported.
    :param environment: (optional) Environment configuring the solvers.
    :return: Quantitative result containing the expected number of visits for each state.
    """
    if model.supports_parameters:
        raise StormError("The expected number of visits is not supported for parametric models.")
    return developer.compute_expected_visiting_times_with_sparse_engine(environment if environment is not None else Environment(), model)


def compute_steady_state_distribution(model, environment: Environment | None = None) -> CheckResult:
    """
    Compute the steady-state (aka stationary) distribution.

    :param model: Sparse deterministic model (DTMC or CTMC). Parametric models are not supported.
    :param environment: (optional) Environment configuring the solvers.
    :return: Quantitative result containing the steady-state probability for each state.
    """
    if model.supports_parameters:
        raise StormError("The steady-state distribution is not supported for parametric models.")
    return developer.compute_steady_state_distribution_with_sparse_engine(environment if environment is not None else Environment(), model)


def create_weight_vector_checker(
    model, property: Property, *, produce_scheduler: bool = False, environment: Environment | None = None
) -> tuple[PcaaWeightVectorChecker, storage.SparseModelMemoryProductReverseData | None]:
    """
    Create a checker for weighted sums of the objectives of a multi-objective property.

    The checker optimizes the weighted sum for a given weight vector via ``checker.check(env, weights)``.

    :param model: Sparse MDP (with float or Rational values).
    :param property: Multi-objective property (or formula).
    :param produce_scheduler: If True, the checker can compute optimal schedulers.
    :param environment: (optional) Environment configuring the preprocessing.
    :return: Tuple of the checker and the data mapping schedulers of the checker back to the original model (None if not required).
    """
    if model.supports_parameters or model.supports_uncertainty:
        raise StormError("Parametric and interval models are not supported.")
    return developer.create_weight_vector_checker(environment if environment is not None else Environment(), model, _formula(property), produce_scheduler)
