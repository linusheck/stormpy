import pytest
import stormpy
import stormpy.examples
import stormpy.examples.files
from stormpy.exceptions import StormError

from helpers.helper import get_example_path
from configurations import pars


class TestBuilding:
    def test_explicit_builder(self):
        path = stormpy.examples.files.prism_dtmc_die
        prism_program = stormpy.parse_prism_program(path)
        formula_str = "P=? [F s=7 & d=2]"
        properties = stormpy.parse_properties(formula_str, prism_program)

        # Fix variables in the program.
        module = prism_program.modules[0]
        s_var = module.get_integer_variable("s").expression_variable
        d_var = module.get_integer_variable("d").expression_variable

        # Construct the model
        options = stormpy.BuilderOptions([p.get_raw_formula() for p in properties])
        options.set_build_state_valuations()
        model_builder = stormpy.developer.make_explicit_model_builder(prism_program, options)
        model = model_builder.build()
        # and export the model from building
        state_mapping = model_builder.export_explicit_state_lookup()

        # lookup 1
        state = {s_var: prism_program.expression_manager.create_integer(3), d_var: prism_program.expression_manager.create_integer(0)}
        id = state_mapping.lookup(state)
        assert model.state_valuations.get_value(id, s_var) == 3
        assert model.state_valuations.get_value(id, d_var) == 0

        # lookup 2
        state = {s_var: prism_program.expression_manager.create_integer(7), d_var: prism_program.expression_manager.create_integer(3)}
        id = state_mapping.lookup(state)
        assert model.state_valuations.get_value(id, s_var) == 7
        assert model.state_valuations.get_value(id, d_var) == 3

    @pytest.mark.parametrize(
        "value_type", [float, stormpy.Rational, pytest.param(stormpy.RationalFunction, marks=pars), stormpy.Interval, stormpy.RationalInterval]
    )
    def test_build_model_value_types(self, value_type):
        program = stormpy.parse_prism_program(
            get_example_path("idtmc", "die-intervals.pm") if value_type in (stormpy.Interval, stormpy.RationalInterval) else get_example_path("dtmc", "die.pm")
        )
        model = stormpy.build_model(program, value_type=value_type)
        assert type(model) is stormpy.SparseDtmc[value_type]
        assert model.nr_states == 13

    def test_build_model_unsupported_value_type(self):
        program = stormpy.parse_prism_program(get_example_path("dtmc", "die.pm"))
        with pytest.raises(TypeError, match="Supported are: float, "):
            stormpy.build_model(program, value_type=int)

    def test_build_model_all_labels(self):
        program = stormpy.parse_prism_program(get_example_path("dtmc", "die.pm"))
        model = stormpy.build_model(program)
        assert "one" in model.labeling.get_labels()
        assert "coin_flips" in model.reward_models
        properties = stormpy.parse_properties('P=? [F "one"]', program)
        model = stormpy.build_model(program, properties)
        assert "one" in model.labeling.get_labels()
        assert "two" not in model.labeling.get_labels()
        assert len(model.reward_models) == 0

    def test_build_model_with_options(self):
        program = stormpy.parse_prism_program(get_example_path("dtmc", "die.pm"))
        options = stormpy.BuilderOptions(True, True)
        options.set_build_state_valuations()
        model = stormpy.build_model(program, options=options)
        assert model.has_state_valuations()
        properties = stormpy.parse_properties('P=? [F "one"]', program)
        with pytest.raises(StormError):
            stormpy.build_model(program, properties, options=options)

    def test_builder_options_defaults(self):
        options = stormpy.BuilderOptions()
        assert not options.is_build_all_labels_set()
        assert not options.is_build_all_reward_models_set()

    def test_build_model_undefined_constants(self):
        program = stormpy.parse_prism_program(get_example_path("dtmc", "brp.pm"))
        with pytest.raises(StormError):
            stormpy.build_model(program)

    @pars
    def test_build_parametric_model_from_drn(self):
        model = stormpy.build_model_from_drn(get_example_path("pdtmc", "die.drn"), value_type=stormpy.RationalFunction)
        assert type(model) is stormpy.SparseDtmc[stormpy.RationalFunction]
        assert model.has_parameters

    def test_build_model_from_explicit_with_rewards(self):
        model = stormpy.build_model_from_explicit(get_example_path("dtmc", "die.tra"), get_example_path("dtmc", "die.lab"))
        assert type(model) is stormpy.SparseDtmc[float]
        assert model.nr_states == 13

    @pytest.mark.parametrize("value_type", [float, stormpy.Rational, pytest.param(stormpy.RationalFunction, marks=pars)])
    def test_build_symbolic_model_value_types(self, value_type):
        program = stormpy.parse_prism_program(get_example_path("dtmc", "die.pm"))
        model = stormpy.build_symbolic_model(program, value_type=value_type)
        assert type(model) is stormpy.SymbolicDtmc[stormpy.DdType.Sylvan, value_type]
        assert model.nr_states == 13

    def test_build_symbolic_model_interval(self):
        program = stormpy.parse_prism_program(get_example_path("dtmc", "die.pm"))
        with pytest.raises(StormError):
            stormpy.build_symbolic_model(program, value_type=stormpy.Interval)
