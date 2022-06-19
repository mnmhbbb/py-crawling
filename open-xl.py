import openpyxl
fPath = r'/Users/mhbaek/dev/python/xlsx/test-1.xlsx'

# 5. 엑셀 불러오기
importXl = openpyxl.load_workbook(fPath)

# 6. 엑셀 시트 선택
importXs = importXl['worksheet-1']

# 7. 데이터 수정하기
importXs['A4'] = '456'
importXs['B4'] = '안녕'

# 8. 엑셀 저장하기
importXl.save(fPath)