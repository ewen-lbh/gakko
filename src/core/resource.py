import json
import os

from src.core.consts import BASE_DIR


def get(file: str) -> dict:
    with open(path(file), 'r') as f:
        return json.loads(f.read())


def write(file: str, data: dict):
    with open(path(file), 'w', encoding='utf8') as f:
        f.write(json.dumps(data, indent=4, ensure_ascii=False))


def path(file: str) -> str:
    if not file.endswith('.json'):
        file = file + '.json'
    return os.path.join(BASE_DIR, 'data', file)
