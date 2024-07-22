from typing import Dict
from typing import Iterator
from typing import List


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """ Фильтрует транзакции по указанной валюте."""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """ Генерирует описания транзакций. """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """ Генерирует номера банковских карт в указанном диапазоне. """
    for number in range(start, stop + 1):
        yield f"{number:016d}"[:4] + " " + f"{number:016d}"[4:8] + " " + f"{number:016d}"[8:12] + " " + f"{number:016d}"[12:]
