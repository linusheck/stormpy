import stormpy
import stormpy.examples.files
from stormpy.numbers import Rational


program = stormpy.parse_prism_program(
    'vacuum.prism')
mdp = stormpy.build_model[Rational](program)
prop = stormpy.parse_properties(
    'Tmin=? [ F "docked" ]', program)[0]
result = stormpy.model_checking(
    mdp, prop, extract_scheduler=True)  # 39.308
dtmc = mdp.apply_scheduler(result.get_scheduler())
visits = stormpy.compute_expected_number_of_visits(dtmc)
rug_visits = sum(visits[s.id] for s in dtmc.states
                 if "rug" in s.labels)  # 12.084
imdp = stormpy.add_uncertainty(mdp, Rational("1/100"))
mode = stormpy.UncertaintyResolutionMode.ROBUST
interval_result = stormpy.model_checking(imdp, prop,
    uncertainty_resolution_mode=mode) #

print(f"Minimal expected time to dock: {float(result[mdp.initial_states[0]]):.6f}")
print(f"Expected number of visits to the rug: {float(rug_visits):.6f}")
print(f"Interval result: {float(interval_result[imdp.initial_states[0]]):.6f}")
