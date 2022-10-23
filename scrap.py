import requests
from bs4 import BeautifulSoup
import json
import codecs
import random


y = random.randrange(114)
urll = "https://quranromanurdu.com/chapter/{}".format(y)
print(urll)

URL = urll
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

table = soup.findAll('div',attrs={"id":"contentpara"})



values = list(filter(None, table[0].text.split('\n')))

values = list(filter(None, [value.replace("\xa0", "") for value in values[1:]]))

d = {}
for item in values:
    key, value = item.split('.' ,maxsplit = 1)
    d[key] = value

print(d)
k = list(d.keys())
maxx = int(max(k))
minn  =int(min(k))


randayahno = random.randrange(minn,maxx)
srandayahno = str(randayahno)
ayah = d.get(srandayahno, "not found")



# print("chapter: {}".format(y))
# print("ayah no: {}".format(srandayahno))
# print("ayah : {}".format(ayah))

x = {
    "chapter": y ,
    "ayah no": srandayahno ,
    "ayah " : ayah
}


jsonn = json.dumps(x)

print(jsonn)