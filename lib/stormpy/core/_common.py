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
