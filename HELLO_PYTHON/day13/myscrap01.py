import requests

url = "http://127.0.0.1:5000/"

html = requests.get(url)

print(html)
print(html.text)