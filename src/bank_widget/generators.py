"""Содержит функции для работы с массивами транзакций"""

from typing import Any, Dict, List, Iterator

def filter_by_currency(transactions: List[Dict[str, Any]], currency: str = "USD") -> Iterator:
    """Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    for transaction in transactions:
        if transaction.get("operationAmount").get("currency").get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator:
    """Возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction["description"]
