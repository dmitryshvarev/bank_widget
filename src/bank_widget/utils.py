
import json

from typing import Any, Dict, List


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
