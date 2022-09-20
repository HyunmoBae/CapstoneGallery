from fileinput import filename
from tkinter import *
from tkinter import filedialog

window = Tk()
window.geometry("1280x960")
window.title = "이미지"

menu = Menu(window)

photo = PhotoImage()

label1 = Label(window, image=photo)
label1.pack(expand=True,anchor=CENTER)

def file_open():
    filename = filedialog.askopenfilename(title="이미지 파일을 선택하세요",filetypes=(("PNG파일","*.png"),("모든 파일","*.*")),initialdir="C:/Users/DCU/Desktop/pythonapp/image")

    photo=PhotoImage(file=filename)
    label1.configure(image=photo)
    label1.image = photo

menu_file = Menu(menu,tearoff=0)
menu_file.add_command(label="파일 열기",command=file_open)
menu_file.add_command(label="파일 저장",command=file_open)
menu_file.add_separator()
menu_file.add_command(label="끝내기",command=window.quit)

menu_edit = Menu(menu,tearoff=0)
menu_edit.add_command(label="복사")
menu_edit.add_command(label="오려두기")
menu_edit.add_command(label="붙여넣기")

menu_help = Menu(menu,tearoff=0)
menu_edit.add_command(label="도우말")

menu.add_cascade(label="파일",menu=menu_file)
menu.add_cascade(label="편집",menu=menu_edit)
menu.add_cascade(label="도우말",menu=menu_help)

window.config(menu=menu)

window.mainloop()



