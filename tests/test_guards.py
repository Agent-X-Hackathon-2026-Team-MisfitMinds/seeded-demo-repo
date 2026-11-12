"""Guard tests: behaviour every change to the shop utilities must keep.

They compare results with each other or check values well away from the
edges, so they hold for any correct implementation and break when a change
only handles one special case.
"""

import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from app import calculate_discount, get_user_profile, validate_age


# calculate_discount: the result must move with price and percentage.

@pytest.mark.parametrize("percent, step", [(10, 90), (20, 80), (25, 75), (50, 50)])
@pytest.mark.parametrize("price", [100, 200])
def test_each_extra_100_of_price_adds_the_undiscounted_share(price, percent, step):
    difference = calculate_discount(price + 100, percent) - calculate_discount(price, percent)
    assert difference == pytest.approx(step)


@pytest.mark.parametrize("price", [80, 200, 1000])
def test_going_from_25_to_50_percent_takes_off_a_quarter_of_the_price(price):
    difference = calculate_discount(price, 25) - calculate_discount(price, 50)
    assert difference == pytest.approx(price * 0.25)


def test_discount_works_for_prices_with_cents():
    difference = calculate_discount(10.30, 50) - calculate_discount(0.10, 50)
    assert difference == pytest.approx(5.10)


# validate_age: ages clearly inside or outside the range.

@pytest.mark.parametrize("age", [19, 25, 40, 64])
def test_validate_age_accepts_ages_inside_range(age):
    assert validate_age(age) is True


@pytest.mark.parametrize("age", [-1, 0, 10, 17, 66, 80, 120])
def test_validate_age_rejects_ages_outside_range(age):
    assert validate_age(age) is False


# get_user_profile: a known user keeps the same shape on every call.

def test_known_profile_has_exactly_name_and_id():
    assert set(get_user_profile(1)) == {"name", "id"}


def test_known_profile_is_not_shared_between_calls():
    first = get_user_profile(1)
    first["name"] = "changed"
    assert get_user_profile(1) == {"name": "Alice", "id": 1}
