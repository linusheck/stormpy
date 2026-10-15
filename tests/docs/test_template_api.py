"""Sphinx template renderer tests; can run without importing Sphinx itself."""

import importlib.util
import re
import runpy
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest
import stormpy
import stormpy.dft
from stormpy._template import _TemplateClass, _TemplateFunction, _template_function, _deduce_default

_spec = importlib.util.spec_from_file_location("stormpy_templates", Path(__file__).parents[2] / "doc/source/_ext/stormpy_templates.py")
docs = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(docs)


def make_family():
    class Floating:
        def shared(self):
            pass

        def floating_only(self):
            """Only implemented for float."""

    class Integral:
        def shared(self):
            pass

    Floating.shared.__doc__ = "shared(self: test._Floating, value: float, tolerance: float) -> float\n\nShared method."
    Integral.shared.__doc__ = "shared(self: test._Integral, value: int, tolerance: float) -> int\n\nShared method."
    Floating.__module__ = "test"
    Floating.__name__ = "_Floating"
    Integral.__module__ = "test"
    Integral.__name__ = "_Integral"
    module = SimpleNamespace(_template_instantiations={"Example": {(float,): Floating, (int,): Integral}})
    return _TemplateClass("test.Example", module, parameters=["ValueType"])


def test_shared_and_fixed_types_and_conditional_members():
    family = make_family()
    output = docs.render_members(family, [family])
    assert "test.Example[ValueType]" in output
    assert "tolerance: float" in output
    assert "value: ValueType" in output
    assert "-> ValueType" in output
    assert "Available only for: ``Example[float]``." in output


def test_published_template_names_take_precedence():
    family = make_family()
    developer = family.publish_as("test.developer.Example")
    public = family.publish_as("test.models.Example")
    for families in ([public, developer], [developer, public]):
        output = docs.render_members(public, families)
        assert "test.models.Example[ValueType]" in output
        assert "test.developer.Example" not in output


def test_template_functions_are_listed_separately(monkeypatch):
    @_template_function("test.scale", parameters=["ValueType"], instantiations=(float, int), deduce=_deduce_default(float))
    def scale(value_type, value: int) -> int:
        """Scale a value."""
        return value

    monkeypatch.setitem(sys.modules, "test", SimpleNamespace(Example=make_family(), scale=scale, alias=scale))
    assert isinstance(scale, _TemplateFunction)
    assert docs.template_families("test") == ["Example"]
    assert docs.template_functions("test") == ["scale"]
    info = docs.template_function_info("test.scale")
    assert info["parameters"] == "ValueType"
    assert info["instantiations"] == ["scale[float]", "scale[int]"]
    assert info["signatures"] == ("(value: int) -> int",)
    assert info["overloads"] == [{"signature": "(value: int) -> int", "description": "Scale a value.", "specializations": []}]
    assert "scale[float]" in info["deduction"]


def make_native_function(monkeypatch, *, conditional=False):
    def floating():
        pass

    def integral():
        pass

    for implementation, typename, index in ((floating, "float", 1), (integral, "int", 2)):
        implementation.__name__ = f"_compute_{typename}"
        implementation.__doc__ = (
            f"_compute_{typename}(*args, **kwargs)\nOverloaded function.\n\n"
            f"1. _compute_{typename}(value: {typename}, tolerance: float, options: test._Options = <test._Options object at 0x{index:x}>) -> {typename}\n\n"
            "Compute a value.\n\n:param value: The input.\n:return: The result.\n\n"
        )
        if not conditional or implementation is floating:
            implementation.__doc__ += (
                f"2. _compute_{typename}(label: str = 'a,b') -> storm::Opaque<{typename}>\n\n" "Compute from a label; see :func:`compute`."
            )
    family = _TemplateFunction(
        "test.compute", SimpleNamespace(_template_instantiations={"compute": {(float,): floating, (int,): integral}}), parameters=["ValueType"]
    )
    monkeypatch.setitem(sys.modules, "test", SimpleNamespace(compute=family))
    return family


