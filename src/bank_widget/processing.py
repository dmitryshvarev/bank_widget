from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(data: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """Фильтрует список словарей по ключу `state`"""
    return [item for item in data if item.get('state') == state]


def sort_by_date(data: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """Сортирует список словарей по ключу `date`"""
    return sorted(
        data,
        key=lambda item: datetime.strptime(item['date'], '%Y-%m-%dT%H:%M:%S.%f'),
        reverse=descending
    )
