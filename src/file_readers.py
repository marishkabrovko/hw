from typing import Dict
from typing import List

import pandas as pd

CSV_FILE_PATH = "data/transactions.csv"
EXCEL_FILE_PATH = "data/transactions_excel.xlsx"


def read_transactions_from_csv(file_path: str = CSV_FILE_PATH) -> List[Dict[str, str]]:
    """
    Считывает финансовые операции из CSV-файла.

    Args:
        file_path (str): Путь к CSV-файлу.

    Returns:
        List[Dict[str, str]]: Список словарей с транзакциями.
    """
    try:
        df = pd.read_csv(file_path)
        return df.to_dict(orient="records")
    except (FileNotFoundError, pd.errors.EmptyDataError):
        return []


def read_transactions_from_excel(file_path: str = EXCEL_FILE_PATH) -> List[Dict[str, str]]:
    """
    Считывает финансовые операции из Excel-файла.

    Args:
        file_path (str): Путь к Excel-файлу.

    Returns:
        List[Dict[str, str]]: Список словарей с транзакциями.
    """
    try:
        df = pd.read_excel(file_path)
        return df.to_dict(orient="records")
    except (FileNotFoundError, ValueError):
        return []
