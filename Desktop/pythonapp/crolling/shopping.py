from pydoc import html
import requests
from bs4 import BeautifulSoup

url = "https://search.shopping.naver.com/search/all?query=%ED%9C%B4%EB%8C%80%ED%8F%B0&frm=NVSHATC&prevQuery=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90"
response = requests.get(url)
print("응답코드 :", response.status_code)
if response.status_code == requests.codes.ok:
    print("정상적인 접근입니다.\n")
else:
    print("문제가 발생했습니다.\n")
html = response.text
soup = BeautifulSoup(html,"lxml")

products = soup.find_all("div",attrs={"class" : "basicList_info_area__TWvzp"})

with open("shopping.txt","w",encoding="utf-8")as s:
    for product in products:
        title = product.find("div",attrs={"class" : "basicList_title__VfX3c"}).get_text()
        price = product.find("span",attrs = {"class" : "price_num__S2p_v"}).get_text()
        review = product.find("em",attrs = {"class" : "basicList_num__sfz3h"}).get_text()
        link = product.find("a",attrs={"class":"basicList_link__JLQJf"})["href"]
        s.write("제품명 : " + title + "\n")
        s.write("가격 : " + price+ "\n")
        s.write("리뷰개수 : " + review + "개\n")
        s.write("링크 : " + link + "\n\n")





