import requests
from bs4 import BeautifulSoup

URL = "https://www.x-rates.com/table/?from=USD&amount=1"
r = requests.get(URL) # this opens the website

soup = BeautifulSoup(r.content, 'html.parser')
print(soup)