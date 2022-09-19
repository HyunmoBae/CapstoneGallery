from tkinter import *

window = Tk()
window.geometry("640x480")

#라디오버튼
label1 = Label(window,text="학년을 선택하세요")
label1.pack()

grade_var1 = StringVar()   #IntVar() : 정수값
btn_grade1 = Radiobutton(window,text="3학년",value="3학년",variable=grade_var1)
btn_grade1.select()
btn_grade2 = Radiobutton(window,text="4학년",value="4학년",variable=grade_var1)

btn_grade1.pack()
btn_grade2.pack()

def btngrade():
    print(grade_var1.get())

btn = Button(window,text="확인",command=btngrade)
btn.pack()






window.mainloop()