from urllib import request, response
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
response = requests.get(url)
soup = BeautifulSoup(response.text,"lxml")

print(soup.title)
print(soup.title.get_text()) #<title>의 구조를 전체들고옴
print(soup.a) #첫번째 a태그 가져오기
print(soup.a.attrs) #a의 속성들을 가져옴
