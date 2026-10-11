"""Building of models from symbolic descriptions and explicit input formats."""

from __future__ import annotations

from collections.abc import Iterable

from stormpy import developer, storage
from stormpy.core._common import _formulas
from stormpy._config import Interval, Rational, RationalFunction, RationalInterval
from stormpy._template import _deduce_default, _template_function
from stormpy.developer import (
    DirectEncodingParserOptions,
    Environment,
    ExplicitModelParserOptions,
    Property,
    SymbolicModelDescription,
)
from stormpy.exceptions import StormError


class BuilderOptions(developer.BuilderOptions):
    """
    Options for building a model from a symbolic description.

    The options can be created preserving the given properties via e.g. ``BuilderOptions(properties)``,
    or they can be created without properties via e.g. ``BuilderOptions(build_all_reward_models=True, build_all_labels=True)``.
    """

    def __init__(self, *args, **kwargs) -> None:
        if args and not isinstance(args[0], bool):
            # Properties (or formulas) to preserve, optionally followed by the model description
            args = (_formulas(args[0]), *args[1:])
        elif "formulas" in kwargs:
            kwargs["formulas"] = _formulas(kwargs["formulas"])
        super().__init__(*args, **kwargs)


def _check_constants(model) -> None:
    """Raise an error if the symbolic model has undefined constants which would change the graph structure."""
    if isinstance(model, SymbolicModelDescription):
        model = model.as_prism_program() if model.is_prism_program() else model.as_jani_model()
    if not model.undefined_constants_are_graph_preserving:
        raise StormError("Model still contains undefined constants which influence the graph structure. Use instantiate_constants() first.")


_VALUE_TYPES = (float, Rational, RationalFunction, Interval, RationalInterval)


@_template_function("stormpy.build_model", parameters=("ValueType",), instantiations=_VALUE_TYPES, deduce=_deduce_default(float))
def build_model(
    value_type: type,
    model: storage.PrismProgram | storage.JaniModel | SymbolicModelDescription,
    properties: Iterable[Property] | None = None,
    *,
    options: BuilderOptions | None = None,
):
    """
    Build a model in sparse (explicit) representation from a symbolic model.

    The value type of the model is selected via subscript, e.g. ``build_model[stormpy.Rational](program)``:
    float (default), Rational (exact), RationalFunction (parametric), Interval or RationalInterval (exact interval).

    :param model: Symbolic model (Prism program, Jani model or symbolic model description).
    :param properties: (optional) Properties which should be checkable on the built model.
        Only the labels and reward models required by the properties are built.
        If None or empty (and no options are given), all labels and reward models are built.
    :param options: (optional) Builder options for full control of the building process. Cannot be combined with properties.
    :return: The model in sparse representation, e.g. a sparse DTMC.
    :raises TypeError: If the value type is not supported.
    """
    build = developer.build_sparse_model[value_type]
    if value_type is not RationalFunction:
        _check_constants(model)
    if options is not None:
        if properties:
            raise StormError("Either properties or builder options can be given, but not both.")
        return build(model, options)
    if properties:
        # Storm derives the builder options from the formulas and the model (e.g., choice labels for POMDPs)
        return build(model, _formulas(properties))
    return build(model, BuilderOptions(build_all_reward_models=True, build_all_labels=True))


@_template_function(
    "stormpy.build_symbolic_model", parameters=("ValueType",), instantiations=(float, Rational, RationalFunction), deduce=_deduce_default(float)
)
def build_symbolic_model(
    value_type: type,
    model: storage.PrismProgram | storage.JaniModel | SymbolicModelDescription,
    properties: Iterable[Property] | None = None,
    *,
    environment: Environment | None = None,
):
    """
    Build a model in symbolic representation (using decision diagrams) from a symbolic model.

    The value type of the model is selected via subscript, e.g. ``build_symbolic_model[stormpy.Rational](program)``:
    float (default), Rational (exact) or RationalFunction (parametric). Interval value types are not supported.

    :param model: Symbolic model (Prism program, Jani model or symbolic model description).
    :param properties: (optional) Properties which should be checkable on the built model. If None, the full model is built.
    :param environment: (optional) Environment configuring the decision diagram libraries.
    :return: The model in symbolic representation, e.g. a symbolic DTMC.
    :raises TypeError: If the value type is not supported.
    """
    build = developer.build_symbolic_model[value_type]
    if value_type is not RationalFunction:
        _check_constants(model)
    formulas = _formulas(properties)
    environment = environment if environment is not None else Environment()
    return build(environment, model, formulas, build_full_model=not formulas)


@_template_function("stormpy.build_model_from_drn", parameters=("ValueType",), instantiations=_VALUE_TYPES, deduce=_deduce_default(float))
def build_model_from_drn(value_type: type, path: str, *, options: DirectEncodingParserOptions | None = None):
    """
    Build a model in sparse representation from a file in the explicit DRN format.

    The value type of the model is selected via subscript, e.g. ``build_model_from_drn[stormpy.Rational](path)``:
    float (default), Rational (exact), RationalFunction (parametric), Interval or RationalInterval (exact interval).

    :param path: Path to the DRN file.
    :param options: (optional) Options for the DRN parser.
    :return: The model in sparse representation.
    :raises TypeError: If the value type is not supported.
    """
    build = developer.build_explicit_drn_model[value_type]
    return build(path, options if options is not None else DirectEncodingParserOptions())


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
    return model


def build_model_from_umb(path: str, *, options: storage.UmbImportOptions | None = None):
    """
    Build a model in sparse representation from a UMB archive.

    :param path: Path to the UMB archive.
    :param options: (optional) Options controlling the value type and which parts of the model are built.
    :return: The model in sparse representation.
    """
    options = options if options is not None else storage.UmbImportOptions()
    umb = storage.import_umb(path, options)
    return storage.sparse_model_from_umb(umb, options)
