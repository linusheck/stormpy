import stormpy
from helpers.helper import get_example_path


class TestEnvironment:
    def test_environment(self):
        env = stormpy.Environment()

    def test_environment_from_settings(self):
        default_method = stormpy.Environment().solver().min_max().method
        assert default_method != stormpy.MinMaxMethod.POLICY_ITERATION
        stormpy.developer.set_from_exploded_string(["--minmax:method", "pi"])
        env = stormpy.developer.EnvironmentBuilder.build_environment()
        assert isinstance(env, stormpy.Environment)
        assert env.solver().min_max().method == stormpy.MinMaxMethod.POLICY_ITERATION
        # Environments created directly do not depend on the settings
        assert stormpy.Environment().solver().min_max().method == default_method

    def test_exploration_environment(self):
        env = stormpy.Environment()
        exploration = env.exploration()
        exploration.precomputation_type = stormpy.PrecomputationType.LOCAL
        assert env.exploration().precomputation_type == stormpy.PrecomputationType.LOCAL
        exploration.next_state_heuristic = stormpy.NextStateHeuristic.UNIFORM
        assert env.exploration().next_state_heuristic == stormpy.NextStateHeuristic.UNIFORM
        exploration.steps_until_precomputation = 42
        assert env.exploration().steps_until_precomputation == 42
        exploration.precision = 1e-4
        assert env.exploration().precision == 1e-4
        exploration.sampled_paths_until_precomputation = 7
        assert env.exploration().sampled_paths_until_precomputation == 7
        exploration.sampled_paths_until_precomputation = None
        assert env.exploration().sampled_paths_until_precomputation is None
