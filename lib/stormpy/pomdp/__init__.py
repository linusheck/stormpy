from . import pomdp
from .pomdp import *

def make_canonic(model):
    """
    Make the POMDP canonic
    :param model:
    :return:
    """

    if model.supports_parameters:
        return pomdp._make_canonic_Rf(model)
    else:
        return pomdp._make_canonic_Double(model)

def make_simple(model):
    """
    Make the POMDP simple (aka alternating), i.e., each state has at most two actions, and if there is nondeterminism, then there is no probabilistic branching,

    :param model:
    :return:
    """
    if model.supports_parameters:
        return pomdp._make_simple_Rf(model)
    else:
        return pomdp._make_simple_Double(model)

def unfold_memory(model, memory, add_memory_labels=False):
    """
    Unfold the memory for an FSC into the POMDP

    :param model: A pomdp
    :param memory: A memory structure
    :return: A pomdp that contains states from the product of the original POMDP and the FSC Memory
    """
    if model.supports_parameters:
        return pomdp._unfold_memory_Rf(model, memory, add_memory_labels)
    else:
        return pomdp._unfold_memory_Double(model, memory, add_memory_labels)

def apply_unknown_fsc(model, mode):
    if model.supports_parameters:
        return pomdp._apply_unknown_fsc_Rf(model, mode)
    else:
        return pomdp._apply_unknown_fsc_Double(model, mode)