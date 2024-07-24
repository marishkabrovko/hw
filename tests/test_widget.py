import pytest

from src.widget import get_date
from src.widget import mask_account_card


@pytest.mark.parametrize(
    "data, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("MasterCard 1234567812345678", "MasterCard 1234 56** **** 5678"),
    ],
)
def test_mask_account_card(data, expected):
    assert mask_account_card(data) == expected


@pytest.mark.parametrize(
    "date_str, expected", [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2019-12-31T23:59:59.999999", "31.12.2019")]
)
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected
