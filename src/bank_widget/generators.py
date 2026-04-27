"""Содержит функции для работы с массивами транзакций"""

from typing import Any, Dict, List, Iterator

def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Iterator:
    """Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction
