
import json
from idlelib.iomenu import encoding

from typing import Any, Dict, List


def load_transactions(path: str) -> List[Dict[str, Any]]:
    """Преобразует JSON-файл в объект Python с данными о финансовых транзакциях"""

    with open(path, "r", encoding="utf-8") as transactions_file:
        transactions_data = json.load(transactions_file)

    return transactions_data


if __name__ == '__main__':
    print(load_transactions(r'..\..\data\operations.json'))
