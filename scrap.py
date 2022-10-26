from curses.ascii import isdigit
import re
import requests
from bs4 import BeautifulSoup
import json
import codecs
import random


y = random.randrange(114)
# urll = "https://quranromanurdu.com/chapter/{}".format(y)
urll = "https://quranromanurdu.com/chapter/38"
print(urll)

URL = urll
page = requests.get(URL)

soup = BeautifulSoup(page.text, "html.parser")

table = soup.findAll('div',attrs={"id":"contentpara"})

# print(table[0].findAll('p'))

data = {}
count = 1
for p in table[0].findAll('p'):
    if not p.find('strong'):
        data[str(count)] = p.text
        count += 1

# print(data)



# values = list(filter(None, table[0].text.split('\n')))

# values = list(filter(None, [value.replace("\xa0", "") for value in values[1:]]))

# d = {}
# di = []
# for item in values:
#     print(item)
#     try:
#         key, value = item.split('.' ,maxsplit = 1)
#         d[key] = value
#     except ValueError:
#         value = item.split('.' , maxsplit= 1)
#         di.append(value)



# print(d)
# print(di)

k = list(data.keys())


maxx = int(max(k))
minn = int(min(k))


randayahno = random.randrange(minn,maxx)
srandayahno = str(randayahno)
ayah = data.get(srandayahno, "not found")

for ele in ayah:
    if ele.strip().isdigit():
        ayah.replace(ele, ' ')
try:
    ayah = ayah.split(':')[1].strip()
except IndexError:
    ayah = ayah.strip()
# ayah = ayah.replace(u'\xa0', u' ')
# for ele in ayah:
#     if ele.isdigit() or ele == ":":
#         ayaah =ayah.replace(ele, " ")
#     else:
#         pass   



print("chapter: {}".format(y))
print("ayah no: {}".format(srandayahno))
print("ayah : {}".format(ayah))

# x = {
#     "chapter": y ,
#     "ayah no": srandayahno ,
#     "ayah " : ayah
# }


# jsonn = json.dumps(x)

# print("\n",jsonn)