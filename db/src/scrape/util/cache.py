import os
import src.settings as settings
import json
from bs4 import BeautifulSoup


def get(id):
    path = f"{settings.SCRAPE_CACHE_ROOT}/{id}.json"
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        return json.load(f)


def set(id, data):
    path = f"{settings.SCRAPE_CACHE_ROOT}/{id}.json"
    with open(path, "w+") as f:
        f.write(json.dumps(data))


def get_html(id):
    path = f"{settings.SCRAPE_CACHE_ROOT}/{id}.html"
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        return BeautifulSoup(f, "lxml")


def set_html(id, data):
    path = f"{settings.SCRAPE_CACHE_ROOT}/{id}.html"
    with open(path, "w+") as f:
        f.write(data)
