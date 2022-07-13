import requests
from bs4 import BeautifulSoup

url = "https://vip.mk.co.kr/newSt/rate/item_all.php"

html = requests.get(url)

print(html)
print(html.text)

soup = BeautifulSoup(html.text, 'html.parser')
trs = soup.select("td")

for idx,tr in enumerate(trs):
    if idx > 0 :
        tds = tr.select("a")
        print(idx, tds[1].text, tds[3].text)


