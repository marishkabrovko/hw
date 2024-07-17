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
