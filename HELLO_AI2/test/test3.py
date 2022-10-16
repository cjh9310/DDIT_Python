from urllib.parse import urlencode, quote_plus, unquote
import requests
from urllib.request import urlopen, Request

url = 'http://openapi.work.go.kr/opi/opi/opia/wantedApi.do?authKey=WNKJ18CZTJJ3NYY0JM1EU2VR1HK&callTp=L&returnType=XML&startPage=1&display=10?'
key = 'WNKJ18CZTJJ3NYY0JM1EU2VR1HK'

queryParams = '&' + urlencode({quote_plus('page'): '1', 
                               quote_plus('perPage'): '1824', 
                               quote_plus('returnType'): 'JSON'})
get_data = requests.get(url + key + unquote(queryParams))


request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
f = open('aaa.xml', 'wb')
f.write(response_body)