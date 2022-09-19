from ctypes import sizeof
from tkinter import *
from turtle import left
window = Tk()
window.title("제목없음")
window.geometry("640x480")

frame = Frame(window)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right",fill="y")

listbox = Listbox(frame,selectmode="extended",height=10,yscrollcommand=scrollbar.set)
for i in range(1,32):
    listbox.insert(END,str(i)+"일")

listbox.pack(side="left")

scrollbar.config(command=listbox.yview)

window.mainloop()