def test_native_function_signatures_and_prose_are_separate(monkeypatch):
    make_native_function(monkeypatch)
    info = docs.template_function_info("test.compute")
    assert info["signatures"] == ("(value: ValueType, tolerance: float, options = ...) -> ValueType", "(label: str = 'a,b')")
    assert info["overloads"] == [
        {"signature": info["signatures"][0], "description": "Compute a value.\n\n:param value: The input.\n:return: The result.", "specializations": []},
        {"signature": info["signatures"][1], "description": "Compute from a label; see :func:`compute`.", "specializations": []},
    ]
    lines = []
    docs.template_docstring(None, "function", "test.compute", sys.modules["test"].compute, None, lines)
    assert lines[0] == "Compute a value."
    assert all("_compute_" not in line and "Overloaded function." not in line for line in lines)


def test_function_overloads_only_available_for_some_specializations(monkeypatch):
    make_native_function(monkeypatch, conditional=True)
    info = docs.template_function_info("test.compute")
    assert info["signatures"] == ()
    assert len(info["overloads"]) == 2
    assert info["overloads"][0]["specializations"] == []
    assert info["overloads"][1]["specializations"] == ["compute[float]"]
    assert info["overloads"][1]["signature"] == "(label: str = 'a,b')"


def test_function_with_value_template_parameters():
    @_template_function("test.scale", parameters=["factor"], instantiations=(2, 3))
    def scale(factor, value: int) -> int:
        return factor * value

    entries = [(inst, "scale(value: int) -> int") for inst in scale.metadata.instantiations]
    assert docs.generic_docs(scale, entries, [], "scale") == entries


def test_functions_without_return_annotations_have_stable_defaults():
    assert (
        docs._public_signature("run(options: test._Options = <test._Options object at 0x123>, label: str = 'a,b')") == "run(options = ..., label: str = 'a,b')"
    )


def test_python_function_signatures_preserve_argument_kinds(monkeypatch):
    @_template_function("test.select", parameters=["ValueType"], instantiations=(float, int))
    def select(value_type, value: "int", /, *args: "str", option: "bool" = False, **kwargs: "int") -> "int":
        """Select a value.\n\n:param value: Input."""
        return value

    monkeypatch.setitem(sys.modules, "test", SimpleNamespace(select=select))
    info = docs.template_function_info("test.select")
    assert info["signatures"] == ("(value: int, /, *args: str, option: bool = False, **kwargs: int) -> int",)
    assert info["overloads"][0]["description"] == "Select a value.\n\n:param value: Input."


def test_real_native_function_uses_public_generic_types():
    info = docs.template_function_info("stormpy.developer.build_sparse_model")
    assert len(info["signatures"]) == 2
    signature = info["signatures"][0]
    assert "model: stormpy.SymbolicModelDescription" in signature
    assert "stormpy.developer.ExplicitModelBuilderOptions[ValueType] = ..." in signature
    assert "-> stormpy.models.SparseModel[ValueType]" in signature
    assert all(not docs._unresolved(overload["signature"]) for overload in info["overloads"])
    assert all("object at 0x" not in overload["signature"] for overload in info["overloads"])
    aliases = docs._public_type_names()
    assert aliases[f"{stormpy.logic.Property.__module__}.Property"] == "stormpy.logic.Property"
    assert aliases[f"{stormpy.models.ModelType.__module__}.ModelType"] == "stormpy.models.ModelType"


def test_real_python_function_resolves_forward_annotations():
    info = docs.template_function_info("stormpy.build_model")
    (signature,) = info["signatures"]
    assert "stormpy.io.PrismProgram | stormpy.io.JaniModel" in signature
    assert "collections.abc.Iterable[stormpy.logic.Property]" in signature
    assert "*, options:" in signature
    assert "engine: stormpy.Engine = stormpy.Engine.SPARSE" in signature
    assert ":param model:" in info["overloads"][0]["description"]
    dft = docs.template_function_info("stormpy.dft.load_dft_galileo_file")
    assert dft["signatures"] == ("(path: str | os.PathLike[str]) -> stormpy.dft.DFT",)


def test_real_native_conversion_preserves_conditional_overloads():
    info = docs.template_function_info("stormpy.developer.storage.to_value_type")
    assert info["signatures"] == ()
    assert all(not docs._unresolved(overload["signature"]) for overload in info["overloads"])
    assert any("stormpy.datastructures.Scheduler[float]" in overload["signature"] for overload in info["overloads"])
    assert any(overload["specializations"] for overload in info["overloads"])


