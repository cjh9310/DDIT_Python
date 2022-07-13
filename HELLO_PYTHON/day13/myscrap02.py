import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:5000/"

html = requests.get(url)

print(html)
print(html.text)

soup = BeautifulSoup(html.text, 'html.parser')
trs = soup.select("tr")

for idx,tr in enumerate(trs):
    if idx > 0 :
        tds = tr.select("td")
        print(idx, tds[1].text, tds[3].text)


