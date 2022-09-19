#50명의 손님 콜택시 5분 ~ 15분 사이의 거리가 탑승 받음
from random import *

count = 0 
#반복문
for i in range(1,51): #승객의 수
    time = randrange(5,51) #임의의 수를 발생 소요시간

    if 5 <= time <=15:
        print("{0}번째 손님은 예상소요시간이 {1}분입니다.\n출발합니다.".format(i,time))
        count += 1
    else:
        print("{0}번째 손님은 예상소요시간이 {1}분입니다.\n승차거부합니다.".format(i,time))  

print("주행가능한 손님은 : {0}분입니다.".format(count))  