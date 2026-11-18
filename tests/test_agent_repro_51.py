import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from app import validate_age

def test_validate_age_includes_65():
    """
    Reproduce the bug where validate_age(65) returns False.
    The docstring states the range is 18 to 65 inclusive.
    """
    assert validate_age(65) is True