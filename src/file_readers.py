import csv
import pandas as pd
from typing import List, Dict


def read_transactions_from_csv(file_path: str) -> List[Dict[str, str]]:
    """Считывает транзакции из CSV-файла."""
    transactions: List[Dict[str, str]] = []
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            transactions = [dict(row) for row in reader]
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return transactions


def read_transactions_from_excel(file_path: str) -> List[Dict[str, str]]:
    """Считывает транзакции из Excel-файла."""
    transactions: List[Dict[str, str]] = []
    try:
        df = pd.read_excel(file_path)
        transactions = df.to_dict(orient='records')
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        transactions = []
    return transactions
