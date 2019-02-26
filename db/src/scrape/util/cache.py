import os
import src.settings as settings
import json


def get(id):
    path = f"{settings.SCRAPE_CACHE_ROOT}/{id}.json"
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        return json.load(f)


def set(id, data):
    path = f"{settings.SCRAPE_CACHE_ROOT}/{id}.json"
    with open(path, "w") as f:
        f.write(json.dumps(data))
