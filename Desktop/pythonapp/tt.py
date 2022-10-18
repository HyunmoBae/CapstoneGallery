import requests
from bs4 import BeautifulSoup

kakao = '035720'

url = f"https://finance.naver.com/item/sise.naver?code={kakao}"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html,'html.parser')
price = soup.select_one("#_nowVal").text
price = price.replace(',','')
print(f"오늘 카카오 주식가격은 {price}")
    