from src.masks import get_mask_account
from src.masks import get_mask_card_number
from src.widget import get_date
from src.widget import mask_account_card

if __name__ == "__main__":
    card_number = 7000792289606361
    account_number = 73654108430135874305

    print(f"Маскированный номер карты: {get_mask_card_number(card_number)}")
    print(f"Маскированный номер счета: {get_mask_account(account_number)}")

    info_card = "Visa Platinum 7000792289606361"
    info_account = "Счет 73654108430135874305"

    print(f"Маскированный номер карты: {mask_account_card(info_card)}")
    print(f"Маскированный номер счета: {mask_account_card(info_account)}")

    date_str = "2024-03-11T02:26:18.671407"
    print(f"Форматированная дата: {get_date(date_str)}")
