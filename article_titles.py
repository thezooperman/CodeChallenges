"""HTTP and Web Scraping shit"""
import requests
from bs4 import BeautifulSoup

URL = 'http://www.nytimes.com/'


def parsedata():
    """
    Some strange HTTP request parse shit
    """
    with requests.get(URL, stream=True) as req:
        req.raise_for_status()
        assert req.status_code == 200, 'Some strange shit happened\
        during HTTP GET'
        r_html = req.text
        soup = BeautifulSoup(r_html, 'html.parser')
        for link in soup.find_all('h2', {'class': "story-heading"}):
            if link.string is not None:
                print(link.string.strip())


parsedata()
