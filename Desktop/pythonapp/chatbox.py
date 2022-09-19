#대화상자
from tkinter import *
from tkinter.simpledialog import *

window = Tk()
window.geometry("480x480")


label1 = Label(window,text="입력된 값")
label1.pack()

value = askinteger("숫자입력","숫자 1~6까지중 하나를 입력하세요",minvalue=1,maxvalue=6)
label1.configure(text=str(value))

window.mainloop()