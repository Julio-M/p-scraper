import requests
from bs4 import BeautifulSoup
import re

URL = "https://en.wikipedia.org/wiki/List_of_programming_languages"
response = requests.get(URL)

soup = BeautifulSoup(response.content, 'html.parser')

data = soup.find(id="mw-content-text")

results = data.find_all('li')

for content in results:
    language = content.text
    source = content.find('a').get('href')
    if source != None:
        print(f'https://en.wikipedia.org{source}')
