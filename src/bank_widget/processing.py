from typing import Any, Dict, List


def filter_by_state(data: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """Фильтрует список словарей по ключу `state`"""
    return [item for item in data if item.get('state') == state]
