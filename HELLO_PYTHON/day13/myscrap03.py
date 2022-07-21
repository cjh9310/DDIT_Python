import requests
from bs4 import BeautifulSoup

url = "https://vip.mk.co.kr/newSt/rate/item_all.php"


html = requests.get(url)
html.encoding='EUC-KR'  # 매일경제가 UTF-8이 아니라 EUC-KR을 사용중이라 바꿔줌


print(html.text)        # 매일경제 페이지소스를 출력해봄 .text도 넣어줘야 함

soup = BeautifulSoup(html.text, 'html.parser')
tds = soup.find_all("td","st2") # st2 = 클래스

for td in tds :
    s_name = td.text    #.text 글씨 가져오는 것
    s_code = td.a['title']
    price = td.parent.find_all("td")[1].text #.parent 부모 찾기 / find_all로 부모 안에 있는 자식 찾기  자식들 중에 2번째자리
    
    #print(s_name,s_code,price) 

