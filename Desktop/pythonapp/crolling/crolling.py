from urllib import request
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.naver.com")
html = response.text
soup = BeautifulSoup(html,'html.parser') 
word= soup.select_one(".logo_area")#class
word2= soup.select_one("#NM_set_home_btn") #id

print(word)
print(word2.text) #텍스트만

response2 = requests.get("https://news.naver.com")
html2 = response2.text
soup2 = BeautifulSoup(html2,'html.parser')
title = soup2.select_one(".cjs_t") #class
print(title)

#크롤링 막혔을때, 다 가져올때
header = {'User-agent':'Mozila/2.0'}

response3 = requests.get("https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100",headers=header)
html3 = response3.text
soup3 = BeautifulSoup(html3,'html.parser')
titles = soup3.select(".cluster_text_headline") 
for title in titles:
    print(title.text)

response4 = requests.get("https://news.daum.net/",headers=header)
html4 = response4.text
soup4 = BeautifulSoup(html4,'html.parser')
titles2 = soup4.select(".link_txt") 
for title in titles2:
    print(title.text.strip()) #빈칸정리
