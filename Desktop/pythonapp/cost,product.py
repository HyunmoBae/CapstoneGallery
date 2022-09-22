import requests
from bs4 import BeautifulSoup
import pyautogui

keyword = pyautogui.prompt("검색어를 입력하세요")


response = requests.get(f"https://search.shopping.naver.com/search/all?query={keyword}&cat_id=&frm=NVSHATC")
html = response.text
soup = BeautifulSoup(html,'html.parser')
links = soup.select(".basicList_link__JLQJf")
prices = soup.select_one(".price_num__S2p_v")

for link in links:
    title = link.text
    price = prices.text
    
    url = link.attrs['href'] #href의 속성값을 가져온다.
    print(title)
    print(price) #수정필요


#news.txt 저장
