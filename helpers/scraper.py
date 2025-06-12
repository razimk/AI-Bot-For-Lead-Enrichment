import requests
from bs4 import BeautifulSoup

def scrape_homepage(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.get_text(separator=" ", strip=True)[:2000]
    except:
        return "Could not fetch site content."
