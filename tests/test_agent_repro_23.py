import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from app import calculate_discount


def test_calculate_discount_100_percent_is_zero():
    """
    Reproduce the bug where a 100% discount results in a negative price.
    Expected: 0
    Actual: -100
    """
    assert calculate_discount(price=100, discount_percent=100) == 0


def test_calculate_discount_over_100_percent_is_zero():
    """
    Ensure that discounts greater than 100% are also clamped to 0,
    preventing the customer from being paid.
    """
    assert calculate_discount(price=100, discount_percent=150) == 0