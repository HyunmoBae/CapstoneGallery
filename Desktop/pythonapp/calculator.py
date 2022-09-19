from ast import Delete, Num
from tkinter import *
from unittest import result

window = Tk()
window.title("계산기")
#window.geometry("320x500")


entry_box = Entry(window,width=30,borderwidth=5)
entry_box.grid(row=0,column=0,columnspan=4)


def btn_click(number):
    curr_num = entry_box.get()
    entry_box.delete(0,END)
    entry_box.insert(0,str(curr_num) + str(number))

def btn_clear():
    entry_box.delete(0,END)

def btn_add():
    first_num = entry_box.get()
    global g_first_num #전역변수
    global g_operation
    g_operation = 'add'
    g_first_num = int(first_num)

    entry_box.delete(0,END)
def btn_minus():
    first_num = entry_box.get()
    global g_first_num #전역변수
    global g_operation
    g_operation = 'minus'
    g_first_num = int(first_num)
    entry_box.delete(0,END)

def btn_multy():
    first_num = entry_box.get()
    global g_first_num #전역변수
    global g_operation
    g_operation = 'multy'
    g_first_num = int(first_num)
    entry_box.delete(0,END)

def btn_divide():
    first_num = entry_box.get()
    global g_first_num #전역변수
    global g_operation
    g_operation = 'divide'
    g_first_num = int(first_num)
    entry_box.delete(0,END)

def btn_equal():
    second_num = int(entry_box.get())
    entry_box.delete(0,END)

    if g_operation == 'add':
      result = g_first_num + second_num
      entry_box.insert(0,result)
        
    elif g_operation == 'minus':
       result = g_first_num - second_num
       entry_box.insert(0,result)

    elif g_operation == 'multy':
        result = g_first_num * second_num
        entry_box.insert(0,result)

    elif g_operation == 'divide':
        result = g_first_num / second_num
        entry_box.insert(0,result)

btn_7 = Button(window,text="7",padx=25,pady=15,width=1,command=lambda:btn_click(7))
btn_8 = Button(window,text="8",padx=25,pady=15,width=1,command=lambda:btn_click(8))
btn_9 = Button(window,text="9",padx=25,pady=15,width=1,command=lambda:btn_click(9))
btn_x = Button(window,text="x",padx=25,pady=15,width=1,command=btn_multy)

btn_4 = Button(window,text="4",padx=25,pady=15,width=1,command=lambda:btn_click(4))
btn_5 = Button(window,text="5",padx=25,pady=15,width=1,command=lambda:btn_click(5))
btn_6 = Button(window,text="6",padx=25,pady=15,width=1,command=lambda:btn_click(6))
btn_mi = Button(window,text="-",padx=25,pady=15,width=1,command=btn_minus)

btn_1 = Button(window,text="1",padx=25,pady=15,width=1,command=lambda:btn_click(1))
btn_2 = Button(window,text="2",padx=25,pady=15,width=1,command=lambda:btn_click(2))
btn_3 = Button(window,text="3",padx=25,pady=15,width=1,command=lambda:btn_click(3))
btn_pl = Button(window,text="+",padx=25,pady=15,width=1,command=btn_add)

btn_0 = Button(window,text="0",padx=25,pady=15,width=1,command=lambda:btn_click(0))
btn_C = Button(window,text="C",padx=25,pady=15,width=1,command=btn_clear)
btn_e = Button(window,text="=",padx=25,pady=15,width=1,command=btn_equal)
btn_s = Button(window,text="/",padx=25,pady=15,width=1,command=btn_divide)

btn_7.grid(row=1,column=0)
btn_8.grid(row=1,column=1)
btn_9.grid(row=1,column=2)
btn_x.grid(row=1,column=3)

btn_4.grid(row=2,column=0)
btn_5.grid(row=2,column=1)
btn_6.grid(row=2,column=2)
btn_mi.grid(row=2,column=3)

btn_1.grid(row=3,column=0)
btn_2.grid(row=3,column=1)
btn_3.grid(row=3,column=2)
btn_pl.grid(row=3,column=3)

btn_0.grid(row=4,column=0)
btn_C.grid(row=4,column=1)
btn_e.grid(row=4,column=2)
btn_s.grid(row=4,column=3)

window.mainloop()