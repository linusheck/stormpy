import pytest
import stormpy
from helpers.helper import build_sparse_model, get_example_path

from configurations import spot

import math


def test_symbolic_filter_template_and_shared_dd_type():
    program = stormpy.parse_prism_program(get_example_path("dtmc", "die.pm"))
    model = stormpy.build_symbolic_model(program)
    result = stormpy.create_filter_initial_states(model)

    assert stormpy.DdType is stormpy.storage.DdType
    assert type(result) is stormpy.SymbolicQualitativeCheckResult[stormpy.DdType.Sylvan]
    assert stormpy.storage.Bdd.parameters_of(result.get_truth_values_vector()) == (stormpy.DdType.Sylvan,)


@pytest.mark.parametrize("value_type", [float, stormpy.Rational, stormpy.RationalFunction])
def test_initial_state_filter_overloads(value_type):
    model = build_sparse_model(get_example_path("dtmc", "die.pm"), value_type)
    result = stormpy.create_filter_initial_states(model)

    assert type(result) is stormpy.ExplicitQualitativeCheckResult[value_type]
    assert result.get_truth_values_vector() == model.initial_states_as_bitvector


class TestModelChecking:
    def test_model_checking_prism_dtmc_label(self):
        program = stormpy.parse_prism_program(get_example_path("dtmc", "die.pm"))
        formulas = stormpy.parse_properties('P=? [ F "one" ]', program)
        model = stormpy.build_model(program, formulas)
        assert model.nr_states == 13
        assert model.nr_transitions == 20
        assert len(model.initial_states) == 1
        initial_state = model.initial_states[0]
        assert initial_state == 0
        result = stormpy.model_checking(model, formulas[0])
        assert math.isclose(result[initial_state], 1 / 6)

    def test_model_checking_prism_dtmc_p(self):
        program = stormpy.parse_prism_program(get_example_path("dtmc", "die.pm"))
        formulas = stormpy.parse_properties("P=? [ F s=2 ]", program)
        model = stormpy.build_model(program, formulas)
        assert model.nr_states == 8
        assert model.nr_transitions == 12
        assert len(model.initial_states) == 1
        initial_state = model.initial_states[0]
        assert initial_state == 0
        result = stormpy.model_checking(model, formulas[0])
        assert math.isclose(result[initial_state], 1 / 2)

    def test_model_checking_prism_dtmc_reward(self):
        program = stormpy.parse_prism_program(get_example_path("dtmc", "die.pm"))
        formulas = stormpy.parse_properties('R=? [F "done"]', program)
        model = stormpy.build_model(program, formulas)
        assert model.nr_states == 13
        assert model.nr_transitions == 20
        assert len(model.initial_states) == 1
        initial_state = model.initial_states[0]
        assert initial_state == 0
        result = stormpy.model_checking(model, formulas[0])
        assert math.isclose(result[initial_state], 11 / 3)

    @spot
    def test_model_checking_prism_dtmc_ltl(self):
        program = stormpy.parse_prism_program(get_example_path("dtmc", "die.pm"))
        formulas = stormpy.parse_properties('P=? [ FG "one" ]', program)
        model = stormpy.build_model(program, formulas)
        assert model.nr_states == 13
        assert model.nr_transitions == 20
        assert len(model.initial_states) == 1
        initial_state = model.initial_states[0]
        assert initial_state == 0
        result = stormpy.model_checking(model, formulas[0])
        assert math.isclose(result[initial_state], 1 / 6)

    def test_model_checking_prism_mdp(self):
        program = stormpy.parse_prism_program(get_example_path("mdp", "coin2-2.nm"))
        formulas = stormpy.parse_properties('Pmin=? [ F "finished" & "all_coins_equal_1"]', program)
        model = stormpy.build_model(program, formulas)
        assert model.nr_states == 272
        assert model.nr_transitions == 492
        assert len(model.initial_states) == 1
        initial_state = model.initial_states[0]
        assert initial_state == 0
        result = stormpy.model_checking(model, formulas[0])
        assert math.isclose(result[initial_state], 49 / 128, rel_tol=1e-5)

    def test_model_checking_interval_dtmc(self):
        program = stormpy.parse_prism_program(get_example_path("idtmc", "die-intervals.pm"))
        formulas = stormpy.parse_properties('P=? [ F "one"]')
        model = stormpy.build_model(program, formulas, value_type=stormpy.Interval)
        initial_state = model.initial_states[0]
        assert initial_state == 0

        env = stormpy.Environment()
        env.solver().min_max().method = stormpy.MinMaxMethod.VALUE_ITERATION

        # Compute maximal
        result = stormpy.model_checking(
            model,
            formulas[0],
            only_initial_states=True,
            extract_scheduler=True,
            uncertainty_resolution_mode=stormpy.UncertaintyResolutionMode.MAXIMIZE,
            environment=env,
        )
        assert math.isclose(result[initial_state], 72.0 / 189.0, rel_tol=1e-4)
        # Compute minimal
        result = stormpy.model_checking(
            model,
            formulas[0],
            only_initial_states=True,
            extract_scheduler=True,
            uncertainty_resolution_mode=stormpy.UncertaintyResolutionMode.MINIMIZE,
            environment=env,
        )
        assert math.isclose(result[initial_state], 9.0 / 189.0, rel_tol=1e-4)

    def test_model_checking_interval_mdp(self):
        model = stormpy.build_model_from_drn(get_example_path("imdp", "tiny-01.drn"), value_type=stormpy.Interval)
        formulas = stormpy.parse_properties('Pmax=? [ F "target"];Pmin=? [ F "target"]')
        initial_state = model.initial_states[0]
        assert initial_state == 0

        env = stormpy.Environment()
        env.solver().min_max().method = stormpy.MinMaxMethod.VALUE_ITERATION

        # Compute maximal robust
        result = stormpy.model_checking(
            model,
            formulas[0],
            only_initial_states=True,
            extract_scheduler=True,
            uncertainty_resolution_mode=stormpy.UncertaintyResolutionMode.ROBUST,
            environment=env,
        )
        assert math.isclose(result[initial_state], 0.4, rel_tol=1e-4)
        # Compute maximal cooperative
        result = stormpy.model_checking(
            model,
            formulas[0],
            only_initial_states=True,
            extract_scheduler=True,
            uncertainty_resolution_mode=stormpy.UncertaintyResolutionMode.COOPERATIVE,
            environment=env,
        )
        assert math.isclose(result[initial_state], 0.5, rel_tol=1e-4)

        # Compute minimal robust
        result = stormpy.model_checking(
            model,
            formulas[1],
            only_initial_states=True,
            extract_scheduler=True,
            uncertainty_resolution_mode=stormpy.UncertaintyResolutionMode.ROBUST,
            environment=env,
        )
        assert math.isclose(result[initial_state], 0.5, rel_tol=1e-4)
        # Compute minimal cooperative
        result = stormpy.model_checking(
            model,
            formulas[1],
            only_initial_states=True,
            extract_scheduler=True,
            uncertainty_resolution_mode=stormpy.UncertaintyResolutionMode.COOPERATIVE,
            environment=env,
        )
        assert math.isclose(result[initial_state], 0.4, rel_tol=1e-4)

    def test_model_checking_exact_interval_dtmc(self):
        program = stormpy.parse_prism_program(get_example_path("idtmc", "die-intervals.pm"))
        formulas = stormpy.parse_properties('P=? [ F "one"]')
        model = stormpy.build_model(program, formulas, value_type=stormpy.RationalInterval)
        initial_state = model.initial_states[0]
        assert initial_state == 0

        env = stormpy.Environment()
        env.solver().min_max().method = stormpy.MinMaxMethod.VALUE_ITERATION

        # Compute maximal
        result = stormpy.model_checking(
            model,
            formulas[0],
            only_initial_states=True,
            extract_scheduler=True,
            uncertainty_resolution_mode=stormpy.UncertaintyResolutionMode.MAXIMIZE,
            environment=env,
        )
        assert math.isclose(result[initial_state], 72.0 / 189.0, rel_tol=1e-4)
        # Compute minimal
        result = stormpy.model_checking(
            model,
            formulas[0],
            only_initial_states=True,
            extract_scheduler=True,
            uncertainty_resolution_mode=stormpy.UncertaintyResolutionMode.MINIMIZE,
            environment=env,
        )
        assert math.isclose(result[initial_state], 9.0 / 189.0, rel_tol=1e-4)

    def test_model_checking_exact_interval_mdp(self):
        model = stormpy.build_model_from_drn(get_example_path("imdp", "tiny-01.drn"), value_type=stormpy.RationalInterval)
        formulas = stormpy.parse_properties('Pmax=? [ F "target"];Pmin=? [ F "target"]')
        initial_state = model.initial_states[0]
        assert initial_state == 0

        env = stormpy.Environment()
        env.solver().min_max().method = stormpy.MinMaxMethod.VALUE_ITERATION

        # Compute maximal robust
        result = stormpy.model_checking(
            model,
            formulas[0],
            only_initial_states=True,
            extract_scheduler=True,
            uncertainty_resolution_mode=stormpy.UncertaintyResolutionMode.ROBUST,
            environment=env,
        )
        assert math.isclose(result[initial_state], 0.4, rel_tol=1e-4)
        # Compute maximal cooperative
        result = stormpy.model_checking(
            model,
            formulas[0],
            only_initial_states=True,
            extract_scheduler=True,
            uncertainty_resolution_mode=stormpy.UncertaintyResolutionMode.COOPERATIVE,
            environment=env,
        )
        assert math.isclose(result[initial_state], 0.5, rel_tol=1e-4)

        # Compute minimal robust
        result = stormpy.model_checking(
            model,
            formulas[1],
            only_initial_states=True,
            extract_scheduler=True,
            uncertainty_resolution_mode=stormpy.UncertaintyResolutionMode.ROBUST,
            environment=env,
        )
        assert math.isclose(result[initial_state], 0.5, rel_tol=1e-4)
        # Compute minimal cooperative
        result = stormpy.model_checking(
            model,
            formulas[1],
            only_initial_states=True,
            extract_scheduler=True,
            uncertainty_resolution_mode=stormpy.UncertaintyResolutionMode.COOPERATIVE,
            environment=env,
        )
        assert math.isclose(result[initial_state], 0.4, rel_tol=1e-4)

    def test_model_checking_jani_dtmc(self):
        jani_model, formulas = stormpy.parse_jani_model(get_example_path("dtmc", "die.jani"))
        formulas = stormpy.storage.eliminate_reward_accumulations(jani_model, formulas)
        assert len(formulas) == 2
        model = stormpy.build_model(jani_model, formulas)
        assert model.nr_states == 13
        assert model.nr_transitions == 20
        assert len(model.initial_states) == 1
        initial_state = model.initial_states[0]
        assert initial_state == 0
        result = stormpy.model_checking(model, formulas[0])
        assert math.isclose(result[initial_state], 1 / 6)
        result = stormpy.model_checking(model, formulas[1])
        assert math.isclose(result[initial_state], 11 / 3)

    def test_model_checking_dtmc_all_labels(self):
        program = stormpy.parse_prism_program(get_example_path("dtmc", "die.pm"))
        formulas = stormpy.parse_properties('P=? [ F "one" ]', program)
        model = stormpy.build_model(program)
        assert model.nr_states == 13
        assert model.nr_transitions == 20
        assert len(model.initial_states) == 1
        initial_state = model.initial_states[0]
        assert initial_state == 0
        result = stormpy.model_checking(model, formulas[0])
        assert math.isclose(result[initial_state], 1 / 6)
        formulas = stormpy.parse_properties('P=? [ F "two" ]', program)
        result = stormpy.model_checking(model, formulas[0])
        assert math.isclose(result[initial_state], 1 / 6)

    def test_model_checking_all_dtmc(self):
        program = stormpy.parse_prism_program(get_example_path("dtmc", "die.pm"))
        formulas = stormpy.parse_properties('P=? [ F "one" ]', program)
        model = stormpy.build_model(program, formulas)
        assert model.nr_states == 13
        assert model.nr_transitions == 20
        result = stormpy.model_checking(model, formulas[0])
        assert result.is_result_for_all_states()
        reference = [1 / 6, 1 / 3, 0, 2 / 3, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        assert all(map(math.isclose, result.get_finite_value_vector(), reference))

    def test_model_checking_only_initial(self):
        program = stormpy.parse_prism_program(get_example_path("dtmc", "die.pm"))
        formulas = stormpy.parse_properties('Pmax=? [F{"coin_flips"}<=3 "one"]', program)
        model = stormpy.build_model(program, formulas)
        assert len(model.initial_states) == 1
        initial_state = model.initial_states[0]
        assert initial_state == 0
        result = stormpy.model_checking(model, formulas[0], only_initial_states=True)
        assert not result.is_result_for_all_states()
        assert math.isclose(result[initial_state], 1 / 8)

    def test_model_checking_prob01(self):
        program = stormpy.parse_prism_program(get_example_path("dtmc", "die.pm"))
        formulaPhi = stormpy.parse_properties("true")[0]
        formulaPsi = stormpy.parse_properties('"six"')[0]
        model = stormpy.build_model(program, [formulaPsi])
        phiResult = stormpy.model_checking(model, formulaPhi)
        phiStates = phiResult.get_truth_values_vector()
        assert phiStates.number_of_set_bits() == model.nr_states
        psiResult = stormpy.model_checking(model, formulaPsi)
        psiStates = psiResult.get_truth_values_vector()
        assert psiStates.number_of_set_bits() == 1
        prob0, prob1 = stormpy.developer.perform_prob01(model, phiStates, psiStates)
        assert prob0.number_of_set_bits() == 9
        assert prob1.number_of_set_bits() == 1
        labelprop = stormpy.Property("cora", formulaPsi.get_raw_formula(), set())
        result = stormpy.model_checking(model, labelprop)
        assert result.get_truth_values_vector().number_of_set_bits() == 1

        program = stormpy.parse_prism_program(get_example_path("mdp", "coin2-2.nm"))
        formulas = stormpy.parse_properties('Pmin=? [ F "finished" & "all_coins_equal_1"]', program)
        model = stormpy.build_model(program, formulas)
        psi_states = stormpy.model_checking(model, formulas[0].get_raw_formula().subformula.subformula).get_truth_values_vector()
        prob0, prob1 = stormpy.developer.perform_prob01_min(model, stormpy.BitVector(model.nr_states, True), psi_states)
        assert prob0.number_of_set_bits() == 94
        assert prob1.number_of_set_bits() == 15
        psi_states = stormpy.model_checking(model, formulas[0].get_raw_formula().subformula.subformula).get_truth_values_vector()
        prob0, prob1 = stormpy.developer.perform_prob01_max(model, stormpy.BitVector(model.nr_states, True), psi_states)
        assert prob0.number_of_set_bits() == 83
        assert prob1.number_of_set_bits() == 18

    def test_model_checking_ctmc(self):
        model = stormpy.build_model_from_drn(get_example_path("ctmc", "dft.drn"))
        formulas = stormpy.parse_properties('T=? [ F "failed" ]')
        assert model.nr_states == 16
        assert model.nr_transitions == 33
        assert len(model.initial_states) == 1
        initial_state = model.initial_states[0]
        assert initial_state == 1
        result = stormpy.model_checking(model, formulas[0])
        assert math.isclose(result[initial_state], 4.166666667)

    def test_filter(self):
        program = stormpy.parse_prism_program(get_example_path("dtmc", "die.pm"))
        formulas = stormpy.parse_properties('P=? [ F "one" ]', program)
        model = stormpy.build_model(program, formulas)
        assert model.nr_states == 13
        assert model.nr_transitions == 20
        assert len(model.initial_states) == 1
        initial_state = model.initial_states[0]
        assert initial_state == 0
        result = stormpy.model_checking(model, formulas[0])
        assert math.isclose(result[initial_state], 1 / 6)
        filter = stormpy.create_filter_initial_states(model)
        result.filter(filter)
        assert result.get_min() == result.get_max()
        assert math.isclose(result.get_min(), 1 / 6)

    def test_model_checking_prism_dd_dtmc(self):
        program = stormpy.parse_prism_program(get_example_path("dtmc", "die.pm"))
        formulas = stormpy.parse_properties('P=? [ F "one" ]', program)
        model = stormpy.build_symbolic_model(program, formulas)
        assert isinstance(model, stormpy.SymbolicDtmc[stormpy.DdType.Sylvan, float])
        assert model.nr_states == 13
        assert model.nr_transitions == 20
        result = stormpy.model_checking(model, formulas[0], engine=stormpy.Engine.DD)
        assert type(result) is stormpy.SymbolicQuantitativeCheckResult[stormpy.DdType.Sylvan, float]
        assert result.get_min() == 0.0
        assert result.get_max() == 1.0
        filter = stormpy.create_filter_initial_states(model)
        result.filter(filter)
        assert result.get_min() == result.get_max()
        assert math.isclose(result.get_min(), 1 / 6, rel_tol=1e-6)

    def test_model_checking_prism_hybrid_dtmc(self):
        program = stormpy.parse_prism_program(get_example_path("dtmc", "die.pm"))
        formulas = stormpy.parse_properties('P=? [ F "one" ]', program)
        model = stormpy.build_symbolic_model(program, formulas)
        assert isinstance(model, stormpy.SymbolicDtmc[stormpy.DdType.Sylvan, float])
        assert model.nr_states == 13
        assert model.nr_transitions == 20
        result = stormpy.model_checking(model, formulas[0], engine=stormpy.Engine.HYBRID)
        assert type(result) is stormpy.HybridQuantitativeCheckResult[stormpy.DdType.Sylvan, float]
        values = result.get_explicit_value_vector()
        assert len(values) == 3
        assert math.isclose(values[0], 1 / 6)
        filter = stormpy.create_filter_initial_states(model)
        result.filter(filter)
        assert result.get_min() == result.get_max()
        assert math.isclose(result.get_min(), 1 / 6, rel_tol=1e-6)

    def test_compute_expected_number_of_visits(self):
        program = stormpy.parse_prism_program(get_example_path("dtmc", "die.pm"))
        model = stormpy.build_model(program)
        environment = stormpy.Environment()
        result = stormpy.compute_expected_number_of_visits(model, environment=environment)
        assert result[0] == 1
        assert math.isclose(result[1], 2.0 / 3)

    def test_compute_steady_state_distribution(self):
        program = stormpy.parse_prism_program(get_example_path("dtmc", "die.pm"))
        model = stormpy.build_model(program)
        environment = stormpy.Environment()
        result = stormpy.compute_steady_state_distribution(model, environment=environment)
        values = result.get_finite_value_vector()
        assert len(values) == 13
        sorted(values)
        for i in range(7):
            assert values[i] == 0
        for i in range(7, 13):
            assert math.isclose(values[i], 1.0 / 6)
