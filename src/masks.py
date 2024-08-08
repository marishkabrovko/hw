import logging
import os

# Создание и настройка логера
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи логов в файл
log_file_path = os.path.join("logs", "masks.log")
file_handler = logging.FileHandler(log_file_path, mode="w")

# Форматирование логов
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Добавление обработчика к логеру
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    card_number_str = str(card_number)
    if len(card_number_str) < 16:
        return card_number_str
    return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"


def get_mask_account(account_number: int) -> str:
    account_number_str = str(account_number)
    if len(account_number_str) <= 4:
        return account_number_str
    return f"**{account_number_str[-4:]}"


def mask_sensitive_info(data: str) -> str:
    try:
        logger.debug(f"Начало обработки данных: {data}")
        # Логика обработки
        masked_data = data.replace("sensitive", "[MASKED]")
        logger.info(f"Обработанные данные: {masked_data}")
        return masked_data
    except Exception as e:
        logger.error(f"Ошибка при обработке данных: {str(e)}")
        raise e
