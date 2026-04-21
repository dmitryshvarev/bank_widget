from src.bank_widget.processing import filter_by_state, sort_by_date


def test_filter_by_state(user_data):
    assert filter_by_state(user_data) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]

    assert filter_by_state(user_data, state="CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_wisout_state(user_data_wisout_state):
    assert filter_by_state(user_data_wisout_state) == []


def test_sort_by_date(user_data, sort_user_data):
    assert sort_by_date(user_data) == sort_user_data

    assert sort_by_date(user_data, descending=False) == sort_user_data[::-1]
