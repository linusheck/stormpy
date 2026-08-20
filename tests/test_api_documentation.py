import importlib
import inspect
import re
from pathlib import Path

import pytest


API_REFERENCES = {
    "core.rst": ("stormpy",),
    "info.rst": ("stormpy.info",),
    "exceptions.rst": ("stormpy.exceptions",),
    "logic.rst": ("stormpy.logic",),
    "storage.rst": ("stormpy.storage",),
    "utility.rst": ("stormpy.utility",),
    "dft.rst": ("stormpy.dft",),
    "gspn.rst": ("stormpy.gspn",),
    "pars.rst": ("stormpy.pars",),
    "pomdp.rst": ("stormpy.pomdp",),
    "pycarl/core.rst": ("stormpy.pycarl", "stormpy.pycarl.gmp", "stormpy.pycarl.cln"),
    "pycarl/convert.rst": ("stormpy.pycarl.convert",),
    "pycarl/formula.rst": ("stormpy.pycarl.formula", "stormpy.pycarl.gmp.formula", "stormpy.pycarl.cln.formula"),
    "pycarl/parse.rst": ("stormpy.pycarl.parse", "stormpy.pycarl.gmp.parse", "stormpy.pycarl.cln.parse"),
}


def _api_root():
    return Path(__file__).parents[1] / "doc" / "source" / "api"


def test_all_api_reference_files_are_checked():
    api_root = _api_root()
    if not api_root.exists():
        pytest.skip("source documentation is not part of the wheel test bundle")
    reference_files = {
        str(path.relative_to(api_root))
        for path in api_root.rglob("*.rst")
        if "generated" not in path.parts
    }
    assert reference_files == set(API_REFERENCES), (
        f"API reference test manifest is out of sync. "
        f"Missing: {sorted(reference_files - set(API_REFERENCES))}; "
        f"stale: {sorted(set(API_REFERENCES) - reference_files)}"
    )


def _public_types(module_name):
    module = importlib.import_module(module_name)
    result = set()
    for name, value in vars(module).items():
        if name.startswith("_") or not inspect.isclass(value):
            continue
        owner = value.__module__
        if module_name == "stormpy":
            # The top-level package re-exports types documented by its submodules.
            # Only types implemented directly in stormpy or stormpy._core belong
            # to the core reference.
            if owner == module_name or owner.startswith("stormpy._"):
                result.add(name)
        elif owner == module_name or owner.startswith(module_name + "."):
            result.add(name)
    return result


@pytest.mark.parametrize(("reference_name", "module_names"), API_REFERENCES.items())
def test_all_public_types_are_in_api_reference(reference_name, module_names):
    """Keep curated API indices in sync with the types exported by their modules."""
    reference = _api_root() / reference_name
    if not reference.exists():
        pytest.skip("source documentation is not part of the wheel test bundle")
    reference_text = reference.read_text()

    for module_name in module_names:
        documented_types = set(
            re.findall(rf"^\s+{re.escape(module_name)}\.([A-Za-z]\w*)\s*$", reference_text, flags=re.MULTILINE)
        )

        # An automodule directive discovers members dynamically. Once a module
        # is converted to a curated autosummary, require an exhaustive list.
        if not documented_types and re.search(rf"^\.\. automodule::\s+{re.escape(module_name)}\s*$", reference_text, flags=re.MULTILINE):
            continue

        try:
            public_types = _public_types(module_name)
        except ImportError as error:
            pytest.skip(f"optional module {module_name} is unavailable: {error}")
        missing_types = public_types - documented_types
        stale_types = documented_types - public_types
        assert not missing_types and not stale_types, (
            f"API reference for {module_name} is out of sync. "
            f"Missing: {sorted(missing_types)}; stale: {sorted(stale_types)}"
        )
