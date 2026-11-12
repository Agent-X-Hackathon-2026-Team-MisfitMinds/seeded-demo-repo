import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from app import calculate_discount


def test_calculate_discount_ten_percent():
    assert calculate_discount(100, 10) == 90