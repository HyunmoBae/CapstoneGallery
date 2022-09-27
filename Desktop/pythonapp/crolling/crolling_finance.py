import requests
from bs4 import BeautifulSoup
import csv

f = open("시가총액.csv","w",encoding="utf-8-sig",newline="")
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
writer.writerow(title)

for page in range(1,3):
    url = f"https://finance.naver.com/sise/sise_market_sum.naver?sosok=0&page="
    response = requests.get(url+str(page))
    html = response.text
    soup = BeautifulSoup(html,"lxml")

    finances = soup.find("table",attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for finance in finances:
        columns = finance.find_all("td")
        if len(columns) <= 1:
            continue
        data = [column.get_text().strip() for column in columns] #1줄 for문
        #print(data)
        writer.writerow(data)

f.close()







