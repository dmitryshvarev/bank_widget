# Импортирование модуля с функциями маскировки номеров карты и счета
import masks


def mask_account_card(type_and_number: str) -> str:
    """Маскирует номер карты или счета"""
    type_and_number_list = type_and_number.split()

    if type_and_number_list[0] == "Счет":
        mask_number_list = ["Счет", masks.get_mask_account(type_and_number_list[1])]
    else:
        mask_number_list = type_and_number_list[:-1]
        mask_number_list.append(masks.get_mask_card_number(type_and_number_list[-1]))

    return " ".join(mask_number_list)


def get_date(input_date: str) -> str:
    """Форматирует строку с датой"""
    date_format_list = input_date[:10].split("-")
    date_format_list.reverse()

    return ".".join(date_format_list)
