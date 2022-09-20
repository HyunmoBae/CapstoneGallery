from tkinter import *

def pic_btn():
    if var.get() == 1:
        labelimage.configure(image=photo1)
    elif var.get() == 2:
        labelimage.configure(image=photo2)
    elif var.get() == 3:
        labelimage.configure(image=photo3)
    elif var.get() == 4:
        labelimage.configure(image=photo4)
  

window = Tk()
window.geometry("1024x768")

labelText=Label(window,text="보고싶은 사진을 선택하세요",fg="blue",font=20)
labelText.pack()
var=IntVar()

opt1 = Radiobutton(window,text="사진1",variable=var,value=1)
opt1.pack(padx=5,pady=5)
opt2 = Radiobutton(window,text="사진2",variable=var,value=2)
opt2.pack(padx=5,pady=5)
opt3 = Radiobutton(window,text="사진3",variable=var,value=3)
opt3.pack(padx=5,pady=5)
opt4 = Radiobutton(window,text="사진4",variable=var,value=4)
opt4.pack(padx=5,pady=5)


btn_s=Button(window,text="사진보기",command=pic_btn)
btn_s.pack(padx=5,pady=5)

photo1 = PhotoImage(file="image/img1.png")
photo2 = PhotoImage(file="image/img2.png")
photo3 = PhotoImage(file="image/img3.png")
photo4 = PhotoImage(file="image/img4.png")

labelimage = Label(window,width=600,height=400,bg="yellow")
labelimage.pack()


window.mainloop()