from tkinter import *

file_list = ["image/img1.png","image/img2.png","image/img3.png","image/img4.png"]

num = 0

def clickNext():
    global num
    num += 1
    if num > 3:
        num = 3

    photo=PhotoImage(file=file_list[num])
    label1.configure(image=photo)
    label1.image = photo

def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 0

    photo=PhotoImage(file=file_list[num])
    label1.configure(image=photo)
    label1.image = photo

window = Tk()
window.geometry("1024x800")
window.title("사진앨범")

photo = PhotoImage(file=file_list[num])
label1 = Label(window,image=photo)
label1.place(x=250,y=50)
label1.image = photo

btn_Prev = Button(window,text="<< 이전",command=clickPrev)
btn_Prev.place(x=200,y=600)

btn_Next = Button(window,text=">> 다음",command=clickNext)
btn_Next.place(x=800,y=600)

label1.configure(image=photo)


window.mainloop()