import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from app import validate_age

def test_validate_age_accepts_65_inclusive():
    """
    Regression test for the bug where 65 is incorrectly rejected.
    The docstring states the range 18 to 65 is inclusive.
    """
    assert validate_age(65) is True