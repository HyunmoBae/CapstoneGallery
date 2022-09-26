from tkinter import *

window = Tk()
window.geometry("640x480")

def clickBtn(event):
    txt=""
    if event.num == 1:
        txt += "마우스 왼쪽 버튼"
    elif event.num == 3:
        txt += "마우스 오른쪽 버튼"

    txt +=str(event.x) + "," + str(event.y) + "이 좌표값"
    label1.configure(text=txt)

label1 = Label(window,text="텍스트")
window.bind("<Button>",clickBtn)

label1.pack(expand=True,anchor=CENTER)




window.mainloop()