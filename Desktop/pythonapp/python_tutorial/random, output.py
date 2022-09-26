from random import *
from tkinter import Y

print(int(random() * 45)+1) #1이상 46미만의 정수
print(int(random() * 45)+1) #1이상 46미만의 정수
print(int(random() * 45)+1) #1이상 46미만의 정수
print(int(random() * 45)+1) #1이상 46미만의 정수

print(randrange(1,46)) #1이상 46미만의 정수

print(randint(1,45)) #1부터 45이하의 정수

date = randint(2,25)
date1 = randrange(2,26)

print("이번 회의 날짜는 "+ str(date) +"일 입니다")
print("이번 회의 날짜는 "+ str(date1) +"일 입니다")

#문자슬라이싱 변수[인덱스]
num = "000120-3456789"

print("성별 : "+num[7] )

#변수명[시작인덱스:종료인덱스]
print("연 : " +num[0:2] + " 월 : " + num[2:4] + " 일 : " + num[4:6])

print("주민등록 앞자리는 : "+num[0:6])
print("주민등록 뒷자리는 : "+num[7:14])

print("주민등록 앞자리는 : "+num[:6])
print("주민등록 뒷자리는 : "+num[7:])

print("주민등록 뒷자리는 : "+num[-7:])

text ="Python Java Node.js"
print(text)
print(text.lower()) #소문자
print(text.upper()) #대문자
print(text[0].isupper()) #인덱스 대문자 확인
print(len(text)) #숫자길이 확인
print(text.replace("Python","Spring")) #텍스트 대체
print(text.count("a"))

text1 = text.index("h")
print(text1)
text2 = text.find("h")
print(text2)
#둘의 차이점 : 해당 인덱스값이 없으면 에러발생
#index : 프로그램 종료 / find : -1을 반환
'''
text2 = text.find("p")
print(text2)
text1 = text.index("p")
print(text1)
'''

#다양한 포맷으로 문자열 출력
#출력1
print("저는 %d학년 입니다" %4) #정수
print("저는 %s에 다닙니다" %"대구가톨릭대학교") #문자열
print("이번 학기 성적은 %c입니다" %"A") #문자

print("저는 %s학년입니다." %4)
print("저는 %s에 %s를 다닙니다." %("대가대","컴정과"))

#출력2
print("나는 {}학년입니다.".format(3))
print("나는 {0}과 {1}학년입니다.".format("인공지능빅데이터공학",3))

#출력3
print("나는 {college}에 다니는 {grade}학년입니다.".format(college="대가대",grade=3))

#출력4 (파이썬 3.6부터 지원)
college = "머가머"
grade = 3

print(f"나는 {college}에 다니는 {grade}학년입니다")

#naver.com만 남기기
url = "https://www.naver.com"

urlname = url.replace("https://www.","") #재배치할 문자열 / 재배치할 문자
url2 = urlname[:5]
password = url2[:3]+ str(len(url)) + str(url.find("h")) + "!"

print(urlname)
print(url2)
print(password)
print(f"{url}의 비밀번호는 {password}입니다!") #또는
print("{0}의 비밀번호는 {1}입니다!".format(url,password)) #또는


