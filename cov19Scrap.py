import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.worldometers.info/coronavirus/")
soup = BeautifulSoup(page.content, 'html.parcer')
print(soup)
