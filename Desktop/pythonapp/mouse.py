#키보드와 마우스 이벤트 처리
import tkinter.messagebox as msgbox
from tkinter import * 

def leftclick(event):
    msgbox.showinfo("마우스","마우스 왼쪽 버튼을 클릭하였습니다.")

def imgclick(event):
    msgbox.showinfo("마우스","이미지 파일클릭")

window = Tk()
window.geometry("1024x760")

photo = PhotoImage(file="icon.png")
label1 = Label(window,image=photo)
label1.pack(expand=True,anchor=CENTER)

label1.bind("<Button>",imgclick)
#window.bind("<Button-1>",leftclick) #Button-1 왼쪽버튼 / Button-2 가운데버튼 / Button-3 우측버튼 / Button 모든버튼
window.mainloop()



