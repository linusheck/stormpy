"""Probabilistic models in sparse and decision diagram representations.

Sparse model classes are template families selected by value type, for example
``SparseDtmc[float]`` or ``SparseDtmc[stormpy.Rational]``. They can be built from
``SparseModelComponents`` containing a transition matrix and state labeling,
or obtained through ``stormpy.build_model``. Copy constructors deduce the value
type from the original model. Reward models store state, action and transition
rewards with the same value type as the model.

Symbolic model families additionally select the decision diagram backend, e.g.
``SymbolicDtmc[DdType.Sylvan, float]``. Use the common ``SparseModel`` or
``SymbolicModel`` families for type inspection across concrete model kinds.

The raw Storm bindings are available in :mod:`stormpy.developer.storage`."""

from stormpy.developer import storage as _bindings

ModelType = _bindings.ModelType
DdType = _bindings.DdType
SparseModel = _bindings.SparseModel.publish_as("stormpy.models.SparseModel")
SparseDtmc = _bindings.SparseDtmc.publish_as("stormpy.models.SparseDtmc")
SparseMdp = _bindings.SparseMdp.publish_as("stormpy.models.SparseMdp")
SparsePomdp = _bindings.SparsePomdp.publish_as("stormpy.models.SparsePomdp")
SparseCtmc = _bindings.SparseCtmc.publish_as("stormpy.models.SparseCtmc")
SparseMA = _bindings.SparseMA.publish_as("stormpy.models.SparseMA")
SparseSmg = _bindings.SparseSmg.publish_as("stormpy.models.SparseSmg")
SparseRewardModel = _bindings.SparseRewardModel.publish_as("stormpy.models.SparseRewardModel")
SparseModelComponents = _bindings.SparseModelComponents.publish_as("stormpy.models.SparseModelComponents")
SymbolicModel = _bindings.SymbolicModel.publish_as("stormpy.models.SymbolicModel")
SymbolicDtmc = _bindings.SymbolicDtmc.publish_as("stormpy.models.SymbolicDtmc")
SymbolicMdp = _bindings.SymbolicMdp.publish_as("stormpy.models.SymbolicMdp")
SymbolicCtmc = _bindings.SymbolicCtmc.publish_as("stormpy.models.SymbolicCtmc")
SymbolicMA = _bindings.SymbolicMA.publish_as("stormpy.models.SymbolicMA")
SymbolicRewardModel = _bindings.SymbolicRewardModel.publish_as("stormpy.models.SymbolicRewardModel")

__all__ = [
    "ModelType",
    "DdType",
    "SparseModel",
    "SparseDtmc",
    "SparseMdp",
    "SparsePomdp",
    "SparseCtmc",
    "SparseMA",
    "SparseSmg",
    "SparseRewardModel",
    "SparseModelComponents",
    "SymbolicModel",
    "SymbolicDtmc",
    "SymbolicMdp",
    "SymbolicCtmc",
    "SymbolicMA",
    "SymbolicRewardModel",
]

from . import _convenience
