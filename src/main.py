from src.masks import get_mask_card_number, get_mask_account

if __name__ == "__main__":
    card_number = 7000792289606361
    account_number = 73654108430135874305

    print(f"Маскированный номер карты: {get_mask_card_number(card_number)}")
    print(f"Маскированный номер счета: {get_mask_account(account_number)}")