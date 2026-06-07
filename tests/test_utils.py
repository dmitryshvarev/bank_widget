from src.bank_widget.utils import amount_in_rub, load_transactions


def test_load_transactions(transaction_json):
    assert load_transactions(r"..\data\operations.json")[0] == transaction_json
    assert load_transactions("bad path") == []


def test_amount_in_rub(transaction_json):
    assert amount_in_rub(transaction_json) == 31957.58
