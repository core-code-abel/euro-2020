import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

API_URL = os.getenv("API_URL")

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