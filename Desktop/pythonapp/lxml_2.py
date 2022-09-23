import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
response = requests.get(url)
soup = BeautifulSoup(response.text,"lxml")

# print(soup.title)
# print(soup.title.get_text()) #<title>의 구조를 전체들고옴
# print(soup.a) #첫번째 a태그 가져오기
# print(soup.a.attrs) #a의 속성들을 가져옴
# print(soup.a["href"])
# print(soup.find("a",attrs={"class":"Nbtn_upload"}).get_text())

# 구조를 통해서 가져오기
# rank1 = soup.find("li",attrs={"class":"rank01"})
# print(rank1.a.get_text())
# rank2 = rank1.next_sibling.next_sibling
# print(rank2.a.get_text())
# rank2_1 = rank3.previous_sibling.previous_sibling
# print(rank2_1.a.get_text())

# print(rank1.parent) #rank1의 부모부터 출력
# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank1_1 = rank2.find_previous_sibling("li")
# print(rank1_1.a.get_text())

days = ["mon","tue","wed","thu","fri","sat","sun"]

titles = soup.findAll("a",attrs={"class":"title"})

with open("naver_webtoon.txt","w",encoding="utf8") as webtoon:
    webtoon.write("현재 네이버웹툰에서 연재중인 웹툰입니다.\n\n")
    for title in titles:
        webtoon.write(str(title.get_text()) + "\n")

