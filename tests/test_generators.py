import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]


def test_filter_by_currency(sample_transactions):
    usd_transactions = filter_by_currency(sample_transactions, "USD")
    assert next(usd_transactions)["operationAmount"]["currency"]["code"] == "USD"
    assert next(usd_transactions)["operationAmount"]["currency"]["code"] == "USD"
    assert next(usd_transactions)["operationAmount"]["currency"]["code"] == "USD"
    with pytest.raises(StopIteration):
        next(usd_transactions)

    rub_transactions = filter_by_currency(sample_transactions, "RUB")
    assert next(rub_transactions)["operationAmount"]["currency"]["code"] == "RUB"
    assert next(rub_transactions)["operationAmount"]["currency"]["code"] == "RUB"
    with pytest.raises(StopIteration):
        next(rub_transactions)

    empty_transactions = filter_by_currency(sample_transactions, "EUR")
    with pytest.raises(StopIteration):
        next(empty_transactions)


def test_transaction_descriptions(sample_transactions):
    descriptions = transaction_descriptions(sample_transactions)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод организации"
    with pytest.raises(StopIteration):
        next(descriptions)


def test_card_number_generator():
    card_numbers = card_number_generator(1, 5)
    assert next(card_numbers) == "0000 0000 0000 0001"
    assert next(card_numbers) == "0000 0000 0000 0002"
    assert next(card_numbers) == "0000 0000 0000 0003"
    assert next(card_numbers) == "0000 0000 0000 0004"
    assert next(card_numbers) == "0000 0000 0000 0005"
    with pytest.raises(StopIteration):
        next(card_numbers)

    card_numbers_large_range = card_number_generator(9999999999999995, 9999999999999999)
    assert next(card_numbers_large_range) == "9999 9999 9999 9995"
    assert next(card_numbers_large_range) == "9999 9999 9999 9996"
    assert next(card_numbers_large_range) == "9999 9999 9999 9997"
    assert next(card_numbers_large_range) == "9999 9999 9999 9998"
    assert next(card_numbers_large_range) == "9999 9999 9999 9999"
    with pytest.raises(StopIteration):
        next(card_numbers_large_range)
