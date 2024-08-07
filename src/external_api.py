import os
import requests
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/convert"


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

    headers = {
        "apikey": API_KEY
    }
    params = {
        "from": currency,
        "to": "RUB",
        "amount": amount
    }

    response = requests.get(BASE_URL, headers=headers, params=params)
    data = response.json()
    result = data.get("result", 0.0)

    return result
