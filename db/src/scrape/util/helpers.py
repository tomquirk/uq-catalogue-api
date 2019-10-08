"""
Various helpers
"""
import requests
from bs4 import BeautifulSoup


def get_soup(url):
    """
    Makes a request to the given url and returns a BeautifulSoup instance of Soup

    """
    res = requests.get(
        url,
        headers={
            "accept": "text/html",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
        },
    )

    if not res.content:
        return None
    soup = BeautifulSoup(res.content, "lxml")
    return soup
