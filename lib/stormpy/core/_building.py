"""Building of models from symbolic descriptions and explicit input formats."""

from __future__ import annotations

from collections.abc import Iterable

from stormpy import developer, storage
from stormpy.core._common import _convert_sparse_model, _convert_symbolic_model, _formulas, _value_type_prefix
from stormpy._config import Interval, Rational, RationalFunction, RationalInterval
from stormpy.developer import (
    BuilderOptions,
    DirectEncodingParserOptions,
    Environment,
    ExplicitModelParserOptions,
    Property,
    SymbolicModelDescription,
)
from stormpy.exceptions import StormError


def _check_constants(model) -> None:
    """Raise an error if the symbolic model has undefined constants which would change the graph structure."""
    if isinstance(model, SymbolicModelDescription):
        model = model.as_prism_program() if model.is_prism_program() else model.as_jani_model()
    if not model.undefined_constants_are_graph_preserving:
        raise StormError("Model still contains undefined constants which influence the graph structure. Use instantiate_constants() first.")


def build_model(
    model: storage.PrismProgram | storage.JaniModel | SymbolicModelDescription,
    properties: Iterable[Property] | None = None,
    *,
    value_type: type = float,
    options: BuilderOptions | None = None,
):
    """
    Build a model in sparse (explicit) representation from a symbolic model.

    :param model: Symbolic model (Prism program, Jani model or symbolic model description).
    :param properties: (optional) Properties which should be checkable on the built model.
        Only the labels and reward models required by the properties are built.
        If None or empty (and no options are given), all labels and reward models are built.
    :param value_type: Value type of the model: float (default), Rational (exact), RationalFunction (parametric),
        Interval or RationalInterval (exact interval).
    :param options: (optional) Builder options for full control of the building process. Cannot be combined with properties.
    :return: The model in sparse representation, e.g. a sparse DTMC.
    """
    build = getattr(developer, f"build_sparse_{_value_type_prefix(value_type)}model")
    if value_type is not RationalFunction:
        _check_constants(model)
    if options is not None:
        if properties:
            raise StormError("Either properties or builder options can be given, but not both.")
        return _convert_sparse_model(build(model, options))
    if properties:
        # Storm derives the builder options from the formulas and the model (e.g., choice labels for POMDPs)
        return _convert_sparse_model(build(model, _formulas(properties)))
    return _convert_sparse_model(build(model, BuilderOptions(build_all_reward_models=True, build_all_labels=True)))


def build_symbolic_model(
    model: storage.PrismProgram | storage.JaniModel | SymbolicModelDescription,
    properties: Iterable[Property] | None = None,
    *,
    value_type: type = float,
    environment: Environment | None = None,
):
    """
    Build a model in symbolic representation (using decision diagrams) from a symbolic model.

    :param model: Symbolic model (Prism program, Jani model or symbolic model description).
    :param properties: (optional) Properties which should be checkable on the built model. If None, the full model is built.
    :param value_type: Value type of the model: float (default), Rational (exact) or RationalFunction (parametric).
    :param environment: (optional) Environment configuring the decision diagram libraries.
    :return: The model in symbolic representation, e.g. a symbolic DTMC.
    """
    if value_type in (Interval, RationalInterval):
        raise StormError("Symbolic models do not support interval value types.")
    build = getattr(developer, f"build_symbolic_{_value_type_prefix(value_type)}model")
    if value_type is not RationalFunction:
        _check_constants(model)
    formulas = _formulas(properties)
    environment = environment if environment is not None else Environment()
    return _convert_symbolic_model(build(environment, model, formulas, build_full_model=not formulas))


def build_model_from_drn(path: str, options: DirectEncodingParserOptions | None = None, *, value_type: type = float):
    """
    Build a model in sparse representation from a file in the explicit DRN format.

    :param path: Path to the DRN file.
    :param options: (optional) Options for the DRN parser.
    :param value_type: Value type of the model: float (default), Rational (exact), RationalFunction (parametric),
        Interval or RationalInterval (exact interval).
    :return: The model in sparse representation.
    """
    build = getattr(developer, f"build_explicit_{_value_type_prefix(value_type)}drn_model")
    return _convert_sparse_model(build(path, options if options is not None else DirectEncodingParserOptions()))


def build_model_from_explicit(
    transitions: str,
    labeling: str,
    *,
    state_rewards: str | None = None,
    transition_rewards: str | None = None,
    choice_labeling: str | None = None,
    options: ExplicitModelParserOptions | None = None,
):
    """
    Build a model in sparse representation from files in the explicit format (.tra, .lab, ...).

    :param transitions: Path to the file containing the transitions (.tra).
    :param labeling: Path to the file containing the state labeling (.lab).
    :param state_rewards: (optional) Path to the file containing state rewards.
    :param transition_rewards: (optional) Path to the file containing transition rewards.
    :param choice_labeling: (optional) Path to the file containing the choice labeling.
    :param options: (optional) Options for the explicit parser.
    :return: The model in sparse representation.
    """
    model = developer.build_explicit_model(
        transitions,
        labeling,
        state_rewards,
        transition_rewards,
        choice_labeling,
        options if options is not None else ExplicitModelParserOptions(),
    )
    return _convert_sparse_model(model)


def build_model_from_umb(path: str, options: storage.UmbImportOptions | None = None):
    """
    Build a model in sparse representation from a UMB archive.

    :param path: Path to the UMB archive.
    :param options: (optional) Options controlling the value type and which parts of the model are built.
    :return: The model in sparse representation.
    """
    options = options if options is not None else storage.UmbImportOptions()
    umb = storage.import_umb(path, options)
    return _convert_sparse_model(storage.sparse_model_from_umb(umb, options))
