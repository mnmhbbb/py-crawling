import requests
from bs4 import BeautifulSoup

codes = [
  '005930',
  '000660',
  '035720'
]

for code in codes:
  url = f'https://finance.naver.com/item/sise.naver?code={code}'
  res = requests.get(url)
  html = res.text
  soup = BeautifulSoup(html, 'html.parser')
  price = soup.select_one('#_nowVal').text
  print(price)