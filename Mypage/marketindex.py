import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/'
response = requests.get(url).text

data = BeautifulSoup(response, 'html.parser')

exchange = data.select_one('')
result = exchange.text
print(result)