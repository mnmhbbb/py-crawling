import openpyxl
import requests
from bs4 import BeautifulSoup
import openpyxl

fpath = r'/Users/mhbaek/dev/python/test-1.xlsx'
wb = openpyxl.load_workbook(fpath)
ws = wb.active # 현재 활성화된 시트

codes = [
  '005930',
  '000660',
  '035720'
]

row = 2
for code in codes:
  url = f'https://finance.naver.com/item/sise.naver?code={code}'
  res = requests.get(url)
  html = res.text
  soup = BeautifulSoup(html, 'html.parser')
  price = soup.select_one('#_nowVal').text
  print(price)
  ws[f'B{row}'] = price
  row = row + 1

wb.save(fpath)