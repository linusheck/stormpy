import stormpy

import stormpy.examples
import stormpy.examples.files


def example_analysis_01():
    path = stormpy.examples.files.prism_dtmc_die
    prism_program = stormpy.parse_prism_program(path)

    formula_str = "P=? [F s=7 & d=2]"
    properties = stormpy.parse_properties(formula_str, prism_program)
    model = stormpy.build_model(prism_program, properties)
    # Target states of the eventually formula
    target = properties[0].get_raw_formula().subformula.subformula
    psi_states = stormpy.model_checking(model, target).get_truth_values_vector()
    phi_states = stormpy.BitVector(model.nr_states, True)
    prob0, prob1 = stormpy.developer.perform_prob01(model, phi_states, psi_states)
    print(prob0)
    print(prob1)


if __name__ == "__main__":
    example_analysis_01()
