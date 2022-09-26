#리스트
num1 = 10
num2 = 20
num3 = 30

num_1 = [10,20,30,15,25]
num_1.sort() #정렬
print(num_1)
num_1.reverse() #뒤집기
print(num_1)
num_1.clear() #데이터 삭제
print(num_1)

pg = ["Node.js","php","Java"]
print(pg)
print(pg.index("Java"))
pg.append("Python") #데이터 끝에 추가(.append)
print(pg)
pg.insert(1,"Oracle")
print(pg)

print(pg.pop()) #맨 뒤에서부터 삭제
print(pg)

pg.append('php')
print(pg)
print(pg.count("php"))

#사전 : key value
member = {1: "배현모",2:"andrue",0:"zero",}
print(member[0]) #값이 없으면 프로그램 종료
print(member.get(3)) #값이 없으면 None을 발생하고 프로그램 계속 실행
print(3 in member) #false // 키 값이 있는지 여부 확인 (in)

member1 = {"a": "배현모","b":"andrue","c":"zero",} # 키 값 문자도 가능
print(member1.get("c"))
member1["d"]="배현모" #데이터가 없으면 신규등록
member1["a"]="배현무" #데이터가 있으면 변경
print(member1)

print(member1.keys()) #키 값만 출력
print(member1.values()) #value 값만 출력
print(member1.items()) #둘다 출력

del member1["c"] #해당되는 키 삭제
print(member1)
member1.clear() #다 삭제
print(member1)

#튜플
member2 = ("홍길동","배현모")
print(member2[0])
print(member2[1])

name="홍길동"
college="대가대"
grade=4

(name, college, grade) = ("홍길동","대가대",4)
print(name,college,grade)

#세트(set) - 중복을 허용하지 않는다.
number_1 = {1,2,3,1,1}
print(number_1,type(number_1))
number_1 = list(number_1)
print(number_1,type(number_1))
number_1 = tuple(number_1)
print(number_1,type(number_1))
number_1 = set({1,2,3,1,1})
print(number_1,type(number_1))

print(number_1) #{1,2,3}






