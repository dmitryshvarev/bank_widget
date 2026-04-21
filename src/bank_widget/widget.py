# Импортирование функций маскировки номеров карты и счета
from .masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: str) -> str:
    """Маскирует номер карты или счета"""
    if not isinstance(type_and_number, str):
        raise TypeError("Функция принимает один аргумент типа str")

    type_and_number_list = type_and_number.split()

    if type_and_number_list[0] == "Счет":
        mask_number_list = ["Счет", get_mask_account(type_and_number_list[1])]
    else:
        mask_number_list = type_and_number_list[:-1]
        mask_number_list.append(get_mask_card_number(type_and_number_list[-1]))

    return " ".join(mask_number_list)


def get_date(input_date: str) -> str:
    """Форматирует строку с датой"""
    if not isinstance(input_date, str):
        raise TypeError("Функция принимает один аргумент типа str")

    date_format_list = input_date[:10].split("-")

    for item in date_format_list:
        if not item.isdigit():
            return input_date

    date_format_list.reverse()

    return ".".join(date_format_list)
