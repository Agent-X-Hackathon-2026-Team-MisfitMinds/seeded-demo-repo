import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from app import validate_age


def test_validate_age_repro_18_year_old():
    """
    Reproduce the bug where validate_age(18) returns False.
    The requirement is that 18 is inclusive, so it should return True.
    """
    assert validate_age(18) is True


def test_validate_age_repro_65_year_old():
    """
    Verify the upper bound of the range (65 inclusive).
    """
    assert validate_age(65) is True