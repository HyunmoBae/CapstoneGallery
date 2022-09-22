import openpyxl

#액셀파일 수정
fpath = r"C:\Users\DCU\Desktop\pythonapp\업체별 현재시세.xlsx"

#액셀 불러오기
wb = openpyxl.load_workbook(fpath)

#시트 선택
ws = wb['업체별 현재시세']

ws['A7'] = '엔씨소프트'

wb.save(fpath)