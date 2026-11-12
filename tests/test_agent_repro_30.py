import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from app import validate_age

def test_validate_age_none_returns_false():
    """
    Acceptance criteria:
    - validate_age(None) returns False without raising.
    - validate_age(30) still returns True.
    - validate_age(17) still returns False.
    """
    assert validate_age(None) is False
    assert validate_age(30) is True
    assert validate_age(17) is False