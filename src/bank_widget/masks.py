"""Содержит функции маскировки номеров"""


def get_mask_card_number(card_number: str) -> str:
    """Возвращает замаскированный номер карты"""
    if not isinstance(card_number, str):
        raise TypeError("Функция принимает один аргумент типа str")

    if len(card_number) < 12 or len(card_number) > 19:
        return card_number

    if not card_number.isdigit():
        return card_number

    if len(card_number) > 12:
        mask_stars = "*" * (len(card_number) - 12) + " "
    else:
        mask_stars = ""

    mask_card_number = card_number[:4] + " " + card_number[4:6] + "** " + mask_stars + card_number[-4:]
    return mask_card_number


def get_mask_account(user_account: str) -> str:
    """Возвращает замаскированный номер счета"""
    if not isinstance(user_account, str):
        raise TypeError("Функция принимает один аргумент типа str")

    if (len(user_account) != 20) or (not user_account.isdigit()):
        return user_account

    mask_account = "**" + user_account[-4:]
    return mask_account
