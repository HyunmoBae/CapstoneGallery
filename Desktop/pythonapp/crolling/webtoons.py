import requests
from bs4 import BeautifulSoup

#회차정보
with open("education.txt","w",encoding="utf8") as education:
    education.write("참교육 회차정보 \n\n")

    for i in range(1,11):
        education.write(f"{i}페이지\n")
        url = f"https://comic.naver.com/webtoon/list?titleId=758037&weekday=mon&page={i}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text,"lxml")
        webtoons = soup.find_all("td",attrs={"class":"title"})

        for webtoon in webtoons:
            title = webtoon.a.get_text()
            link = "https://comic.naver.com" + webtoon.a["href"]
            education.write(f"{title} ({link})\n")

#평점
ratings = soup.find_all("div",attrs={"class":"rating_type"})
rates = ratings[0].find("strong")

total_rates = 0

for rate in ratings:
    rating = rate.find("strong").get_text()
    #print(rating)
    total_rates += float(rating)

#print(total_rates/len(ratings))#평균