def test_sphinx_renders_public_and_developer_apis(monkeypatch, tmp_path):
    pytest.importorskip("sphinx")
    from io import StringIO
    from types import ModuleType

    from sphinx.addnodes import pending_xref
    from sphinx.application import Sphinx

    family = make_native_function(monkeypatch)

    @_template_function("test.select", parameters=["ValueType"], instantiations=(float, int), deduce=_deduce_default(float))
    def select(value_type, value: int, *, label="a,b") -> int:
        """Select a value using :func:`compute`.

        :param value: The input value.
        :param label: The label.
        :return: The selected value.
        """
        return value

    module = ModuleType("test")
    module.compute, module.select = family, select
    monkeypatch.setitem(sys.modules, "test", module)
    developer = ModuleType("test.developer")
    developer.compute = family.publish_as("test.developer.compute")
    developer.select = select.publish_as("test.developer.select")
    developer.Template = make_family().publish_as("test.developer.Template")
    developer.Ordinary = type("Ordinary", (), {"__module__": developer.__name__, "__doc__": "An ordinary class."})
    developer.ApiError = type("ApiError", (Exception,), {"__module__": developer.__name__, "__doc__": "An API error."})
    developer.CONSTANT = 123
    module.developer = developer
    monkeypatch.setitem(sys.modules, "test.developer", developer)
    source = Path(__file__).parents[2] / "doc/source"
    config = runpy.run_path(str(source / "conf.py"))
    (tmp_path / "conf.py").write_text("")
    (tmp_path / "index.rst").write_text("Documentation\n=============\n\n.. toctree::\n\n   api\n   developer_api\n")
    (tmp_path / "api.rst").write_text(
        "API Documentation\n=================\n\n.. autosummary::\n   :toctree: api/generated\n   :template: autosummary/module.rst\n\n   test\n"
        "\n.. autosummary::\n   :toctree: api/generated\n   :template: autosummary/class.rst\n\n   stormpy.io.JaniModel\n"
        "\nSee :class:`stormpy.developer.storage.JaniModel` or :class:`Custom label <stormpy.developer.storage._storage.JaniModel>`.\n"
    )
    (tmp_path / "developer_api.rst").write_text(
        "Developer API Documentation\n===========================\n\n.. autosummary::\n   :toctree: developer_api/generated\n   :template: autosummary/module.rst\n\n   test.developer\n"
        "\n.. autosummary::\n   :toctree: developer_api/generated\n\n   test.developer.CONSTANT\n"
        "\n.. autosummary::\n   :toctree: developer_api/generated\n   :template: autosummary/class.rst\n\n   stormpy.numbers.developer.gmp.Rational\n"
    )
    warnings = StringIO()
    app = Sphinx(
        str(tmp_path),
        str(tmp_path),
        str(tmp_path / "html"),
        str(tmp_path / "doctrees"),
        "html",
        confoverrides={
            "extensions": ["stormpy_templates", "stormpy_developer", "sphinx.ext.autosummary"],
            "templates_path": [str(source / "_templates")],
            "html_static_path": [str(source / "_static")],
            "html_css_files": ["custom.css"],
            "autosummary_context": config["autosummary_context"],
            "autosummary_imported_members": True,
            "autoclass_content": "both",
            # The test loads conf.py through runpy, whose functions cannot be pickled.
            "suppress_warnings": ["config.cache"],
        },
        status=StringIO(),
        warning=warnings,
        warningiserror=True,
        freshenv=True,
    )
    app.build(force_all=True)
    assert app.statuscode == 0, warnings.getvalue()
    assert warnings.getvalue() == ""
    overview = (tmp_path / "api/generated/test.rst").read_text()
    assert "Functions" in overview
    assert "Module Attributes" not in overview
    assert "Classes" not in overview
    for name in ("compute", "select"):
        assert app.env.domains["py"].objects[f"test.{name}"].objtype == "function"
        html = (tmp_path / f"html/api/generated/test.{name}.html").read_text()
        assert "field-list" in html
        assert ":param" not in html
        assert "_compute_" not in html
        assert "object at 0x" not in html
        assert "Overloaded function." not in html
    html = (tmp_path / "html/api/generated/test.select.html").read_text()
    assert 'href="test.compute.html#test.compute"' in html
    jani = (tmp_path / "html/api/generated/stormpy.io.JaniModel.html").read_text()
    assert "other_model" in jani
    assert 'href="#stormpy.io.JaniModel" title="stormpy.io.JaniModel"' in jani
    api = (tmp_path / "html/api.html").read_text()
    assert 'href="api/generated/stormpy.io.JaniModel.html#stormpy.io.JaniModel"' in api
    assert "Custom label" in re.sub(r"<[^>]*>", "", api)
    # Inspect page content and type-reference targets, excluding shared navigation.
    developer_name = re.compile(r"\b(?:[A-Za-z_]\w*\.)+developer(?:\.[A-Za-z_]\w*)*\b")
    for docname in sorted(app.env.found_docs):
        if docname != "api" and not docname.startswith("api/"):
            continue
        tree = app.env.get_doctree(docname)
        mentions = set(developer_name.findall(tree.astext()))
        for reference in tree.findall(pending_xref):
            mentions.update(developer_name.findall(reference.get("reftarget", "")))
        assert not mentions, f"Developer API mentioned in {docname}: {sorted(mentions)}"
    disclaimer = "The stormpy developer API is internal and always subject to change."
    for page in (tmp_path / "html/api").rglob("*.html"):
        assert disclaimer not in page.read_text()
    for name in (
        "test.developer",
        "test.developer.compute",
        "test.developer.select",
        "test.developer.Template",
        "test.developer.Ordinary",
        "test.developer.ApiError",
        "test.developer.CONSTANT",
        "stormpy.numbers.developer.gmp.Rational",
    ):
        html = (tmp_path / f"html/developer_api/generated/{name}.html").read_text()
        assert html.count(disclaimer) == 1
        assert "developer-api-warning" in html
    assert disclaimer in (tmp_path / "html/developer_api.html").read_text()
    developer_index = (tmp_path / "html/developer_api.html").read_text()
    assert 'href="developer_api/generated/stormpy.numbers.developer.gmp.Rational.html#stormpy.numbers.developer.gmp.Rational"' in developer_index
    assert "developer-api-warning" in (tmp_path / "html/_static/custom.css").read_text()


