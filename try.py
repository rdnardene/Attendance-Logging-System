
from tkinter import *
import os


def openwindow():
    window.withdraw()

    os.system("try1.py")

window = Tk()

btn1 = Button(window, text="Open Second Frame", command=openwindow)
btn1.pack()

window.mainloop()