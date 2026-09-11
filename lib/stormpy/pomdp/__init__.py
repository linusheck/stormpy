from stormpy.info import _config

if not _config.STORM_WITH_POMDP:
    raise ImportError("No support for POMDPs was built in Storm.")

from . import _pomdp
from ._pomdp import *
from stormpy._template import TemplateClass, deduce_default as _deduce_default, deduce_from_first_argument as _deduce_from_first_argument
from stormpy.storage import SparseDtmc as _SparseDtmc, SparsePomdp as _SparsePomdp

BeliefSupportTracker = TemplateClass(
    "stormpy.pomdp.BeliefSupportTracker", _pomdp, parameters=("ValueType",), deduce=_deduce_from_first_argument(_SparsePomdp, keyword="pomdp")
)
SparseBeliefState = TemplateClass("stormpy.pomdp.SparseBeliefState", _pomdp, parameters=("ValueType",), deduce=_deduce_default(float))
NondeterministicBeliefTrackerSparseOptions = TemplateClass(
    "stormpy.pomdp.NondeterministicBeliefTrackerSparseOptions", _pomdp, parameters=("ValueType",), deduce=_deduce_default(float)
)
NondeterministicBeliefTrackerSparse = TemplateClass(
    "stormpy.pomdp.NondeterministicBeliefTrackerSparse", _pomdp, parameters=("ValueType",), deduce=_deduce_from_first_argument(_SparsePomdp, keyword="pomdp")
)
IterativeQualitativeSearchSolver = TemplateClass("stormpy.pomdp.IterativeQualitativeSearchSolver", _pomdp, parameters=("ValueType",))
BeliefSupportWinningRegionQueryInterface = TemplateClass(
    "stormpy.pomdp.BeliefSupportWinningRegionQueryInterface",
    _pomdp,
    parameters=("ValueType",),
    deduce=_deduce_from_first_argument(_SparsePomdp, keyword="pomdp"),
)
BeliefExplorationModelChecker = TemplateClass(
    "stormpy.pomdp.BeliefExplorationModelChecker", _pomdp, parameters=("ValueType",), deduce=_deduce_from_first_argument(_SparsePomdp, keyword="model")
)
BeliefMdpExplorer = TemplateClass("stormpy.pomdp.BeliefMdpExplorer", _pomdp, parameters=("ValueType",))
BeliefExplorationModelCheckerOptions = TemplateClass(
    "stormpy.pomdp.BeliefExplorationModelCheckerOptions", _pomdp, parameters=("ValueType",), deduce=_deduce_default(float)
)
BeliefExplorationPomdpModelCheckerResult = TemplateClass(
    "stormpy.pomdp.BeliefExplorationPomdpModelCheckerResult", _pomdp, parameters=("ValueType",), deduce=_deduce_default(float)
)
MonitorVerifier = TemplateClass(
    "stormpy.pomdp.MonitorVerifier", _pomdp, parameters=("ValueType",), deduce=_deduce_from_first_argument(_SparsePomdp, keyword="product")
)
GenerateMonitorVerifier = TemplateClass(
    "stormpy.pomdp.GenerateMonitorVerifier", _pomdp, parameters=("ValueType",), deduce=_deduce_from_first_argument(_SparseDtmc, keyword="mc")
)
GenerateMonitorVerifierOptions = TemplateClass("stormpy.pomdp.GenerateMonitorVerifierOptions", _pomdp, parameters=("ValueType",), deduce=_deduce_default(float))
ObservationTraceUnfolder = TemplateClass(
    "stormpy.pomdp.ObservationTraceUnfolder", _pomdp, parameters=("ValueType",), deduce=_deduce_from_first_argument(_SparsePomdp, keyword="model")
)


def make_canonic(model):
    """
    Make the POMDP canonic
    :param model:
    :return:
    """

    if model.supports_parameters:
        return _pomdp._make_canonic_Rf(model)
    elif model.is_exact:
        return _pomdp._make_canonic_Exact(model)
    else:
        return _pomdp._make_canonic_Double(model)


def make_simple(model, keep_state_valuations=False):
    """
    Make the POMDP simple (aka alternating), i.e., each state has at most two actions, and if there is nondeterminism, then there is no probabilistic branching,

    :param model:
    :return:
    """
    if model.supports_parameters:
        return _pomdp._make_simple_Rf(model, keep_state_valuations)
    else:
        return _pomdp._make_simple_Double(model, keep_state_valuations)


def unfold_memory(model, memory, add_memory_labels=False, keep_state_valuations=False):
    """
    Unfold the memory for an FSC into the POMDP

    :param model: A pomdp
    :param memory: A memory structure
    :return: A pomdp that contains states from the product of the original POMDP and the FSC Memory
    """
    if model.supports_parameters:
        return _pomdp._unfold_memory_Rf(model, memory, add_memory_labels, keep_state_valuations)
    else:
        return _pomdp._unfold_memory_Double(model, memory, add_memory_labels, keep_state_valuations)


def apply_unknown_fsc(model, mode):
    if model.supports_parameters:
        return _pomdp._apply_unknown_fsc_Rf(model, mode)
    else:
        return _pomdp._apply_unknown_fsc_Double(model, mode)


def create_nondeterminstic_belief_tracker(model, reduction_timeout, track_timeout):
    """

    :param model: A POMDP
    :param reduction_timeout: timeout in milliseconds for the reduction algorithm, 0 for no timeout.
    :return:
    """
    vt = _SparsePomdp.parameters_of(model)[0]
    opts = NondeterministicBeliefTrackerSparseOptions[vt]()
    opts.reduction_timeout = reduction_timeout
    opts.track_timeout = track_timeout
    return NondeterministicBeliefTrackerSparse[vt](model, opts)


def create_observation_trace_unfolder(model, risk_assessment, expr_manager, options=None):
    """

    :param model:
    :param risk_assessment:
    :param expr_manager:
    :param options:
    :return:
    """
    if options is None:
        options = ObservationTraceUnfolderOptions()

    return ObservationTraceUnfolder(model, risk_assessment, expr_manager, options)
