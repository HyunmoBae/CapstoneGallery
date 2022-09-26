import requests
from bs4 import BeautifulSoup

kakao = '035720'
naver='035420'
samsung='005930'
Hyundae='005380'
Lg='066570'

codes = [kakao,naver,samsung,Hyundae,Lg]

for code in codes:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html,'html.parser')
    price = soup.select_one("#_nowVal").text
    price = price.replace(',','')
    print(f"오늘 {price}")
    