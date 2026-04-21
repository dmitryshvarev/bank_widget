import pytest

from src.bank_widget.masks import get_mask_account, get_mask_card_number


def test_get_mask_standard_card_number(standard_card_number):
    assert get_mask_card_number(standard_card_number) == "7000 79** **** 6361"


@pytest.mark.parametrize(
    "card_number, mask_card_number",
    [
        ("700079226361", "7000 79** 6361"),
        ("7000790002289606361", "7000 79** ******* 6361"),
        ("zero792289606361", "zero792289606361"),
        ("7", "7"),
        ("70007900002289606361", "70007900002289606361"),
        ("", ""),
    ],
)
def test_get_mask_card_number(card_number, mask_card_number):
    assert get_mask_card_number(card_number) == mask_card_number


def test_get_mask_card_number_invalid_type():
    with pytest.raises(TypeError) as exc_info:
        get_mask_card_number(7000792289606361)
    assert str(exc_info.value) == "Функция принимает один аргумент типа str"


def test_get_mask_standard_user_account(standard_user_account):
    assert get_mask_account(standard_user_account) == "**4305"


@pytest.mark.parametrize(
    "user_account, mask_account",
    [
        ("730135874305", "730135874305"),
        ("736541084301358743050", "736541084301358743050"),
        ("zero4108430135874305", "zero4108430135874305"),
        ("", ""),
    ],
)
def test_get_mask_account(user_account, mask_account):
    assert get_mask_account(user_account) == mask_account


def test_get_mask_account_invalid_type():
    with pytest.raises(TypeError) as exc_info:
        get_mask_account([])
    assert str(exc_info.value) == "Функция принимает один аргумент типа str"
