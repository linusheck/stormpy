"""Python conveniences on the public classes; native methods retain Storm's names.

Public and developer classes share their native type, so these conveniences also
work on objects returned by the native engines.
"""

from stormpy.developer import storage
from stormpy._template import _TemplateClass

_ALIASES = {
    "SparseModel": {"labels_state": "get_labels_of_state"},
    "SparseRewardModel": {"get_zero_reward_states": "get_states_with_zero_reward"},
    "SparseCtmc": {"probability_matrix": "compute_probability_matrix"},
}

for _name, _aliases in _ALIASES.items():
    _family = getattr(storage, _name)
    _classes = _family.instantiations.values() if isinstance(_family, _TemplateClass) else (_family,)
    for _class in _classes:
        for _alias, _method in _aliases.items():
            setattr(_class, _alias, getattr(_class, _method))
