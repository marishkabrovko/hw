import re
from collections import Counter
from typing import Dict
from typing import List


def search_transactions_by_description(transactions: List[Dict], search_str: str) -> List[Dict]:
    """
    Ищет транзакции по описанию с использованием регулярных выражений.

    :param transactions: список словарей с транзакциями.
    :param search_str: строка для поиска в описании.
    :return: список транзакций, содержащих поисковую строку в описании.
    """
    pattern = re.compile(re.escape(search_str), re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction.get("description", ""))]


def count_transactions_by_category(transactions: List[Dict[str, str]], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество транзакций по категориям.

    :param transactions: список словарей с транзакциями.
    :param categories: список категорий для подсчета.
    :return: словарь с количеством транзакций по категориям.
    """
    counter: Counter[str] = Counter()
    for transaction in transactions:
        description = transaction.get("description", "")
        for category in categories:
            if category.lower() in description.lower():
                counter[category] += 1
    return dict(counter)
