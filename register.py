from tkinter import*
import tkinter
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from tkinter import filedialog

class Register:

    def __init__(self,root):
        self.root = root

        self.root.title("Registration Form")
        self.root.geometry("850x500+250+100")
        self.root.resizable(False, False)
        def open():
            global my_image
            pik.filename = filedialog.askopenfilename(
                initialdir="/Face-Recognition-Based-Attendance-System-main/images",
                title="Select a file", filetypes=(("jpg files", "*.jpg"), ("all files", "*,*")))
            my_label = Label(pik, text=pik.filename).pack()
            my_image = ImageTk.PhotoImage(Image.open(pik.filename))
            my_image_label = Label(image=my_image).pack()


        self.left = ImageTk.PhotoImage(file = "images/bg.png")
        left = Label(self.root, bg="green", image = self.left).place(x=0,y=0,width=440,height=500)


        Frame_register = Frame(self.root, bg="white")
        Frame_register.place(x=450, y=0, width=550, height=500)

        pik = tkinter.Frame(Frame_register, bg="black")
        pik.place(x=250, y=250, width=130, height=130)

        lbl_user = Label(Frame_register, text="Full Name:", font=("Goudy old style", 15, "bold"), fg="grey",
                         bg="white").place(x=5, y=120)
        self.fname = Entry(Frame_register, font=("Goudy old style", 15), bg="#E7E6E6")
        self.fname.place(x=170, y=120, width=240, height=30)

        lbl_course = Label(Frame_register, text="Course & Section:", font=("Goudy old style", 15, "bold"), fg="grey",
                           bg="white").place(x=5, y=180)
        self.course = Entry(Frame_register, font=("Goudy old style", 15), bg="#E7E6E6")
        self.course.place(x=170, y=180, width=240, height=30)

        lbl_idnum = Label(Frame_register, text="ID Number:", font=("Goudy old style", 15, "bold"), fg="grey",
                          bg="white").place(x=5, y=240)
        self.idnum = Entry(Frame_register, font=("Goudy old style", 15), bg="#E7E6E6")
        self.idnum.place(x=170, y=240, width=240, height=30)

        lbl_pic = Label(Frame_register, text="Photo:", font=("Goudy old style", 15, "bold"), fg="grey",
                        bg="white").place(x=5, y=300)
        btn_pic = Button(Frame_register, text="Open File", command=open).place(x=70, y=300, width=150, height=40)

        face = Button(Frame_register, text="Verify Identity", bd=0,
                      font=("Goudy old style", 15, "bold"), bg="green", fg="black").place(x=5, y=360, width=150,
                                                                                          height=40)
        submit = Button(Frame_register, text="Register", bd=0,
                        font=("Goudy old style", 15, "bold"), bg="green", fg="white").place(x=150, y=440, width=150,
                                                                                            height=40)



root=Tk()
obj = Register(root)
root.mainloop()