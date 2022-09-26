#표준입출력

print("Python","Java")
print("Python" + "Java") #합
print("Python","Java",sep=",")

print("Pyhthon","Java","Node",sep=" vs ",end=" ")
print("당신의 선택은?")

scores = {"php":0,"java":90,"python":100} #튜플형태의 데이터
for i,score in scores.items():
    print(i.ljust(6),str(score).rjust(3),sep=" : ") #ljust(left정렬)

for num in range(1,21):
    print("번호 : " + str(num).zfill(3))  

#파일입출력

#book_file = open("book.txt","w",encoding="utf8") #파일 쓰기모드 열기
#print("Node : 5,000원",file=book_file)
#print("Java : 15,000원",file=book_file) 
#book_file.close()    

#book_file = open("book.txt","a",encoding="utf8")
#book_file.write("Php : 10,000")
#book_file.write("\nC# : 20,000")
#book_file.close()

#book_file = open("book.txt","r",encoding="utf8")
#print(book_file.read()) #전체 읽어오기
#print(book_file.readline(),end="")
#print(book_file.readline())
#book_file.close()

book_file = open("book.txt","r",encoding="utf8")
while True:
    line = book_file.readline()
    if not line:
        break #반복문 탈출
    print(line, end="")
book_file.close()   

book_file = open("book.txt","r",encoding="utf8")
lines = book_file.readlines() #모든 줄을 들고와서 리스트형태로
for line in lines:
    print(line,end="")
book_file.close()   