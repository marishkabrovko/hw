from typing import Dict
from typing import List
from typing import Optional


def filter_by_state(data: List[Dict], state: Optional[str] = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param data: Список словарей.
    :param state: Значение ключа 'state', по которому производится фильтрация.
    :return: Отфильтрованный список словарей.
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по дате.

    :param data: Список словарей.
    :param descending: Порядок сортировки. По умолчанию True (убывание).
    :return: Отсортированный список словарей.
    """
    return sorted(data, key=lambda x: x.get("date", ""), reverse=descending)
