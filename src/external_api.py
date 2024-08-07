import os
import requests
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.exchangeratesapi.io/v1/latest"


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции из USD или EUR в рубли.
    Обращается к внешнему API для получения текущего курса валют.

    :param transaction: Словарь с данными о транзакции.
    :return: Сумма транзакции в рублях.
    """
    amount = transaction.get("amount", 0.0)
    currency = transaction.get("currency", "RUB")

    if currency == "RUB":
        return amount

    params = {
        "access_key": API_KEY,
        "symbols": "RUB",
        "base": currency
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()
    rates = data.get("rates", {})
    rub_rate = rates.get("RUB", 1.0)

    return amount * rub_rate
