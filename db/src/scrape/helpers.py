"""
Various helpers
"""
import requests
from bs4 import BeautifulSoup


def get_soup(url):
    """
    Makes a request to the given url and returns a BeautifulSoup instance of Soup
    """
    res = requests.get(url)

    if not res.content:
        return None
    soup = BeautifulSoup(res.content, "lxml")
    return soup
