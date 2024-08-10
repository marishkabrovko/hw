from unittest.mock import mock_open
from unittest.mock import patch

import pandas as pd
import pytest

from src.file_readers import read_transactions_from_csv
from src.file_readers import read_transactions_from_excel

# Пример данных, которые будут возвращены при чтении CSV
mock_csv_data = """date,amount,category
2023-08-01,1000,groceries
2023-08-02,2000,entertainment
"""

# Пример данных, которые будут возвращены при чтении Excel
mock_excel_data = pd.DataFrame(
    {"date": ["2023-08-01", "2023-08-02"], "amount": [1000, 2000], "category": ["groceries", "entertainment"]}
)


# Тест для функции считывания данных из CSV
@patch("builtins.open", new_callable=mock_open, read_data=mock_csv_data)
@patch("csv.DictReader")
def test_read_transactions_from_csv(mock_dict_reader, mock_file):
    mock_dict_reader.return_value = [
        {"date": "2023-08-01", "amount": "1000", "category": "groceries"},
        {"date": "2023-08-02", "amount": "2000", "category": "entertainment"},
    ]

    transactions = read_transactions_from_csv("data/transactions.csv")

    assert len(transactions) == 2, "Должны быть считаны две транзакции"
    assert transactions[0]["date"] == "2023-08-01", "Дата первой транзакции должна совпадать"
    assert transactions[0]["amount"] == 1000.0, "Сумма первой транзакции должна быть 1000"
    assert transactions[0]["category"] == "groceries", "Категория первой транзакции должна быть 'groceries'"


# Тест для функции считывания данных из Excel
@patch("pandas.read_excel")
def test_read_transactions_from_excel(mock_read_excel):
    mock_read_excel.return_value = mock_excel_data

    transactions = read_transactions_from_excel("data/transactions_excel.xlsx")

    assert len(transactions) == 2, "Должны быть считаны две транзакции"
    assert transactions[1]["date"] == "2023-08-02", "Дата второй транзакции должна совпадать"
    assert transactions[1]["amount"] == 2000.0, "Сумма второй транзакции должна быть 2000"
    assert transactions[1]["category"] == "entertainment", "Категория второй транзакции должна быть 'entertainment'"