def test_public_api_filter_includes_refactored_implementations(monkeypatch):
    config = runpy.run_path(str(Path(__file__).parents[2] / "doc/source/conf.py"))
    implementation = type("Public", (), {"__module__": "test.developer._core"})
    monkeypatch.setitem(sys.modules, "test.public", SimpleNamespace(__all__=["Public"], Public=implementation, Imported=object(), _private=object()))
    assert config["_filter_api_members"]("test.public", ["Public", "Imported", "_private"]) == ["Public"]


def test_developer_api_filter_omits_published_aliases(monkeypatch):
    config = runpy.run_path(str(Path(__file__).parents[2] / "doc/source/conf.py"))
    family = make_family().publish_as("test.developer.Example")
    shared = object()
    monkeypatch.setitem(sys.modules, "test.developer", SimpleNamespace(Example=family, Shared=shared, Raw=object()))
    monkeypatch.setitem(sys.modules, "test.public", SimpleNamespace(Example=family.publish_as("test.public.Example"), Shared=shared))
    config["_PUBLIC_MODULES"]["test.developer"] = ("test.public",)
    assert config["_filter_api_members"]("test.developer", ["Example", "Shared", "Raw"]) == ["Raw"]


def test_core_bindings_moved_to_other_public_modules_are_not_duplicated(monkeypatch):
    config = runpy.run_path(str(Path(__file__).parents[2] / "doc/source/conf.py"))
    property_type, direction_type, log_level_type = object(), object(), object()
    monkeypatch.setitem(
        sys.modules, "stormpy.developer", SimpleNamespace(Property=property_type, OptimizationDirection=direction_type, LogLevel=log_level_type, Raw=object())
    )
    monkeypatch.setitem(sys.modules, "stormpy.logic", SimpleNamespace(Property=property_type, OptimizationDirection=direction_type))
    monkeypatch.setitem(sys.modules, "stormpy.utility", SimpleNamespace(LogLevel=log_level_type))
    assert config["_filter_api_members"]("stormpy.developer", ["Property", "OptimizationDirection", "LogLevel", "Raw"]) == ["Raw"]


def test_template_docstring_uses_native_description():
    lines = ["Native C++ template family exposed as a subscriptable Python object."]
    docs.template_docstring(None, "class", "stormpy.dft.DFT", stormpy.dft.DFT, None, lines)
    assert lines == ["Dynamic Fault Tree"]


