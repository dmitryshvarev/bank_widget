from src.bank_widget.re_counter import process_bank_search, process_bank_operations


def test_process_bank_search(transactions_):
    assert process_bank_search(transactions_, "С КАРТЫ") == [{
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        }]

    assert process_bank_search(transactions_, "none") == []


def test_process_bank_operations(transactions_):
    assert process_bank_operations(transactions_, ["Перевод организации", "Перевод с карты на карту"]) == {'Перевод организации': 2, 'Перевод с карты на карту': 1}
    assert process_bank_operations(transactions_, ["Перевод с карты на счет"]) == {}
