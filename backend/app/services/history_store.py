from collections import defaultdict

_history: dict[str, list[dict]] = defaultdict(list)


def add(user_id: str, item: dict) -> None:
    _history[user_id].append(item)


def get(user_id: str) -> list[dict]:
    return _history[user_id]
