import json
import logging
import os
from typing import Any, Dict, List

from src.bank_widget.external_api import get_exchange_rate


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(r'..\..\logs\utils.log', mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def load_transactions(path: str) -> List[Dict[str, Any]]:
    """Преобразует JSON-файл в объект Python с данными о финансовых транзакциях"""

    transactions_data = []

    try:
        with open(path, "r", encoding="utf-8") as transactions_file:
            logger.info(f'Файл "{path}" успешно загружен')
            try:
                transactions_data = json.load(transactions_file)
                logger.info(f'Данные из файла "{path}" преобразованы в объект Python')
            except json.JSONDecodeError:
                logger.error(f'Ошибка декодирования файла "{path}"')
                return transactions_data
    except FileNotFoundError:
        logger.error(f'Файл "{path}" не найден')
        return transactions_data

    return transactions_data


def amount_in_rub(transaction: Dict[str, Any]) -> float:
    """Возвращает сумму транзакции в рублях"""

    amount = 0

    currency_code = transaction.get("operationAmount").get("currency").get("code")
    if currency_code:
        logger.info('Получаем данные о сумме транзакции')
        if currency_code == "RUB":
            logger.info('Данная транзакция в рублях')
            amount = float(transaction.get("operationAmount").get("amount"))
        else:
            logger.info('Данная транзакция не в рублях. Происходит обращение к API')
            exchange_rate = get_exchange_rate()["Valute"][currency_code]["Value"]
            amount = round(float(transaction.get("operationAmount").get("amount")) * exchange_rate, 2)
    else:
        logger.error('Неверные данные о транзакции')

    return amount
