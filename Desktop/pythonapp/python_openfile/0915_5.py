import time
import tkinter.ttk as ttk #ttk로 별칭 지정 
from tkinter import *

window = Tk()
window.geometry("640x480")

#콤보박스
values = [str(i) + "일" for i in range(1,32)]
cbox = ttk.Combobox(window,height=5,values=values)
cbox.pack()
cbox.set("날짜를 선택하세요")

#프로그레스바
pvar = DoubleVar()
probar = ttk.Progressbar(window,maximum=100,mode="determinate",length=150,variable=pvar)
#probar.start(10)
probar.pack()

def btn_cbox():
    #probar.stop()
    for i in range(1, 101):
        time.sleep(0.01) #0.01초 대기

        pvar.set(i)
        probar.update()
        print(pvar.get())

Button(window,text="시작",command=btn_cbox).pack()


window.mainloop()