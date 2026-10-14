from pathlib import Path

from vacuum_tikz import export_vacuum_tikz

import stormpy
import stormpy.examples.files

# Load the vacuum cleaner MDP from the PRISM file.
program = stormpy.parse_prism_program(stormpy.examples.files.prism_mdp_vacuum)

# Build the MDP from the PRISM program with rational numbers.
options = stormpy.BuilderOptions(build_all_reward_models=True, build_all_labels=True)
options.set_build_state_valuations()
options.set_build_choice_labels()
mdp = stormpy.build_model[stormpy.numbers.Rational](program, options=options)

# Minimize expected time to docking and extract an optimal scheduler.
# In this MDP time counts transitions, including the initial start transition.
steps = stormpy.parse_properties('Tmin=? [ F "docked" ]', program)[0]
result = stormpy.model_checking(mdp, steps, extract_scheduler=True)
expected_steps = result[mdp.initial_states[0]]
print(f"Minimum expected time to docking: {expected_steps} ({float(expected_steps):.6f})")

# Apply the scheduler to the MDP to obtain a DTMC.
dtmc = mdp.apply_scheduler(result.get_scheduler())
fixed_steps = stormpy.parse_properties('T=? [ F "docked" ]', program)[0]
assert stormpy.model_checking(dtmc, fixed_steps)[dtmc.initial_states[0]] == expected_steps

# Sum visiting times by grid position, including states with different bump
# values. Exclude the initial setup state, but include absorbing locations.
variables = {name: program.expression_manager.get_variable(name) for name in ("x", "y", "started")}
width = program.get_constant("W").definition.evaluate_as_int() + 1
height = program.get_constant("H").definition.evaluate_as_int() + 1
grid = [[stormpy.numbers.Rational(0) for x in range(width)] for y in range(height)]
visits = stormpy.compute_expected_number_of_visits(dtmc)
values = dtmc.state_valuations
for state in dtmc.states:
    if not values.get_value(state.id, variables["started"]):
        continue
    x = values.get_value(state.id, variables["x"])
    y = values.get_value(state.id, variables["y"])
    time = visits[state.id]
    # Infinite visiting times are floats; finite sums remain exact.
    if time == float("inf") or grid[y][x] == float("inf"):
        grid[y][x] = float("inf")
    else:
        grid[y][x] += time

print("Expected visits by position (inf = absorbing location, 0 = never visited):")
print("      " + " ".join(f"x={x: <7}" for x in range(width)))
for y in reversed(range(height)):
    print(f"y={y}   " + " ".join(f"{float(time):9.3f}" for time in grid[y]))

# Compile with: pdflatex vacuum-visits.tex
output = Path("vacuum-visits.tex")
export_vacuum_tikz(output, grid, mdp, dtmc, result.get_scheduler(), visits, variables)
print(f"TikZ visualization written to {output}")
