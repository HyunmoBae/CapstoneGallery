#if문 if조건:

from pickletools import int4


score = int(input("성적을 입력하세요"))

if score >= 90:
    print("성적은 A 입니다.")
elif score >= 80:
    print("성적은 B 입니다.")
elif score >= 70:
    print("성적은 C 입니다.")
else:
    print("불합격 입니다.")

#for 반복문 : for 변수 in 반복대상:
for i in [1,2,3]:
    print("번호 : {0}".format(i))

for i in range(1,101):
    print("번호 : {0}".format(i))

name = ["홍길동","김철수","박영희"]

for name1 in name:
    print("{0}님 반갑습니다.".format(name1))

#while문 : 조건이 만족하는동안 반복

    num = 1
while(num<=10):
    print("숫자는 {0} 입니다.".format(num))
    num+=1
    if num > 10:
        print("10초과!")

#한줄 for문
number = [1,2,3,4,5]
number = [i + 100 for i in number]
print(number)

name = ["홍길동","김철수","박영희희"]
name = [len(i) for i in name]
print(name)
