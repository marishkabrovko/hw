from typing import List, Dict, Iterator


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """
    Фильтрует транзакции по указанной валюте.

    :param transactions: Список словарей с транзакциями.
    :param currency: Код валюты для фильтрации.
    :return: Итератор транзакций с указанной валютой.
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Генерирует описания транзакций.

    :param transactions: Список словарей с транзакциями.
    :return: Итератор описаний транзакций.
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генерирует номера банковских карт в указанном диапазоне.

    :param start: Начальное значение диапазона.
    :param stop: Конечное значение диапазона.
    :return: Итератор номеров карт в формате XXXX XXXX XXXX XXXX.
    """
    for number in range(start, stop + 1):
        yield f"{number:016d}"[:4] + " " + f"{number:016d}"[4:8] + " " + f"{number:016d}"[8:12] + " " + f"{number:016d}"[12:]
