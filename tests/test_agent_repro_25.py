import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from app import calculate_discount

def test_calculate_discount_above_100_percent_returns_zero():
    # Acceptance criteria: calculate_discount(100, 150) returns 0.
    assert calculate_discount(100, 150) == 0

def test_calculate_discount_at_100_percent_returns_zero():
    # Acceptance criteria: calculate_discount(100, 100) returns 0.
    assert calculate_discount(100, 100) == 0

def test_calculate_discount_below_100_percent_returns_correct_value():
    # Acceptance criteria: calculate_discount(100, 20) returns 80.
    assert calculate_discount(100, 20) == 80