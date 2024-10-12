import requests
from bs4 import BeautifulSoup


def fetch_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup


if __name__ == "__main__":
    url = "https://www.example.com"
    data = fetch_data(url)
    print(data.prettify())
