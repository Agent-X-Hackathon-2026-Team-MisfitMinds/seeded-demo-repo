import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from app import validate_age


def test_validate_age_includes_65():
    """
    The docstring states the valid range is 18 to 65 inclusive.
    validate_age(65) should return True.
    """
    assert validate_age(65) is True