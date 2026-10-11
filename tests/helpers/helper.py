import os
import stormpy
import stormpy.examples
import stormpy.examples.files

example_dir = stormpy.examples.files.testfile_dir


def get_example_path(*paths):
    return os.path.join(example_dir, *paths)


def build_sparse_model(path, value_type):
    program = stormpy.parse_prism_program(path)
    if value_type in (stormpy.numbers.Rational, stormpy.numbers.RationalInterval):
        model = stormpy.build_model[stormpy.numbers.Rational](program)
    elif value_type is stormpy.numbers.RationalFunction:
        model = stormpy.build_model[stormpy.numbers.RationalFunction](program)
    else:
        model = stormpy.build_model(program)
    # The following are hardcoded interval values for testing purposes
    if value_type is stormpy.numbers.Interval:
        model = stormpy.add_uncertainty(model, 0.01)
    elif value_type is stormpy.numbers.RationalInterval:
        model = stormpy.add_uncertainty(model, stormpy.numbers.Rational("1/100"))
    return model
