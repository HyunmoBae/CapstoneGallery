from ast import keyword
from urllib import response
import requests
from bs4 import BeautifulSoup

keyword = input("검색어를 입력하세요")
response = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=" + keyword)
html = response.text
soup = BeautifulSoup(html,'html.parser')
links = soup.select(".news_tit")
for link in links:
    title = link.text
    url = link.attrs['href'] #href의 속성값을 가져온다.
    print(title,url)


