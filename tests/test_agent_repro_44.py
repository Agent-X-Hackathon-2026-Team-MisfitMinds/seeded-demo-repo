import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from app import validate_age

def test_validate_age_none_returns_false():
    """
    Reproduce the issue: validate_age(None) raises TypeError.
    Expected: Returns False.
    """
    assert validate_age(None) is False

def test_validate_age_valid_cases():
    """
    Ensure existing functionality remains intact.
    """
    assert validate_age(30) is True
    assert validate_age(17) is False