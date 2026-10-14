"""Python conveniences on the public classes; native methods retain Storm's names.

Public and developer classes share their native type, so these conveniences also
work on objects returned by the native engines.
"""

from stormpy.developer import storage
from stormpy._template import _TemplateClass

_ALIASES = {
    "ExpressionManager": {
        "create_rational": "rational",
        "create_boolean": "boolean",
        "create_integer": "integer",
        "create_boolean_variable": "declare_boolean_variable",
        "create_integer_variable": "declare_integer_variable",
        "create_rational_variable": "declare_rational_variable",
        "create_string_variable": "declare_string_variable",
    },
    "Variable": {"has_bitvector_type": "has_bit_vector_type"},
    "Expression": {"identifier": "get_identifier"},
    "ExpressionParser": {"parse": "parse_from_string"},
}

for _name, _aliases in _ALIASES.items():
    _family = getattr(storage, _name)
    _classes = _family.instantiations.values() if isinstance(_family, _TemplateClass) else (_family,)
    for _class in _classes:
        for _alias, _method in _aliases.items():
            setattr(_class, _alias, getattr(_class, _method))


# Static constructors are public conveniences over native operators and functions.
for _name, _method in {
    "Plus": "__add__",
    "Minus": "__sub__",
    "Multiply": "__mul__",
    "Divide": "__truediv__",
    "And": "__and__",
    "Or": "__or__",
    "Geq": "__ge__",
    "Eq": "__eq__",
    "Neq": "__ne__",
    "Greater": "__gt__",
    "Less": "__lt__",
    "Leq": "__le__",
}.items():
    setattr(storage.Expression, _name, staticmethod(getattr(storage.Expression, _method)))

for _name in ("modulo", "implies", "iff", "conjunction", "disjunction"):
    setattr(storage.Expression, _name.capitalize(), staticmethod(getattr(storage, _name)))
