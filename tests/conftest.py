import pytest

@pytest.fixture
def card_numbers():
    return [
        7000792289606361,
        1234567812345678,
        4000123412341234,
        5000
    ]

@pytest.fixture
def account_numbers():
    return [
        73654108430135874305,
        12345678901234567890,
        98765432109876543210,
        1234
    ]

@pytest.fixture
def transactions():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]
