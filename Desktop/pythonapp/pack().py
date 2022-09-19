from tkinter import *
from turtle import left
window = Tk()
window.title("제목없음")
window.geometry("640x480")

Label(window,text="메뉴/음료선택").pack(side="top")
Button(window,text="주문하기").pack(side="bottom")

frame_food = Frame(window,relief="solid",bd=1) #테두리
frame_food=LabelFrame(window,text="면류")
frame_food.pack(side="left",fill="both",expand=True)

frame_drink = LabelFrame(window,text="음료")
frame_drink.pack(side="right",fill="both",expand=True)

Button(frame_food,text="짜장면").pack()
Button(frame_food,text="짬뽕").pack()
Button(frame_food,text="탕수육").pack()

Button(frame_drink,text="콜라").pack()
Button(frame_drink,text="사이다").pack()

window.mainloop()