import json
from typing import Any, Dict, List

from .external_api import get_exchange_rate


def load_transactions(path: str) -> List[Dict[str, Any]]:
    """Преобразует JSON-файл в объект Python с данными о финансовых транзакциях"""

    transactions_data = []

    try:
        with open(path, "r", encoding="utf-8") as transactions_file:
            try:
                transactions_data = json.load(transactions_file)
            except json.JSONDecodeError:
                print("Ошибка декодирования файла")
                return transactions_data
    except FileNotFoundError:
        print("Файл не найден")
        return transactions_data

    return transactions_data


def amount_in_rub(transaction: Dict[str, Any]) -> float:
    """Возвращает сумму транзакции в рублях"""

    amount = 0

    currency_code = transaction.get("operationAmount").get("currency").get("code")

    if currency_code == "RUB":
        amount = float(transaction.get("operationAmount").get("amount"))
    else:
        exchange_rate = get_exchange_rate()["Valute"][currency_code]["Value"]
        amount = round(float(transaction.get("operationAmount").get("amount")) * exchange_rate, 2)

    return amount
