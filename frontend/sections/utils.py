import requests
import json
from .config import API_URL

MEDALS = {
    0: '🥇',
    1: '🥈',
    2: '🥉',
}

def get_master(table, key):
    try:
        res = requests.get(f"{API_URL}/masters/{table}/{key}")
        return [x[key] for x in res.json()] if res.status_code == 200 else []
    except:
        return ['Substitution']