from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pyautogui

now = datetime.now()
date = now.date()

keyword = pyautogui.prompt("검색어를 입력하세요")
pageNum = 1
lastpage = pyautogui.prompt("마지막 페이지를 입력하세요")
 
with open("news."+ str(date) + "txt","w",encoding="utf8") as news:
    for i in range(1,int(lastpage)*10,10):#시작,끝,단계    
        print(f"{pageNum}페이지 입니다.=========================================================\n\n")
        response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={i}")
        html = response.text
        soup = BeautifulSoup(html,'html.parser')
        links = soup.select(".news_tit")

        news.write(f"{keyword}의 헤드라인입니다.")
        news.write(f"\n{pageNum}페이지 입니다.=============================================\n\n")
        for link in links:
            title = link.text
            url = link.attrs['href'] #href의 속성값을 가져온다.
            print(title)
            news.write(title + "\n")
        pageNum = pageNum + 1

#news.txt 저장
