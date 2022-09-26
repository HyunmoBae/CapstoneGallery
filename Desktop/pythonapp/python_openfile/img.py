#윈도우창
from cgitb import text
from msilib.schema import CheckBox
from tkinter import *

window = Tk()
window.title("계산기")
#window.geometry("640x480+300+0") #가로*세로+x좌표+y좌표
#window.resizable(False,False)

#텍스트 & 엔트리 (textarea / input type="text")
txt = Text(window,width=30,height=5)
txt.pack()
txt.insert(END,"내용을 입력하세요")

ey = Entry(window,width=30)
ey.pack()
ey.insert(0,"글을 입력하세요")

def btn_txt():
    print(txt.get("1.0",END)) #첫번째 라인 0번째 칼럼
    print(ey.get())

    txt.delete("1.0",END)
    ey.delete(0, END)

btn_a = Button(window,text="클릭",command=btn_txt)
btn_a.pack()

#체크버튼
chkvar = IntVar()
chkbox = Checkbutton(window,text="체크하세요",variable=chkvar)
#chkbox.select()
chkbox.pack()

def btnchk():
    print(chkvar.get())

btn_chk = Button(window,text="체크",command=btnchk)
btn_chk.pack()


#리스트박스 (select)
listbox = Listbox(window,selectmode="extended",height=0) #single / extended
listbox.insert(0,"홍길동")
listbox.insert(1,"김철수")
listbox.insert(2,"이영희")
listbox.insert(END,"박영숙")
listbox.pack()

def btnlist():
    #listbox.delete(END)
    print("리스트 목록은", listbox.size(), "개")
    print(listbox.get(0,2))
    print("선택한 항목 :", listbox.curselection())
btn_list = Button(window,text="확인",command=btnlist)
btn_list.pack()

#레이블
label1 = Label(window,text="안녕하세요")
label1.pack()

photo1 = PhotoImage(file="icon.png")
label2 = Label(window,image=photo1)
label2.pack()

#버튼
btn1 = Button(window,text="버튼")
btn1.pack()

btn2 = Button(window,padx=10,pady=5,text="버튼버튼버튼버튼버튼버튼")
btn2.pack()

btn3 = Button(window,width=10,height=3,text="버튼버튼버튼버튼버튼버튼")
btn3.pack()

btn4 = Button(window,fg="red",bg="blue",text="버튼")
btn4.pack()

btn6 = Button(window,text="종료",command=quit)
btn6.pack()

photo = PhotoImage(file="icon.png")
btn5 = Button(window,image=photo)
btn5.pack()




window.mainloop()