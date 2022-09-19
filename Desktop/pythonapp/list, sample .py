from random import *

number = [1,2,3,4,5] #리스트 형태의 데이터
shuffle(number) #데이터 섞기
print(number)
print(sample(number,3)) #데이터 n개 뽑기

#로또번호 뽑기
lotto = range(1,46)
lotto = list(lotto) #리스트로 변환
print(lotto)
shuffle(lotto)
happy_lotto = sample(lotto,7)
print("이번 로또 추첨번호는 " + str(happy_lotto) + " 입니다")
print("이번 로또 추첨번호는 {} 입니다.".format(happy_lotto[:6]))
print("이번 로또 추첨 보너스 번호는 {} 입니다.".format(happy_lotto[6]))

#ex) 총 인원이 20명이다. 여기서 3명을 뽑을것이다. 1등:1명, 2등:3명
#answer 1
people = range(1,21)
event = sample(people,4)
first = event[0]
second = event[1:]
print(event)
print(first)
print(second)

#answer 2
entry_number = list(range(1,21))
shuffle(entry_number)
print(entry_number)

win1_number = sample(entry_number,1)
print(win1_number)
etc_number = set(entry_number) - set(win1_number)
print(etc_number)


win2_number = sample(etc_number,3)
print(win1_number)
print(win2_number)

number_1 = set([1,2,3,4,5,6])
number_2 = set([1,3,5,7,9])

print(number_1 & number_2) #교집합
print(number_1.intersection(number_2)) #교집합

print(number_1 | number_2) #합집합
print(number_1.union(number_2)) #합집합

print(number_1 - number_2) #차집합
print(number_1.difference(number_2)) #차집합

number_1.add(100) #데이터 추가
print(number_1)
