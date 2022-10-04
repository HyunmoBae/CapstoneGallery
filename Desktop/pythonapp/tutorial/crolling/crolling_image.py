import requests
from bs4 import BeautifulSoup

for year in range(2011,2022):

    url = f"https://search.daum.net/search?w=tot&m=&q={year}%20%EC%98%81%ED%99%94%20%EC%88%9C%EC%9C%84&nzq=%EC%98%81%ED%99%94%20%EC%88%9C%EC%9C%84&DA=NSJ"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html,"lxml")

    images = soup.find_all("img",attrs={"class":"thumb_img"})

    for idx, image in enumerate(images): #for 원소값
        print(image["src"])
        image_url = image["src"]
        if image_url.startswith("//"): #문자를 찾는기능 : startswith(시작하는문자)
            image_url = "https:" + image_url #https:추가
        print(image_url)
        image_response = requests.get(image_url)

        with open("img_{}_{}.jpg".format(year,idx + 1),"wb") as img:
            img.write(image_response.content)
        if idx >= 4: #상위 5개만 다운로드
            break

