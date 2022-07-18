import requests
from bs4 import BeautifulSoup
import datetime
from day13.daostock import DaoStock



ds = DaoStock()

now = datetime.datetime.now()
ymd = now.strftime("%Y%m%d.%H%M")

url = "https://vip.mk.co.kr/newSt/rate/item_all.php"


html = requests.get(url)
html.encoding='EUC-KR'

soup = BeautifulSoup(html.text, 'html.parser')
tds = soup.find_all("td","st2")  

for idx,td in enumerate(tds) :
    s_name = td.text    #.text 글씨 가져오는 것
    s_code = td.a['title']
    price = td.parent.find_all("td")[1].text.replace(",","") 
    #.parent 부모 찾기 / find_all로 부모 안에 있는 자식 찾기  자식들 중에 2번째자리 / replace(",","") price는 int로 되어있어서 문자열 지우기.
    cnt = ds.insert(s_code,ymd,s_name,price)  # daostock와 연동
    
    print(idx,"cnt",cnt) 


