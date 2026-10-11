"""DFT-specific tests for the public DFT API (stormpy.dft).

Generic checks of all public APIs (names exist, documentation) are in tests/test_public_apis.py.
"""

import stormpy
from configurations import dft


@dft
class TestPublicDftApi:
    def test_internal_imports_not_public(self):
        import stormpy.dft

        for name in ["Iterable", "Property", "RationalFunction", "SparseCtmc", "SparseMA", "StormError", "StormWarning"]:
            assert name not in stormpy.dft.__all__
