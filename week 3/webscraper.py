import requests
from bs4 import BeautifulSoup

URL = "https://www.x-rates.com/table/?from=USD&amount=1"
r = requests.get(URL) # this opens the website

soup = BeautifulSoup(r.content, 'html.parser') # prints the website content
ratelist = soup.findAll("table", {"class": "ratesTable"})[0].findAll("tbody") # this finds the table

for i in ratelist:
    trList = i.findAll('tr') # tr is the thing before the text in the html file, .findall finds all instances, tr is table row
    for j in trList[:10]: # prints the 10 table contents
        print(j.text)