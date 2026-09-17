from types import SimpleNamespace

import pytest

from stormpy._template import TemplateClass, deduce_default, deduce_from_first_argument, deduce_from_object


class BaseImplementation:
    def __init__(self, source=None):
        self.source = source


class DerivedImplementation(BaseImplementation):
    pass


def make_family(*, deduce=None) -> TemplateClass:
    module = SimpleNamespace(_template_instantiations={"Example": {("base",): BaseImplementation}})
    return TemplateClass("test.Example", module, parameters=["kind"], deduce=deduce)


def test_deduction_selects_exact_registered_subclass():
    family = make_family(deduce=deduce_from_first_argument())
    family.register("derived", DerivedImplementation)
    source = DerivedImplementation()

    result = family(source)

    assert type(result) is DerivedImplementation
    assert result.source is source


def test_default_deduction_selects_configured_instantiation():
    family = make_family(deduce=deduce_default("base"))

    result = family()

    assert type(result) is BaseImplementation


def test_deduction_rejects_unregistered_subclass():
    class UnregisteredImplementation(BaseImplementation):
        pass

    family = make_family(deduce=deduce_from_first_argument())
    source = UnregisteredImplementation()

    with pytest.raises(TypeError, match="Cannot infer Example template parameters"):
        family(source)
    assert not family.is_instantiation(source)


def test_cannot_register_implementation_for_multiple_parameters():
    family = make_family()

    with pytest.raises(ValueError, match="already registered for .*base"):
        family.register("duplicate", BaseImplementation)

    assert ("duplicate",) not in family.instantiations
    assert family.parameters_of(BaseImplementation()) == ("base",)


def test_object_deduction_transforms_argument():
    family = make_family(deduce=deduce_from_object(lambda obj: obj.kind, keyword="source"))
    family.register("derived", DerivedImplementation)
    source = SimpleNamespace(kind="derived")

    for result in (family(source), family(source=source)):
        assert type(result) is DerivedImplementation
        assert result.source is source


def test_object_deduction_argument_selection():
    guide = deduce_from_object(lambda obj: float if obj is None else obj.kind, keyword="model")
    source = SimpleNamespace(kind=int)
    alternate = SimpleNamespace(kind=str)

    assert guide(None, (source,), {"model": alternate}) is int
    assert guide(None, (), {"model": alternate}) is str
    assert guide(None, (), {}) is float
    assert guide(None, (), {"model": None}) is float


def test_object_deduction_keyword_aliases():
    guide = deduce_from_object(type, keyword=("components", "other_model"))

    assert guide(None, (), {"other_model": 1}) is int
    assert guide(None, (), {"components": 1.0, "other_model": 1}) is float
    assert guide(None, (), {"components": None, "other_model": 1}) is type(None)
    assert guide(None, (1,), {"components": 1.0}) is int


def test_object_deduction_second_argument():
    guide = deduce_from_object(type, keyword="model", position=1)

    assert guide(None, (2, 1.0), {"model": 1}) is float
    assert guide(None, (2,), {"model": 1.0}) is float
    assert guide(None, (), {"model": 1.0}) is float
    assert guide(None, (2,), {}) is type(None)
