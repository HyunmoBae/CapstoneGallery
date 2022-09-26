#
from cProfile import label
from fileinput import filename
from tkinter import *
from tkinter.filedialog import *

window = Tk()
window.geometry("480x480")

label1 = Label(window, text="선택된 파일이름")
label1.pack()

# filename= askopenfilename(parent=window,filetypes=(("PNG 파일","*.png"),("모든 파일","*.*")))
# label1.configure(text=str(filename))

savefile = asksaveasfile(parent=window,mode="w",defaultextension=".png",filetypes=(("PNG 파일","*.png"),("모든 파일","*.*")))
label1.configure(text=savefile)

window.mainloop()