def test_non_template_docstring_is_unchanged():
    lines = ["Ordinary class description."]
    docs.template_docstring(None, "class", "Example", object, None, lines)
    assert lines == ["Ordinary class description."]


def test_constructor_descriptions_in_class_body():
    family = make_family()
    for inst in family.metadata.instantiations:

        def constructor(self):
            pass

        typ = docs.argument_name(inst.arguments[0])
        constructor.__doc__ = f"__init__(self: {inst.native_name}, value: {typ}) -> None\n\nCreate an example.\n\n:param value: Initial value."
        inst.implementation.__init__ = constructor
    assert docs.constructor_descriptions(family, [family]) == [("Create an example.\n\n:param value: Initial value.", [])]
    assert docs.constructors(family, [family]) == (("(value: ValueType)",), [])
    assert "Example.__init__" not in docs.render_members(family, [family])


def test_constructor_descriptions_preserve_specialization_differences():
    family = make_family()
    for inst in family.metadata.instantiations:

        def constructor(self):
            pass

        typ = docs.argument_name(inst.arguments[0])
        constructor.__doc__ = f"__init__(self: {inst.native_name}) -> None\n\nCreate the {typ} specialization."
        inst.implementation.__init__ = constructor
    assert docs.constructor_descriptions(family, [family]) == [
        ("Create the float specialization.", ["Example[float]"]),
        ("Create the int specialization.", ["Example[int]"]),
    ]


def test_inherited_object_constructor_description_is_omitted():
    family = make_family()
    assert docs.constructor_descriptions(family, [family]) == []


def test_public_aliases():
    assert docs.argument_name(stormpy.Rational) == "stormpy.Rational"
    assert docs.argument_name(stormpy.Interval) == "stormpy.Interval"
    assert docs.argument_name(stormpy.RationalInterval) == "stormpy.RationalInterval"
    assert docs.argument_name(stormpy.RationalFunction) == "stormpy.RationalFunction"
    assert docs.argument_name(stormpy.models.DdType.Sylvan) == "stormpy.models.DdType.Sylvan"
    assert all("_storage" not in docs.specialization_name(stormpy.models.SparseMdp, inst) for inst in stormpy.models.SparseMdp.metadata.instantiations)


def test_pybind_overloads():
    doc = """get(self: test._Floating, value: float) -> float\nOverloaded function.\n\n1. get(self: test._Floating, value: float) -> float\n\n2. get(self: test._Floating, value: int) -> float\n\nDescription."""
    indexes = docs.signature_lines(doc, "get")
    assert indexes == [0, 3, 5]
    assert docs.signature_lines("get(self: test.Example[ValueType])\n\nDescription.", "get") == [0]
    assert "Description." not in [doc.splitlines()[i] for i in indexes]


def test_overload_substitution_and_unrecognized_cpp_types():
    family = make_family()
    entries = []
    for inst in family.metadata.instantiations:
        typ = docs.argument_name(inst.arguments[0])
        entries.append(
            (
                inst,
                f"""shared(*args, **kwargs)\nOverloaded function.\n\n1. shared(self: {inst.native_name}, value: {typ}) -> {typ}\n\n2. shared(self: {inst.native_name}, value: int) -> storm::opaque<{typ}>\n\nShared method.""",
            )
        )
    variants = docs.generic_docs(family, entries, [family], "shared")
    assert all("1. shared(self: test.Example[ValueType], value: ValueType) -> ValueType" in text for _, text in variants)
    assert all("storm::opaque<" not in text for _, text in variants)
    assert all("2. shared(self: test.Example[ValueType], value: int)" in text for _, text in variants)
    assert all("Shared method." in text for _, text in variants)


def test_unresolved_annotations_are_omitted_not_overloads():
    assert (
        docs._public_signature(
            "run(self: stormpy._core._CheckResult, components: storm::Components<std::pair<int, int>>, limit: int = 5) -> storm::Result<int>"
        )
        == "run(self, components, limit: int = 5)"
    )
    assert docs._public_signature("run(self: stormpy.models.SparseMdp[ValueType]) -> float") == "run(self: stormpy.models.SparseMdp[ValueType]) -> float"


