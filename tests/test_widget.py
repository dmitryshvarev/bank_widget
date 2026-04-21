import pytest
from src.bank_widget.widget import mask_account_card, get_date


@pytest.mark.parametrize("card_account, mask_card_account", [("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
                                                             ("Счет 73654108430135874305", "Счет **4305"),
                                                             ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
                                                             ("Счет 64686473678894779589", "Счет **9589"),
                                                             ("64686473678894779589", "64686473678894779589"),
                                                             ("MasterCard7158300734726758", "MasterCard7158300734726758")
                                                             ])
def test_mask_account_card(card_account, mask_card_account):
    assert mask_account_card(card_account) == mask_card_account


def test_mask_account_card_invalid_type():
    with pytest.raises(TypeError) as exc_info:
        mask_account_card([7000792289606361])
    assert str(exc_info.value) == "Функция принимает один аргумент типа str"


@pytest.mark.parametrize("date, date_format", [("2024-03-11T02:26:18.671407", "11.03.2024"),
                                               ("2024-03-11", "11.03.2024"),
                                               ("T02:26:18.671407", "T02:26:18.671407"),
                                               ("", "")
                                               ])
def test_get_date(date, date_format):
    assert get_date(date) == date_format


def test_get_date_invalid_type():
    with pytest.raises(TypeError) as exc_info:
        get_date(("2024", "03", "11"))
    assert str(exc_info.value) == "Функция принимает один аргумент типа str"
