import pytest
import stormpy
from stormpy.exceptions import StormError

from helpers.helper import get_example_path


class TestAnalysis:
    def test_topological_sort(self):
        program = stormpy.parse_prism_program(get_example_path("dtmc", "die.pm"))
        model = stormpy.build_model(program)
        order = stormpy.topological_sort(model)
        assert sorted(order) == list(range(model.nr_states))
        backward = stormpy.topological_sort(model, forward=False, initial=[7])
        assert len(backward) > 0

    def test_create_weight_vector_checker_unsupported(self):
        program = stormpy.parse_prism_program(get_example_path("mdp", "multiobjective1.nm"))
        properties = stormpy.parse_properties('multi(Pmax=? [ F<=3 s=2 ],R{"rew"}max=? [ F s=2 ])', program)
        model = stormpy.build_model[stormpy.numbers.Interval](program, properties)
        with pytest.raises(StormError):
            stormpy.create_weight_vector_checker(model, properties[0])