def test_constructor_deduction_descriptions():
    assert "SparseMatrix[float]" in docs.deduction_description(stormpy.datastructures.SparseMatrix)
    inferred = docs.deduction_description(stormpy.models.SparseMdp)
    assert "first positional constructor argument" in inferred
    assert "``components`` or ``other_model``" in inferred
    assert "[float]" not in inferred
    second = docs.deduction_description(stormpy.datastructures.MemoryStructureBuilder)
    assert "second positional constructor argument" in second
    assert "``model``" in second
    fallback = docs.deduction_description(stormpy.models.SparseModelComponents)
    assert "``transition_matrix``" in fallback
    assert "If none is supplied, ``SparseModelComponents[float]``" in fallback
    assert "first positional constructor argument" in docs.deduction_description(stormpy.dft.developer.DFTTraceSimulator)
    assert "``dft``" in docs.deduction_description(stormpy.dft.developer.DFTTraceSimulator)
    assert docs.deduction_description(stormpy.developer.storage.Add) is None


def test_real_constructor_overloads_are_not_dropped():
    family = stormpy.models.SparseCtmc
    output = docs.render_members(family, [family, stormpy.models.SparseModel])
    signatures, variants = docs.constructors(family, [family, stormpy.models.SparseModel])
    assert signatures == ("(other_model: stormpy.models.SparseCtmc[ValueType])", "(components)")
    assert variants == []
    assert "SparseCtmc.__init__" not in output
    assert "SparseCtmc.__str__" not in output
    assert ".. py:method:: SparseCtmc.collect_reward_parameters(self: stormpy.models.SparseModel[stormpy.RationalFunction])" in output
    assert ".. code-block:: text\n\n      collect_reward_parameters(" not in output


def test_object_defaults_do_not_split_generic_signatures():
    family = make_family()
    for index, inst in enumerate(family.metadata.instantiations):

        def constructor(self):
            pass

        constructor.__doc__ = f"__init__(self: {inst.native_name}, options: test._Options = <test._Options object at 0x{index + 1:x}>) -> None"
        inst.implementation.__init__ = constructor
    signatures, variants = docs.constructors(family, [family])
    assert signatures == ("(options = ...)",)
    assert variants == []


def test_developer_dft_builder_constructor():
    family = stormpy.dft.developer.ExplicitDFTModelBuilder
    output = docs.render_members(family, [family])
    signatures, variants = docs.constructors(family, [family])
    assert signatures == ("(env, dft, symmetries)",)
    assert variants == []
    assert "ExplicitDFTModelBuilder.__init__" not in output
    assert "object at 0x" not in output


def test_specialization_specific_constructors_are_retained():
    family = stormpy.models.SparseRewardModel
    signatures, variants = docs.constructors(family, [family])
    assert not signatures
    assert variants
    assert all("SparseRewardModel[" in specialization for specialization, _ in variants)
    assert all("ValueType" not in signature for _, signature in variants)


def test_real_conditional_methods_and_unrecognized_signatures():
    output = docs.render_members(stormpy.datastructures.Scheduler, [stormpy.datastructures.Scheduler])
    assert ".. py:method:: Scheduler.to_value_type" in output
    assert "cast_to_double_datatype" not in output
    check = docs.render_members(stormpy.ExplicitQualitativeCheckResult, [stormpy.ExplicitQualitativeCheckResult])
    assert ".. py:method:: ExplicitQualitativeCheckResult.get_truth_values_vector" in check
    assert "storm::modelchecker::ExplicitQualitativeCheckResult" not in check
    matrix = docs.render_members(
        stormpy.datastructures.SparseMatrix,
        [stormpy.datastructures.SparseMatrix, stormpy.datastructures.SparseMatrixRows, stormpy.datastructures.SparseMatrixEntry],
    )
    assert "stormpy.datastructures.SparseMatrixEntry[ValueType]" in matrix
    assert ".. py:property:: SparseMatrix.nr_rows" in matrix
    ma = docs.render_members(stormpy.models.SparseMA, [stormpy.models.SparseMA])
    assert ".. py:property:: SparseMA.supports_parameters" in ma
    assert "Type: ``bool``" not in ma
    state = docs.render_members(stormpy.developer.storage.SparseModelState, [stormpy.developer.storage.SparseModelState])
    assert "SparseModelState.__int__" not in state
    assert "SparseModelState.__new__" not in state
