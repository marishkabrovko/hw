import json
import logging
import os
from typing import Any
from typing import Dict
from typing import List

# Создание и настройка логера
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи логов в файл
log_file_path = os.path.join("logs", "utils.log")
file_handler = logging.FileHandler(log_file_path, mode="w")

# Форматирование логов
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Добавление обработчика к логеру
logger.addHandler(file_handler)


def read_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, возвращается пустой список.

    :param file_path: Путь к JSON-файлу.
    :return: Список словарей с данными о финансовых транзакциях.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    return []


def read_json(file_path: str) -> List[Dict[str, Any]]:
    try:
        logger.debug(f"Чтение файла: {file_path}")
        if not os.path.exists(file_path):
            logger.error(f"Файл не найден: {file_path}")
            return []

        with open(file_path, "r") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(f"Файл успешно прочитан: {file_path}")
                return data
            else:
                logger.error(f"Неправильный формат данных в файле: {file_path}")
                return []
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON: {str(e)}")
        return []
    except Exception as e:
        logger.error(f"Произошла ошибка при чтении файла: {str(e)}")
        return []
