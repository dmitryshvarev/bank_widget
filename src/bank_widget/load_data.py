"""Содержит функции для считывания финансовых операций из табличных данных"""

import pandas as pd
from typing import Dict, List, Union


def load_transactions_from_csv(path_to_csv: str) -> List[Dict[str, Union[str, float]]]:
    """Считывает данные о финансовых операциях из CSV"""
    transactions_df = pd.read_csv(path_to_csv, delimiter=';')
    return transactions_df.to_dict(orient='records')


def load_transactions_from_excel(path_to_excel: str) -> List[Dict[str, Union[str, float]]]:
    """Считывает данные о финансовых операциях из Excel"""
    transactions_df = pd.read_excel(path_to_excel)
    return transactions_df.to_dict(orient='records')
