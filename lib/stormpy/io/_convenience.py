"""Python conveniences on the public classes; native methods retain Storm's names.

Public and developer classes share their native type, so these conveniences also
work on objects returned by the native engines.
"""

from stormpy.developer import storage
from stormpy._template import _TemplateClass

_ALIASES = {
    "JaniModel": {"define_constants": "define_undefined_constants", "make_standard_compliant": "make_standard_jani_compliant"},
    "PrismProgram": {
        "get_variables": "get_all_expression_variables",
        "define_constants": "define_undefined_constants",
        "substitute_nonstandard_predicates": "substitute_non_standard_predicates",
        "flatten": "flatten_modules",
    },
}

for _name, _aliases in _ALIASES.items():
    _family = getattr(storage, _name)
    _classes = _family.instantiations.values() if isinstance(_family, _TemplateClass) else (_family,)
    for _class in _classes:
        for _alias, _method in _aliases.items():
            setattr(_class, _alias, getattr(_class, _method))
