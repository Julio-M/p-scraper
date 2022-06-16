import requests
from bs4 import BeautifulSoup
import json

URL = "https://en.wikipedia.org/wiki/List_of_programming_languages"
response = requests.get(URL)

soup = BeautifulSoup(response.content, 'html.parser')

data = soup.find(id="mw-content-text")

results = data.find_all('li')

all_data = []

for content in results:
    data = {}
    language = content.text
    data['language'] = language
    source = content.find('a').get('href')
    if source != None:
        data['source'] = (f'https://en.wikipedia.org{source}')
    all_data.append(data)


with open("data.json", "w") as outfile:
    json.dump(all_data, outfile)
