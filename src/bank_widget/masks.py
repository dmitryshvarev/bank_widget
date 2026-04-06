"""Содержит функции маскировки номеров"""


def get_mask_card_number(card_number: str) -> str:
    """Возвращает замаскированный номер карты"""
    mask_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    return mask_card_number


def get_mask_account(user_account: str) -> str:
    """Возвращает замаскированный номер счета"""
    mask_account = "**" + user_account[-4:]
    return mask_account
