import tkinter.messagebox as msgbox
from tkinter import *

def keyEvent(event):
    msgbox.showinfo("키보드","눌린키 : " + chr(event.keycode))

window = Tk()

window.bind("<Key>",keyEvent)

window.mainloop()
