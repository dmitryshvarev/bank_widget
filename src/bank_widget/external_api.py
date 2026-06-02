
from typing import Any, Dict


def amount_in_rub(transaction: Dict[str, Any]) -> float:
    """Возвращает сумму транзакции в рублях"""

    amount = 0

    if transaction.get("operationAmount").get("currency").get("code") == "RUB":
        amount = transaction.get("operationAmount").get("amount")
    else:
        pass

    return amount