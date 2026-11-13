import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from app import validate_age

def test_validate_age_accepts_65_inclusive():
    """
    The docstring states that validate_age should return True for ages 
    between 18 and 65 inclusive. This test verifies that 65 is accepted.
    """
    assert validate_age(65) is True