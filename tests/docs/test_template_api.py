"""Sphinx template renderer tests; can run without importing Sphinx itself."""

import importlib.util
import runpy
import sys
from pathlib import Path
from types import SimpleNamespace

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
    assert info["descriptions"] == [("scale(value: int) -> int\n\nScale a value.", ["scale[float]", "scale[int]"])]


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
