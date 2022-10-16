# 모듈 import
import requests
import pprint

class Api_Parsing:
    
    def __init__(self):
        pass
    
    
    def parsing(self, startPage):
        #-----------------------------------------------------------------------------
        # 채용정보 url 입력
        url = 'https://openapi.work.go.kr/opi/opi/opia/wantedApi.do?'
        
        authKey = 'WNKJ18CZTJJ3NYY0JM1EU2VR1HK'
        
        params ={'authKey' : authKey, 
                 'callTp' : 'L', 
                 'returnType' : 'XML', 
                 'startPage' : startPage, 
                 'display' : '100' 
                }
        #-----------------------------------------------------------------------------
        
        response = requests.get(url, params=params)
        
        # xml 내용
        content = response.text
        
        print(content)
        # # 깔끔한 출력 위한 코드
        # pp = pprint.PrettyPrinter(indent=4)
        #
        # print(pp.pprint(content))
        
        
if __name__ == '__main__':
    ap = Api_Parsing()
    for i in range(1001):
        ap.parsing(i)
    
    
    