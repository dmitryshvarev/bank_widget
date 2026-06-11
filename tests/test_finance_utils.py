import pandas as pd
from unittest.mock import patch

from src.bank_widget.finance_utils import load_transactions_from_csv, load_transactions_from_excel


@patch('pandas.read_excel')
def test_load_transactions_from_excel_success(mock_read_excel):
    expected_data = pd.DataFrame({
        'id': [650703.0, 3598919.0],
        'date': ['2023-09-05T11:30:32Z', '2020-12-06T23:00:58Z'],
        'description': ['Перевод организации', 'Перевод с карты на карту']
    })
    mock_read_excel.return_value = expected_data

    result = load_transactions_from_excel('dummy_path.xlsx')
    assert result == expected_data.to_dict(orient='records')
    mock_read_excel.assert_called_once_with('dummy_path.xlsx')


@patch('pandas.read_csv')
def test_load_transactions_from_csv_success(mock_read_csv):
    expected_data = pd.DataFrame({
        'id': [650703.0, 3598919.0],
        'date': ['2023-09-05T11:30:32Z', '2020-12-06T23:00:58Z'],
        'description': ['Перевод организации', 'Перевод с карты на карту']
    })
    mock_read_csv.return_value = expected_data

    result = load_transactions_from_csv('dummy_path.csv')
    assert result == expected_data.to_dict(orient='records')
    mock_read_csv.assert_called_once_with('dummy_path.csv', delimiter=';')
