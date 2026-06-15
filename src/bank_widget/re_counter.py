"""Содержит функцию поиска с помощью регулярных выражений
и функцию для подсчета количества банковских операций определенного типа"""

import re
from typing import Dict, List, Union
from collections import Counter


def process_bank_search(transactions_data: List[Dict[str, Union[str, float]]], search: str) -> List[Dict[str, Union[str, float]]]:
    """Поиск данных в словаре с помощью регулярных выражений"""
    pattern = rf"{search}"

    found_transactions = [transaction for transaction in transactions_data if re.search(pattern, transaction.get("description", "Описание не найдено"), flags=re.IGNORECASE)]

    return found_transactions







