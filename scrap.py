import requests
from bs4 import BeautifulSoup
import json
import codecs

URL = "https://quranromanurdu.com/chapter/1"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

table = soup.findAll('div',attrs={"id":"contentpara"})

values = list(filter(None, table[0].text.split('\n')))
values = list(filter(None, [value.replace("\xa0", "") for value in values[1:]]))

d = {}
for item in values:
    key, value = item.split('.', maxsplit=1)
    d[key] = value

print(d)    




