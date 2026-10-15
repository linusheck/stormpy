"""Helpers for selecting public and developer autosummary members."""

import importlib
import sys

# For developer modules that re-export members of other modules: the members that should
# be listed on the module's autosummary page, identified by their __module__.
# All other module pages list all their members.
_MEMBER_MODULES = {
    # The number-independent core types live in the compiled _pycarl_core module.
    "stormpy.numbers.developer": {"stormpy.numbers.developer", "stormpy.numbers.developer._pycarl_core"},
    # The number-dependent formula types are bound under the shared formula module.
    "stormpy.numbers.developer.gmp.formula": {"stormpy.numbers.developer.formula"},
    "stormpy.numbers.developer.cln.formula": {"stormpy.numbers.developer.formula"},
    # Utility modules re-export pycarl helpers.
    "stormpy.numbers.developer.convert": {"stormpy.numbers.developer.convert"},
    "stormpy.numbers.developer.parse": {"stormpy.numbers.developer.parse"},
}

# Raw bindings shared with a public module are documented on the public page.
_PUBLIC_MODULES = {
    "stormpy.developer": ("stormpy", "stormpy.logic", "stormpy.utility"),
    "stormpy.developer.info": ("stormpy.info",),
    "stormpy.developer.logic": ("stormpy.logic",),
    "stormpy.developer.storage": ("stormpy.models", "stormpy.datastructures", "stormpy.expressions", "stormpy.io"),
    "stormpy.developer.utility": ("stormpy.utility",),
    "stormpy.dft.developer": ("stormpy.dft",),
    "stormpy.numbers.developer": ("stormpy.numbers",),
}


def _filter_api_members(module, members):
    """
    Filter the members listed on the autosummary page of a module.

    Public modules declare their API in __all__, including objects whose
    implementations live in private core modules or developer bindings.
    """
    members = [name for name in members if not name.startswith("_")]
    module_obj = sys.modules[module]
    if hasattr(module_obj, "__all__"):
        return [name for name in members if name in module_obj.__all__]
    for public_name in _PUBLIC_MODULES.get(module, ()):
        public_module = importlib.import_module(public_name)
        members = [
            name
            for name in members
            if getattr(public_module, name, None) is not getattr(module_obj, name, None)
            and not (
                hasattr(getattr(module_obj, name, None), "publish_as")
                and getattr(getattr(public_module, name, None), "canonical_name", None) == f"{public_name}.{name}"
            )
        ]
    accepted = _MEMBER_MODULES.get(module)
    if accepted is None:
        return members
    return [name for name in members if getattr(getattr(module_obj, name, None), "__module__", None) in accepted]
