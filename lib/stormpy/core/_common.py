"""Internal helpers shared by the modules of the public API."""

from __future__ import annotations

from collections.abc import Iterable

from stormpy import storage
from stormpy._config import Rational, RationalFunction
from stormpy.developer import Property
from stormpy.exceptions import StormError


def _value_type_of_model(model) -> type:
    """Get the value type of a sparse or symbolic model."""
    if model.is_sparse_model:
        return storage.parameters_of_model(model)[0]
    if model.supports_parameters:
        return RationalFunction
    if model.is_exact:
        return Rational
    return float


def _formula(property: Property | object):
    """Get the raw formula of the given property (formulas are passed through)."""
    return property.get_raw_formula() if isinstance(property, Property) else property


def _formulas(properties: Iterable[Property | object] | None) -> list:
    """Get the raw formulas of the given properties (formulas are passed through)."""
    if properties is None:
        return []
    return [_formula(prop) for prop in properties]


_SPARSE_SUFFIXES = {
    storage.ModelType.DTMC: "dtmc",
    storage.ModelType.MDP: "mdp",
    storage.ModelType.POMDP: "pomdp",
    storage.ModelType.CTMC: "ctmc",
    storage.ModelType.MA: "ma",
    storage.ModelType.SMG: "smg",
}

_SPARSE_PREFIXES = {
    float: "",
    Rational: "exact_",
    RationalFunction: "p",
    Interval: "i",
    RationalInterval: "exact_i",
}


def _convert_sparse_model(model):
    """Convert a generic sparse model into the concrete model class (e.g. a sparse DTMC over doubles)."""
    if model.supports_parameters:
        value_type = RationalFunction
    elif model.supports_uncertainty:
        value_type = RationalInterval if model.is_exact else Interval
    else:
        value_type = Rational if model.is_exact else float
    try:
        suffix = _SPARSE_SUFFIXES[model.model_type]
    except KeyError:
        raise StormError(f"Unsupported model type {model.model_type}") from None
    return getattr(model, f"_as_sparse_{_SPARSE_PREFIXES[value_type]}{suffix}")()


_SYMBOLIC_SUFFIXES = {
    storage.ModelType.DTMC: "dtmc",
    storage.ModelType.MDP: "mdp",
    storage.ModelType.CTMC: "ctmc",
    storage.ModelType.MA: "ma",
}


def _convert_symbolic_model(model):
    """Convert a generic symbolic model into the concrete model class (e.g. a symbolic DTMC over doubles)."""
    try:
        suffix = _SYMBOLIC_SUFFIXES[model.model_type]
    except KeyError:
        raise StormError(f"Unsupported model type {model.model_type}") from None
    return getattr(model, f"_as_symbolic_{_SPARSE_PREFIXES[_value_type_of_model(model)]}{suffix}")()
