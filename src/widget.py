from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(info: str) -> str:
    """ Маскирует номер карты или счета в зависимости от типа."""
    parts = info.split()
    if len(parts) < 2:
        raise ValueError("Invalid input format. Expected 'Type Number'.")

    number = parts[-1]
    masked_number = ""

    if number.isdigit():
        if len(number) in [15, 16]:
            masked_number = get_mask_card_number(int(number))
        elif len(number) > 16:
            masked_number = get_mask_account(int(number))
        else:
            raise ValueError("Invalid card or account number length.")
    else:
        raise ValueError("Invalid card or account number format.")

    return f"{' '.join(parts[:-1])} {masked_number}"


def get_date(date_str: str) -> str:
    """ Преобразует строку с датой из формата "YYYY-MM-DDTHH:MM:SS.mmmmmm" в формат "ДД.ММ.ГГГГ". """
    from datetime import datetime
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")
