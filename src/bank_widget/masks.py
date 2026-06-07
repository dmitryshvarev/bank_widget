"""Содержит функции маскировки номеров"""

import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(r"..\..\logs\masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Возвращает замаскированный номер карты"""
    if not isinstance(card_number, str):
        logger.error('Функция get_mask_card_number принимает один аргумент типа "str"')
        raise TypeError("Функция принимает один аргумент типа str")

    if len(card_number) < 12 or len(card_number) > 19:
        logger.error("Длина номера карты не верна")
        return card_number

    if not card_number.isdigit():
        logger.error("Номер карты должен состоять только из цифр")
        return card_number

    if len(card_number) > 12:
        logger.info("Маскируется номер карты")
        mask_stars = "*" * (len(card_number) - 12) + " "
    else:
        logger.info("Маскируется номер карты")
        mask_stars = ""

    mask_card_number = card_number[:4] + " " + card_number[4:6] + "** " + mask_stars + card_number[-4:]
    return mask_card_number


def get_mask_account(user_account: str) -> str:
    """Возвращает замаскированный номер счета"""
    if not isinstance(user_account, str):
        logger.error('Функция get_mask_account принимает один аргумент типа "str"')
        raise TypeError("Функция принимает один аргумент типа str")

    if (len(user_account) != 20) or (not user_account.isdigit()):
        logger.info(f"Номер счета {user_account} не подлежит маскировке")
        return user_account

    logger.info(f"Маскируется номер счета {user_account}")
    mask_account = "**" + user_account[-4:]
    return mask_account
