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


def card_number_generator(begin: int, end: int) -> Iterator:
    """Генерирует номера карт в заданном диапазоне"""
    return (f"{num:016}"[:4] + ' ' + f"{num:016}"[4:8] + ' ' + f"{num:016}"[8:12] + ' ' + f"{num:016}"[12:]
            for num in range(begin, end+1)
            if begin > 0 and end < 10**16 and begin <= end)
