import tkinter
from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter import messagebox as mess
from tkinter import ttk
import tkinter.simpledialog as tsd
import os
import io
import cv2
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.messagebox
import mysql.connector
import face_recognition
from datetime import datetime
from PIL import ImageFile, Image , ImageTk
ImageFile.LOAD_TRUNCATED_IMAGES = True
from datetime import datetime
now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
# connecting to the database
connectiondb = mysql.connector.connect(host="localhost", user="root", passwd="", database="facerecognation")
cursordb = connectiondb.cursor()

# Login page------------------------------------------------------------------
def login():

    global root
    root = Toplevel(root)
    root.title("Login Form")
    root.geometry("800x400+300+150")
    root.resizable(False, False)

    root.bg = PhotoImage(file="images/bg.png")
    bg_image = Label(root, bg="green", image=root.bg).place(x=200, y=0, relwidth=1, relheight=1)

    site = Frame(root, bg="white")
    site.place(x=0, y=0, width=400, height=400)

    title = Label(root, text="Login Here", font=("Impact", 35, "bold"), fg="#000", bg="white").place(x=80,
                                                                                                     y=20)

    global username_verification
    global password_verification,lbl_user

    username_verification = StringVar()
    password_verification = StringVar()
    lbl_user = Label(root, text="Username:", font=("Goudy old style", 15, "bold"), fg="grey",bg="white").place(x=30, y=130)
    lbl_user = Entry(root, font=("Goudy old style", 15), bg="#E7E6E6", textvariable=username_verification)
    lbl_user.place(x=130, y=130, width=220, height=35)


    lbl_password = Label(root, text="Password:", font=("Goudy old style", 15, "bold"), fg="grey",bg="white").place(x=30, y=210)
    lbl_password = Entry(root, font=("Goudy old style", 15), bg="#E7E6E6", show='*', textvariable=password_verification)
    lbl_password.place(x=130, y=210, width=220, height=35)

    Button(root, text="Login",relief="groove", font=("Goudy old style", 15, "bold"),bg="green", fg="white",
       command=login_verification).place(x=120, y=330, width=150, height=40)

def login_verification():
    user_verification = username_verification.get()
    pass_verification = password_verification.get()
    sql = "select * from user_acct where usrname = %s and paswrd = %s"
    cursordb.execute(sql, [(user_verification), (pass_verification)])
    results = cursordb.fetchall()
    if results:
        for i in results:
            conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="facerecognation")
            cursor = conn.cursor()
            user_verification = lbl_user.get()
            data = "insert into historylog(id, student, Course$Section, profile_photo)" \
                   " select id, student, Course$Section, profile_photo from user_acct where usrname = %s "
            cursor.execute(data, [(user_verification)])

            data1 = "insert into timein(timein) values (%s)"

            cursor.execute(data1, [(formatted_date)])
            conn.commit()

            logged()

    else:
        failed()


#destroy message---------------------------------------------------

def logged_destroy():
    logged.destroy()


    root.destroy()


def failed_destroy():
    failed_message.destroy()


def toggle_win():
    f1 = Frame(root, width=200, height=650, bg='#1a301f')
    f1.place(x=0, y=0)



def failed():
    global failed_message
    failed_message = Toplevel(root)
    failed_message.title("Invalid Message")
    failed_message.geometry("500x100+470+260")
    Label(failed_message, text="Invalid Username or Password", fg="red", font="bold").pack()
    Label(failed_message, text="").pack()
    Button(failed_message, text="Ok", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),
       command=failed_destroy).pack()

def Exit():
    wayOut = tkinter.messagebox.askyesno("Login System", "Do you want to exit the system")

    if wayOut > 0:
        root.destroy()
        return

def on_closing():
    if mess.askyesno("Quit", "You are exiting window.Do you want to quit?"):
        window.destroy()




# attendance==========================================================================
def logged():
    def regester():
        global lbl_user2
        window3 = tkinter.Toplevel()
        window3.title("Registration Form")
        window3.geometry("850x600+250+20")
        window3.resizable(False, False)
        def updatebtn():
            mydb = mysql.connector.connect(
                host="localhost", user="root", passwd="", database="facerecognation"
            )
            mycursor = mydb.cursor()
            root = Tk()
            root.title("User Data")
            root.geometry("450x300")
            label = Label(root, text=lbl_user2.get(), width=20, height=2,fg="black",font=("Times New Roman", 12, "bold")).grid(row=0, column=1)
            label1 = Label(root, text="ID NUMBER", width=20, height=2).grid(row=1, column=0)
            label2 = Label(root, text="NAME", width=20, height=2).grid(row=2, column=0)
            label3 = Label(root, text="COURSE & SECTION", width=20, height=2).grid(row=3, column=0)
            label4 = Label(root, text="USERNAME", width=20, height=2).grid(row=4, column=0)
            label5 = Label(root, text="PASSWORD", width=20, height=2).grid(row=5, column=0)

            label8 = Label(root, width=10, height=2).grid(row=7, column=2)
            label9 = Label(root, width=10, height=2).grid(row=7, column=4)
            label10 = Label(root, width=10, height=2).grid(row=7, column=6)
            label11 = Label(root, width=10, height=2).grid(row=7, column=8)

            user2_verification2 = lbl_user2.get()
            sql = "SELECT * FROM user_acct where  usrname = %s "
            mycursor.execute(sql, [(user2_verification2)])
            results = mycursor.fetchall()
            for student in results:
                e1 = Entry(root, width=30, borderwidth=8, text=student[1])
                e1.grid(row=1, column=1)
                e2 = Entry(root, width=30, borderwidth=8, text=student[2])
                e2.grid(row=2, column=1)
                e3 = Entry(root, width=30, borderwidth=8, text=student[3])
                e3.grid(row=3, column=1)
                e4 = Entry(root, width=30, borderwidth=8, text=student[4])
                e4.grid(row=4, column=1)
                e5 = Entry(root, width=30, borderwidth=8, text=student[5])
                e5.grid(row=5, column=1)

            def Update():
                RollNo = e1.get()
                First_Name = e2.get()
                Last_Name = e3.get()
                Phone_Number = e4.get()
                City = e5.get()

                Update = "Update user_acct set student='%s', Course$Section='%s', usrname='%s', paswrd='%s' where id='%s'" % (
                First_Name, Last_Name, Phone_Number, City, RollNo)
                mycursor.execute(Update)
                mydb.commit()
                e1.delete(0, 'end')
                e2.delete(0, 'end')
                e3.delete(0, 'end')
                e4.delete(0, 'end')
                e5.delete(0, 'end')
            button3 = Button(root, text="Update", width=10, height=2, command=Update).grid(row=6, column=1)
        def deletebtn():
            global delete
            delete = tkinter.Toplevel()
            delete.title("Delete Record")
            delete.geometry("400x200+470+130")
            delete.resizable(False, False)
            title2 = Label(delete, text="Are you sure to delete record?", font=("Impact", 20, "bold"), fg="#000",
                           bg="white").place(
                x=20, y=30)
            buttonyes = Button(delete, text="Yes", font=("Impact", 20, "bold"), fg="white",
                           bg="blue", command=yesbth)
            buttonyes.place(x=100, y=150, width=100, height=30)
            buttonno = Button(delete, text="No", font=("Impact", 20, "bold"), fg="white",
                           bg="blue", command=nobtn)
            buttonno.place(x=200, y=150, width=100, height=30)

        def yesbth():
            mydb = mysql.connector.connect(
                host="localhost", user="root", passwd="", database="facerecognation"
            )
            mycursor = mydb.cursor()

            dele = lbl_user2.get()



            sql = "DELETE FROM user_acct WHERE usrname = '%s'" % (dele)

            mycursor.execute(sql)

            mydb.commit()


            delete.destroy()
        def nobtn():
            delete.destroy()
        def show():

            History = tkinter.Toplevel()
            History.title("Login History")
            History.geometry("400x450+470+130")
            History.resizable(False, False)
            History.bg = ImageTk.PhotoImage(file="images/2.jpg")
            button3 = Button(History, text="Update", width=10, height=2, command=updatebtn)
            button3.place(x=260, y=330)
            button4 = Button(History, text="Delete", width=10, height=2, command=deletebtn)
            button4.place(x=260, y=290)
            siteimg = Frame(History, bg="#061421")
            siteimg.place(x=100, y=150, width=150, height=150)
            sitetext = Frame(History, bg="white")
            sitetext.place(x=100, y=300, width=150, height=100)

            title = Label(History, text="User Admin Details", bg="#061421", fg="white",
                          font=("Times New Roman", 30, "bold")).place(x=21, y=0)
            user2_verification2 = lbl_user2.get()
            sql = "SELECT * FROM user_acct where  usrname = %s "
            cursordb.execute(sql, [(user2_verification2)])
            results = cursordb.fetchall()
            for student in results:
                stream = io.BytesIO(student[6])
                img = Image.open(stream)
                img = ImageTk.PhotoImage(img)
                e = Label(sitetext, bg='white', font=("TImes New Roman", 15, "bold"), text=student[2])
                e.place(x=20, y=10)
                e1 = Label(sitetext, bg='white', font=("TImes New Roman", 15, "bold"), text=student[1])
                e1.place(x=40, y=40)
                e2 = Label(sitetext, bg='white', font=("TImes New Roman", 15, "bold"), text=student[3])
                e2.place(x=30, y=70)
                e3 = Label(siteimg, bg='white', image=img)
                e3.place(x=0, y=0)
            History.mainloop()


        def upload_file():
            global filename, img
            f_types = [('Png files', '.png'), ('Jpg Files', '.jpg')]
            filename = filedialog.askopenfilename(filetypes=f_types)
            img = ImageTk.PhotoImage(file=filename)
            b2 = tk.Button(Frame_register1, image=img)
            b2.grid(row=4, column=1, columnspan=2)

        def add_data():  # Add data to MySQL table+
            if window3.fname.get() == "" or window3.course.get() == "" or window3.idnum.get() == "" or window3.usern.get() =="" or window3.passw.get() =="":
                messagebox.showerror("warning", "All fields are required to fill!", parent=Frame_register)
            else:
                global img, filename
                fob = open(filename, 'rb')  # filename from upload_file()
                fob = fob.read()
                data = (window3.idnum.get(), window3.fname.get(), window3.course.get(), window3.usern.get(), window3.passw.get(), fob)  # tuple with data
                conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="facerecognation")
                cursor = conn.cursor()
                sql = ("INSERT INTO  user_acct(id,student,Course$Section,usrname,paswrd,profile_photo) "
                       "VALUES (%s,%s,%s,%s,%s,%s)")
                try:
                    # executing the sql command
                    cursor.execute(sql, data)
                    conn.commit()
                    messagebox.showinfo("success", "Registered Successfully!", parent=Frame_register)
                    window3.fname.delete(0, 'end')
                    window3.course.delete(0, 'end')
                    window3.idnum.delete(0, 'end')
                    window3.usern.delete(0, 'end')
                    window3.passw.delete(0, 'end')
                    Frame_register1.delete(0, 'end')



                except:
                    conn.rollback()

        window3.left = ImageTk.PhotoImage(file="images/bg.png")
        left = Label(window3, bg="green", image=window3.left).place(x=0, y=0, width=420, height=600)
        show = Button(window3, text="Show Details", bd=5, command=show,
                      font=("Goudy old style", 15, "bold"), bg="green", fg="black").place(x=10, y=15, width=150,height=40)
        Frame_register2 = Frame(window3, bg="white")
        Frame_register2.place(x=170, y=15, width=220, height=35)

        Frame_register = Frame(window3, bg="white")
        Frame_register.place(x=420, y=0, width=550, height=600)
        Frame_register1 = Frame(Frame_register, bg="black")
        Frame_register1.place(x=220, y=390, width=150, height=150)
        title2 = Label(window3,text="Please input username.", font=("Impact", 10, "bold"), fg="#000", bg="white").place(
            x=170, y=0)

        lbl_user2 = Entry(Frame_register2, font=("Goudy old style", 15), bg="#E7E6E6")
        lbl_user2.place(x=0, y=0, width=220, height=35)

        title = Label(Frame_register, text="Register Here", font=("Impact", 35, "bold"), fg="#000", bg="white").place(x=75,y=10)

        lbl_user = Label(Frame_register, text="Full Name:", font=("Goudy old style", 15, "bold"), fg="grey",
                         bg="white").place(x=5, y=110)
        window3.fname = Entry(Frame_register, font=("Goudy old style", 15), bg="#E7E6E6")
        window3.fname.place(x=170, y=110, width=240, height=30)

        lbl_course = Label(Frame_register, text="Course & Section:", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(x=5, y=170)
        window3.course = Entry(Frame_register, font=("Goudy old style", 15), bg="#E7E6E6")
        window3.course.place(x=170, y=170, width=240, height=30)

        lbl_idnum = Label(Frame_register, text="ID Number:", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(x=5, y=230)
        window3.idnum = Entry(Frame_register, font=("Goudy old style", 15), bg="#E7E6E6")
        window3.idnum.place(x=170, y=230, width=240, height=30)

        lbl_usern = Label(Frame_register, text="Username:", font=("Goudy old style", 15, "bold"), fg="grey",
                         bg="white").place(x=5, y=290)
        window3.usern = Entry(Frame_register, font=("Goudy old style", 15), bg="#E7E6E6")
        window3.usern.place(x=170, y=290, width=240, height=30)

        lbl_passw = Label(Frame_register, text="Password:", font=("Goudy old style", 15, "bold"), fg="grey",
                         bg="white").place(x=5, y=350)
        window3.passw = Entry(Frame_register, show="*", font=("Goudy old style", 15), bg="#E7E6E6")
        window3.passw.place(x=170, y=350, width=240, height=30)

        window3.btn_pic = Button(Frame_register, text="Upload File", command= upload_file,
                        font=("Goudy old style", 15, "bold"), bg="green", fg="black").place(x=5, y=420, width=150, height=40)

        submit = Button(Frame_register, text="Register", bd=5, command= add_data,
                        font=("Goudy old style", 15, "bold"), bg="green", fg="black").place(x=145, y=550, width=150,height=40)

    def contact():
        master1 = tkinter.Tk()
        master1.geometry("350x200+500+250")
        master1.resizable(False, False)
        master1.title("Contact")
        master1.configure(background="white")
        lbl3 = tkinter.Label(master1, text='Facebook Account:', fg="#0961ed", bg='white', font=('times', 12, ' bold ')).place(x=10,
                                                                                                                  y=10)
        lbl4 = tkinter.Label(master1, text='Jay Montejo Sajulga', bg='white', font=('times', 12, ' bold ')).place(x=60, y=30)
        lbl5 = tkinter.Label(master1, text='Jessa Christine Bagongon Pejer', bg='white', font=('times', 12, ' bold ')).place(x=60,y=50)
        lbl6 = tkinter.Label(master1, text='Claire Ann Dedal', bg='white',font=('times', 12, ' bold ')).place(x=60, y=70)
        lbl7 = tkinter.Label(master1, text='Carlyl Stephen Manzanares Clerino', bg='white', font=('times', 12, ' bold ')).place(x=60,
                                                                                                               y=90)
        lbl8 = tkinter.Label(master1, text='Contact Number:', fg="#0961ed", bg='white', font=('times', 12, ' bold ')).place(x=10,
                                                                                                               y=110)
        lbl9 = tkinter.Label(master1, text='09631845435', bg='white',  font=('times', 12, ' bold ')).place(x=60,
                                                                                                               y=130)



    def about():
        window = tkinter.Toplevel()
        window.title("About")
        window.geometry("550x270+380+220")
        window.configure(bg="#1eb332")
        window.resizable(False, False)
        labl = Label(window, bg="#1eb332", text="Face recognition is one of the computer vision",
                     font=('Times New Roman', 11, 'bold')).place(x=120, y=10)
        labl = Label(window, bg="#1eb332", text="topics that has gotten a lot of attention over the last decade. Many researchers",
                     font=('Times New Roman', 11, 'bold')).place(x=15, y=30)
        labl = Label(window, bg="#1eb332", text="have contributed to the development and improvement of innovative computer",
                      font=('Times New Roman', 11, 'bold')).place(x=15, y=50)
        labl = Label(window, bg="#1eb332", text="vision theories, as well as the use of these ideas in real-world applications.",
                     font=('Times New Roman', 11, 'bold')).place(x=15, y=70)
        labl = Label(window, bg="#1eb332", text="Several studies on face recognition have been published, with the goal of",
                     font=('Times New Roman', 11, 'bold')).place(x=15, y=90)
        labl = Label(window, bg="#1eb332", text="developing methods to detect the presence of faces and recognize it. The study",
                     font=('Times New Roman', 11, 'bold')).place(x=15, y=110)
        labl = Label(window, bg="#1eb332", text="conduces to clarify the obstacles of detection and identification and introduce an",
                     font=('Times New Roman', 11, 'bold')).place(x=15, y=130)
        labl = Label(window, bg="#1eb332", text="explication that able to develop a new recognition system method for both",
                     font=('Times New Roman', 11, 'bold')).place(x=15, y=150)
        labl = Label(window, bg="#1eb332", text="circumstances.",
                     font=('Times New Roman', 11, 'bold')).place(x=230, y=170)
        labl = Label(window, bg="#1eb332", text="The main goal of the study is to develop a system that uses facial recognition",
                     font=('Times New Roman', 11, 'bold')).place(x=15, y=190)
        labl = Label(window, bg="#1eb332", text="technology to simplify and automate the process of registering and tracking",
                     font=('Times New Roman', 11, 'bold')).place(x=15, y=210)
        labl = Label(window, bg="#1eb332", text="students' attendance.",
                     font=('Times New Roman', 11, 'bold')).place(x=210, y=230)

    def assure_path_exists(path):
        dir = os.path.dirname(path)
        if not os.path.exists(dir):
            os.makedirs(dir)

    # check for haarcascade file
    def check_haarcascadefile():
        exists = os.path.isfile("haarcascade_frontalface_default.xml")
        if exists:
            pass
        else:
            mess._show(title='fechar file missing', message='some file is missing.Please contact me for help')
            window.destroy()

    def save_pass():
        assure_path_exists("Pass_Train/")
        exists1 = os.path.isfile("Pass_Train\pass.txt")
        if exists1:
            tf = open("Pass_Train\pass.txt", "r")
            str = tf.read()
        else:
            master.destroy()
            new_pas = tsd.askstring('Password not set', 'Please enter a new password below', show='*')
            if new_pas == None:
                mess._show(title='Null Password Entered', message='Password not set.Please try again!')
            else:
                tf = open("Pass_Train\pass.txt", "w")
                tf.write(new_pas)
                mess._show(title='Password Registered!', message='New password was registered successfully!')
                return
        op = (old.get())
        newp = (new.get())
        nnewp = (nnew.get())
        if (op == str):
            if (newp == nnewp):
                txf = open("Pass_Train\pass.txt", "w")
                txf.write(newp)
            else:
                mess._show(title='Error', message='Confirm new password again!!!')
                return
        else:
            mess._show(title='Wrong Password', message='Please enter correct old password.')
            return
        mess._show(title='Password Changed', message='Password changed successfully!!')
        master.destroy()

    def change_pass():
        global master
        master = tkinter.Tk()
        master.geometry("400x160")
        master.resizable(False, False)
        master.title("Change Admin Password")
        master.configure(background="white")
        lbl4 = tkinter.Label(master, text='    Enter Old Password', bg='white', font=('times', 12, ' bold '))
        lbl4.place(x=10, y=10)
        global old
        old = tkinter.Entry(master, width=25, fg="black", relief='solid', font=('times', 12, ' bold '), show='*')
        old.place(x=180, y=10)
        lbl5 = tkinter.Label(master, text='   Enter New Password', bg='white', font=('times', 12, ' bold '))
        lbl5.place(x=10, y=45)
        global new
        new = tkinter.Entry(master, width=25, fg="black", relief='solid', font=('times', 12, ' bold '), show='*')
        new.place(x=180, y=45)
        lbl6 = tkinter.Label(master, text='Confirm New Password', bg='white', font=('times', 12, ' bold '))
        lbl6.place(x=10, y=80)
        global nnew
        nnew = tkinter.Entry(master, width=25, fg="black", relief='solid', font=('times', 12, ' bold '), show='*')
        nnew.place(x=180, y=80)
        cancel = tkinter.Button(master, text="Cancel", command=master.destroy, fg="white", bg="#13059c", height=1,
                                width=25, activebackground="white", font=('times', 10, ' bold '))
        cancel.place(x=200, y=120)
        save1 = tkinter.Button(master, text="Save", command=save_pass, fg="black", bg="#00aeff", height=1, width=25,
                               activebackground="white", font=('times', 10, ' bold '))
        save1.place(x=10, y=120)
        master.mainloop()

    def TrackImages():
        check_haarcascadefile()
        assure_path_exists("Attendance/")
        assure_path_exists("StudentDetails/")
        for k in tb.get_children():
            tb.delete(k)
        msg = ''
        i = 0
        j = 0
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        exists3 = os.path.isfile("Pass_Train\Trainner.yml")
        if exists3:
            recognizer.read("Pass_Train\Trainner.yml")
        else:
            mess._show(title='Data Missing', message='Please click on Save Profile to reset data!!')
            return
        harcascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath);

        cam = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX
        col_names = ['Id', 'Name', 'Course', 'Date', 'Time']
        exists1 = os.path.isfile("StudentDetails\StudentDetails.csv")
        if exists1:
            df = pd.read_csv("StudentDetails\StudentDetails.csv")
        else:
            mess._show(title='Details Missing', message='Students details are missing, please check!')
            cam.release()
            cv2.destroyAllWindows()
            window.destroy()
        while True:
            ret, im = cam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.2, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
                serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
                if (conf < 50):
                    ts = time.time()
                    date = datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                    timeStamp = datetime.fromtimestamp(ts).strftime('%H:%M:%S')

                    cc = df.loc[df['SERIAL NO.'] == serial]['COURSE'].values
                    aa = df.loc[df['SERIAL NO.'] == serial]['NAME'].values
                    ID = df.loc[df['SERIAL NO.'] == serial]['ID'].values
                    ID = str(ID)
                    ID = ID[1:-1]
                    bb = str(aa)
                    bb = bb[2:-2]
                    dd = str(cc)
                    dd = dd[3:-3]
                    cv2.putText(im, f"COURSE: {dd} ", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(im, f"ID NUMBER:: {ID} ", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    attendance = [str(ID), bb, dd, str(date), str(timeStamp)]

                else:
                    Id = 'Unknown'
                    bb = str(Id)
                cv2.putText(im, str(bb), (x, y + h), font, 1, (0, 251, 255), 2)
            cv2.imshow('Taking Attendance', im)
            if (cv2.waitKey(1) == ord('q')):
                break
        ts = time.time()
        date = datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
        exists = os.path.isfile("Attendance\Attendance_" + date + ".csv")
        if exists:
            with open("Attendance\Attendance_" + date + ".csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(attendance)
            csvFile1.close()
        else:
            with open("Attendance\Attendance_" + date + ".csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(col_names)
                writer.writerow(attendance)
            csvFile1.close()
        with open("Attendance\Attendance_" + date + ".csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for lines in reader1:
                i = i + 1
                if (i > 1):
                    if (i % 2 != 0):
                        iidd = str(lines[0]) + '   '
                        tb.insert('', 0, text=iidd, values=(str(lines[1]), str(lines[2]), str(lines[3]), str(lines[4])))
        csvFile1.close()
        cam.release()
        cv2.destroyAllWindows()

        # Back End
        # Front End
    def logout():
        main_display()
        window1.destroy()

    def history():
        History = tkinter.Toplevel()
        History.title("Login History")
        History.geometry("800x450+270+130")
        History.resizable(False, False)
        History.bg = ImageTk.PhotoImage(file="images/2.jpg")
        bg = Label(History, image=History.bg).place(x=0, y=0, relwidth=1, relheight=1)
        time1 = Label(History, text="Time In:", fg="white", bg="black", font=("TImes New Roman", 15, "bold"))
        time1.place(x=260, y=330)
        time = Label(History, text=formatted_date, fg="white", bg="black", font=("TImes New Roman", 15, "bold"))
        time.place(x=260, y=350)

        site = Frame(History, bg="#061421")
        site.place(x=450, y=0, width=400, height=450)
        site1 = Frame(site, bg="#061421")
        site1.place(x=0, y=80, width=200, height=300)
        site2 = Frame(site, bg="#061421")
        site2.place(x=200, y=80, width=200, height=300)
        siteimg = Frame(History, bg="#061421")
        siteimg.place(x=100, y=150, width=150, height=150)
        sitetext = Frame(History, bg="white")
        sitetext.place(x=100, y=300, width=150, height=100)

        title = Label(site, text="Recent Logged In", bg="#061421", fg="white",
                      font=("Times New Roman", 30, "bold")).place(x=21, y=0)

        def ok():
            History.destroy()

        bttn = Button(site, text="OK", bg="white", bd=8, command=ok, fg="black",
                      font=("TImes New Roman", 15, "bold")).place(x=130, y=410, width=100, height=30)

        cursordb.execute("SELECT student FROM historylog limit 0,10")

        i = 1  # data starts from row 1

        for student1 in cursordb:
            for j in range(len(student1)):
                e = Entry(site1, width=20, fg='black', font=("TImes New Roman", 15, "bold"), )
                e.grid(row=i, column=j)
                e.insert(END, student1[j])
            i = i + 1
        cursordb.execute("SELECT timein FROM timein limit 0,10")

        i1 = 1  # data starts from row 1

        for student2 in cursordb:
            for j in range(len(student2)):
                e = Entry(site2, width=20, fg='black', font=("TImes New Roman", 15, "bold"), )
                e.grid(row=i1, column=j)
                e.insert(END, student2[j])
            i1 = i1 + 1

        user_verification = lbl_user.get()
        sql = "SELECT * FROM user_acct where  usrname = %s "
        cursordb.execute(sql, [(user_verification)])
        results = cursordb.fetchall()
        for student in results:
            stream = io.BytesIO(student[6])
            img = Image.open(stream)
            img = ImageTk.PhotoImage(img)
            e = Label(sitetext, bg='white', font=("TImes New Roman", 15, "bold"), text=student[2])
            e.place(x=20, y=10)
            e1 = Label(sitetext, bg='white', font=("TImes New Roman", 15, "bold"), text=student[1])
            e1.place(x=40, y=40)
            e2 = Label(sitetext, bg='white', font=("TImes New Roman", 15, "bold"), text=student[3])
            e2.place(x=30, y=70)
            e3 = Label(siteimg, bg='white', image=img)
            e3.place(x=0, y=0)
        History.mainloop()




    root.deiconify()
    global window

    window = tkinter.Toplevel()
    window.title("Face Recognition Based Attendance System")
    window.geometry("1280x720+35+10")
    window.pack_propagate(False)
    window.resizable(False, False)
    # window.configure(background='red')
    window.bg = ImageTk.PhotoImage(file="images/5.jpg")
    bg = Label(window, image=window.bg).place(x=0, y=0, relwidth=1, relheight=1)
    menubar = Menu(window)
    help = Menu(menubar, tearoff=0)
    help.add_command(label="Change Password!", command=change_pass)
    help.add_command(label="Contact Us", command=contact)


    help.add_separator()

    menubar.add_cascade(label="Help", menu=help)

    menubar.add_command(label="About", command=about)
    menubar.add_command(label="History Log", command=history)
    menubar.add_command(label="Register", command=regester)
    root.withdraw()
    menubar.add_command(label="Logout", command=window.destroy)
    window.config(menu=menubar)

    frame2 = tkinter.Frame(window, bg="black")
    frame2.place(relx=0.01, rely=0.15, relwidth=0.50, relheight=0.70)
    #  file view==========================================

    frame3 = tk.LabelFrame(window, text="Excel Data")
    frame3.place(relx=0.51, rely=0.19, relwidth=0.48, relheight=0.52)
    fr_head3 = tkinter.Label(window, text="Student's attendance Report", fg="white", bg="black",font=('times', 17, ' bold '))
    fr_head3.place(relx=0.51, rely=0.15, relwidth=.50)
    # Frame for open file dialog
    file_frame = tk.LabelFrame(window, text="Open File")
    file_frame.place(relx=0.51, rely=0.70, relwidth=0.48, relheight=0.15)



    # The file/file path text
    label_file = ttk.Label(file_frame, text="Browse file")
    label_file.place(rely=0, relx=0)

    ## Treeview Widget
    tv1 = ttk.Treeview(frame3)
    tv1.place(relheight=1, relwidth=1)  # set the height and width of the widget to 100% of its container (frame1).

    treescrolly = tk.Scrollbar(frame3, orient="vertical",
                               command=tv1.yview)  # command means update the yaxis view of the widget
    treescrollx = tk.Scrollbar(frame3, orient="horizontal",
                               command=tv1.xview)  # command means update the xaxis view of the widget
    tv1.configure(xscrollcommand=treescrollx.set,
                  yscrollcommand=treescrolly.set)  # assign the scrollbars to the Treeview Widget
    treescrollx.pack(side="bottom", fill="x")  # make the scrollbar fill the x axis of the Treeview widget
    treescrolly.pack(side="right", fill="y")  # make the scrollbar fill the y axis of the Treeview widget

    def File_dialog():
        """This Function will open the file explorer and assign the chosen file path to label_file"""
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select A File",
                                              filetype=(("xlsx files", "*.xlsx"), ("All Files", "*.*")))
        label_file["text"] = filename
        return None

    def Load_excel_data():

        """If the file selected is valid this will load the file into the Treeview"""
        file_path = label_file["text"]
        try:
            excel_filename = r"{}".format(file_path)
            if excel_filename[-4:] == ".csv":
                df = pd.read_csv(excel_filename)
            else:
                df = pd.read_excel(excel_filename)

        except ValueError:
            tk.messagebox.showerror("Information", "The file you have chosen is invalid")
            return None
        except FileNotFoundError:

            tk.messagebox.showerror("Information", f"No such file as {file_path}")

            return None

        clear_data()
        tv1["column"] = list(df.columns)
        tv1["show"] = "headings"
        for column in tv1["columns"]:
            tv1.heading(column, text=column)

        df_rows = df.to_numpy().tolist()  # turns the dataframe into a list of lists
        for row in df_rows:
            tv1.insert("", "end",
                       values=row)  # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
        return None

    def clear_data():
        tv1.delete(*tv1.get_children())
        return None



    fr_head2 = tkinter.Label(frame2, text="Current Student's attendance", fg="white", bg="black",
                             font=('times', 17, ' bold '))
    fr_head2.place(x=0, y=0, relwidth=1)
    trackImg = tkinter.Button(window, text="Register Student", command=regerterstudent, fg="black", bg="#00aeff", height=1,
                              activebackground="white", font=('times', 16, ' bold '))
    trackImg.place(x=30, y=10, relwidth=0.29)

    trackImg = tkinter.Button(window, text="Take Attendance", command=TrackImages, fg="black", bg="#00aeff", height=1,
                              activebackground="white", font=('times', 16, ' bold '))
    trackImg.place(x=30, y=60, relwidth=0.29)
    # Buttons
    buttonA = tk.Button(file_frame, text="Browse A File", activebackground="white", fg="white", bg="#13059c",font=('times', 16, ' bold '),
                        command=lambda: File_dialog())
    buttonA.place(rely=0.55, relx=0.20, relwidth=0.25)

    buttonB = tk.Button(file_frame, text="Load File", activebackground="white", fg="white", bg="#13059c", font=('times', 16, ' bold '),
                        command=lambda: Load_excel_data())
    buttonB.place(rely=0.55, relx=0.02, relwidth=0.19)
    quitWindow = tkinter.Button(frame2, text="Quit", command=window.destroy, fg="white", bg="#13059c", width=35,
                                height=1, activebackground="white", font=('times', 16, ' bold '))
    quitWindow.place(x=0, y=450, relwidth=0.19)

    # Display total registration----------

    global tb
    # Attandance table----------------------------
    style = ttk.Style()
    style.configure("mystyle.Treeview", highlightthickness=0, bd=2, font=('Calibri', 11))
    style.configure("mystyle.Treeview.Heading", font=('times', 13, 'bold'))
    style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])
    tb = ttk.Treeview(frame2, height=20, columns=('name', 'course', 'date', 'time'), style="mystyle.Treeview")
    tb.column('#0', width=52)
    tb.column('name', width=150)
    tb.column('course', width=150)
    tb.column('date', width=150)
    tb.column('time', width=150)
    tb.grid(row=2, column=0, padx=(0, 0), pady=(30, 0), columnspan=8)
    tb.heading('#0', text='ID')
    tb.heading('name', text='NAME')
    tb.heading('course', text='Course/Section')
    tb.heading('date', text='DATE')
    tb.heading('time', text='TIME')



#register=============================================================================


global  window1
def regerterstudent():
    def closeregester():
        window1.destroy()
    def clear():
        txt.delete(0, 'end')
        txt2.delete(0, 'end')
        txt3.delete(0, 'end')
        res = "1)Take Images  ===> 2)Save Profile"
        message1.configure(text=res)

    def assure_path_exists(path):
        dir = os.path.dirname(path)
        if not os.path.exists(dir):
            os.makedirs(dir)

    def check_haarcascadefile():
        exists = os.path.isfile("haarcascade_frontalface_default.xml")
        if exists:
            pass
        else:
            mess._show(title='fechar file missing', message='some file is missing.Please contact me for help')
            window.destroy()
        master = tkinter.Tk()
        master.geometry("400x160")
        master.resizable(False, False)

    def change_pass():
        global master

        master.title("Change Admin Password")
        master.configure(background="white")
        lbl4 = tkinter.Label(master, text='Enter Old Password', bg='white', font=('times', 12, ' bold '))
        lbl4.place(x=10, y=10)
        global old
        old = tkinter.Entry(master, width=25, fg="black", relief='solid', font=('times', 12, ' bold '), show='*')
        old.place(x=180, y=10)
        lbl5 = tkinter.Label(master, text='   Enter New Password', bg='white', font=('times', 12, ' bold '))
        lbl5.place(x=10, y=45)
        global new
        new = tkinter.Entry(master, width=25, fg="black", relief='solid', font=('times', 12, ' bold '), show='*')
        new.place(x=180, y=45)
        lbl6 = tkinter.Label(master, text='Confirm New Password', bg='white', font=('times', 12, ' bold '))
        lbl6.place(x=10, y=80)
        global nnew
        nnew = tkinter.Entry(master, width=25, fg="black", relief='solid', font=('times', 12, ' bold '), show='*')
        nnew.place(x=180, y=80)
        cancel = tkinter.Button(master, text="Cancel", command=master.destroy, fg="white", bg="#13059c", height=1,
                                width=25, activebackground="white", font=('times', 10, ' bold '))
        cancel.place(x=200, y=120)
        save1 = tkinter.Button(master, text="Save", command=save_pass, fg="black", bg="#00aeff", height=1, width=25,
                               activebackground="white", font=('times', 10, ' bold '))
        save1.place(x=10, y=120)
        master.mainloop()


    def save_pass():
        assure_path_exists("Pass_Train/")
        exists1 = os.path.isfile("Pass_Train\pass.txt")
        if exists1:
            tf = open("Pass_Train\pass.txt", "r")
            str = tf.read()
        else:
            master.destroy()
            new_pas = tsd.askstring('Password not set', 'Please enter a new password below', show='*')
            if new_pas == None:
                mess._show(title='Null Password Entered', message='Password not set.Please try again!')
            else:
                tf = open("Pass_Train\pass.txt", "w")
                tf.write(new_pas)
                mess._show(title='Password Registered!', message='New password was registered successfully!')
                return
        op = (old.get())
        newp = (new.get())
        nnewp = (nnew.get())
        if (op == str):
            if (newp == nnewp):
                txf = open("Pass_Train\pass.txt", "w")
                txf.write(newp)
            else:
                mess._show(title='Error', message='Confirm new password again!!!')
                return
        else:
            mess._show(title='Wrong Password', message='Please enter correct old password.')
            return
        mess._show(title='Password Changed', message='Password changed successfully!!')
        master.destroy()

    def psw():
        assure_path_exists("Pass_Train/")
        exists1 = os.path.isfile("Pass_Train\pass.txt")
        if exists1:
            tf = open("Pass_Train\pass.txt", "r")
            str_pass = tf.read()
        else:
            new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
            if new_pas == None:
                mess._show(title='No Password Entered', message='Password not set!! Please try again')
            else:
                tf = open("Pass_Train\pass.txt", "w")
                tf.write(new_pas)
                mess._show(title='Password Registered', message='New password was registered successfully!!')
                return
        password = tsd.askstring('Password', 'Enter Password', show='*')
        if (password == str_pass):
            TrainImages()

        elif (password == None):
            pass
        else:
            mess._show(title='Wrong Password', message='You have entered wrong password')



        messagebox.showinfo("success", "Profile Saved Successfully!", parent=window1)
        txt.delete(0, 'end')
        txt2.delete(0, 'end')
        txt3.delete(0, 'end')



    # $$$$$$$$$$$$$
    def TakeImages():
        check_haarcascadefile()
        columns = ['SERIAL NO.', 'ID', 'NAME', 'COURSE']
        assure_path_exists("StudentDetails/")
        assure_path_exists("TrainingImage/")
        serial = 0
        exists = os.path.isfile("StudentDetails\StudentDetails.csv")
        if exists:
            with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
                reader1 = csv.reader(csvFile1)
                for l in reader1:
                    serial = serial + 1
            serial = (serial // 2)
            csvFile1.close()
        else:
            with open("StudentDetails\StudentDetails.csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(columns)
                serial = 1
            csvFile1.close()
        Id = (txt.get())
        name = (txt2.get())
        course = (txt3.get())
        if ((name.isalpha()) or (' ' in name)):
            cam = cv2.VideoCapture(0)
            harcascadePath = "haarcascade_frontalface_default.xml"
            detector = cv2.CascadeClassifier(harcascadePath)
            sampleNum = 0
            while (True):
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.05, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    # incrementing sample number
                    sampleNum = sampleNum + 1
                    # saving the captured face in the dataset folder TrainingImage
                    cv2.imwrite("TrainingImage\ " + course + "." + str(serial) + "." + name + "." + str(serial) + "." + Id + '.' + str(sampleNum) + ".jpg",
                                gray[y:y + h, x:x + w])
                    # display the frame
                    cv2.imshow('Taking Images', img)
                # wait for 100 miliseconds
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
                # break if the sample number is morethan 100
                elif sampleNum > 50:
                    break
            cam.release()
            cv2.destroyAllWindows()
            res = "Images Taken for ID : " + Id
            row = [serial, Id, name, course]
            with open('StudentDetails\StudentDetails.csv', 'a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
            csvFile.close()
            message1.configure(text=res)
        else:
            if (name.isalpha() == False):
                res = "Enter Correct name"
                message1.configure(text=res)

    ########################################################################################
    # $$$$$$$$$$$$$
    def TrainImages():
        check_haarcascadefile()
        assure_path_exists("Pass_Train/")
        recognizer = cv2.face_LBPHFaceRecognizer.create()
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        faces, ID = getImagesAndLabels("TrainingImage")
        try:
            recognizer.train(faces, np.array(ID))
        except:
            mess._show(title='No Registrations', message='Please Register someone first!!!')
            return
        recognizer.save("Pass_Train\Trainner.yml")
        res = "Profile Saved Successfully"
        message1.configure(text=res)
        message1.configure(text='Total Registrations till now  : ' + str(ID[0]))

    ############################################################################################3
    # $$$$$$$$$$$$$
    def getImagesAndLabels(path):
        # get the path of all the files in the folder
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        # create empty face list
        faces = []
        # create empty ID list
        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting it to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            ID = int(os.path.split(imagePath)[-1].split(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(ID)
        return faces, Ids


        clear_data()
        tv1["column"] = list(df.columns)
        tv1["show"] = "headings"
        for column in tv1["columns"]:
            tv1.heading(column, text=column)

        df_rows = df.to_numpy().tolist()  # turns the dataframe into a list of lists
        for row in df_rows:
            tv1.insert("", "end",
                       values=row)  # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
        return None



    window1 = tkinter.Toplevel()
    window1.title("Face Recognition Based Attendance System")
    window1.geometry("1280x720+35+10")
    window1.resizable(False, False)
    window1.bg = ImageTk.PhotoImage(file="images/5.jpg")
    bg = Label(window1, image=window1.bg).place(x=0, y=0, relwidth=1, relheight=1)


    trackImg = tkinter.Button(window1, text="Return", command=closeregester, fg="black", bg="#00aeff", height=1,
                              activebackground="white", font=('times', 16, ' bold '))
    trackImg.place(x=30, y=10, relwidth=0.10)

    frame1 = tkinter.Frame(window1, bg="white")
    frame1.place(relx=0.01, rely=0.15, relwidth=0.49, relheight=0.75)

    fr_head1 = tkinter.Label(frame1, text="Register New Student", fg="white", bg="black", font=('times', 17, ' bold '))
    fr_head1.place(x=0, y=0, relwidth=1)

    # frame5 = tkinter.Frame(window1, bg="white")
    # frame5.place(relx=0.50, rely=0.15, relwidth=0.49, relheight=0.75)
    #
    # fr_head5 = tkinter.Label(frame5, text="Registered Student's", fg="white", bg="black", font=('times', 17, ' bold '))
    # fr_head5.place(x=0, y=0, relwidth=1)


    message0 = tkinter.Label(frame1, text="Follow the steps..", bg="white", fg="black", width=39, height=1,
                             font=('times', 16, ' bold '))
    message0.place(x=7, y=275)


    clearButton = tkinter.Button(frame1, text="Clear", command=clear, fg="white", bg="blue", width=11,
                                 activebackground="white", font=('times', 12, ' bold '))
    clearButton.place(x=55, y=230, relwidth=0.29)

    takeImg = tkinter.Button(frame1, text="Train Images", command=TakeImages, fg="black", bg="#00aeff", width=34,
                             height=1, activebackground="white", font=('times', 16, ' bold '))
    takeImg.place(x=30, y=350, relwidth=0.30)
    trainImg = tkinter.Button(frame1, text="Save New Profile", command=psw, fg="black", bg="#00aeff", width=34, height=1,
                              activebackground="white", font=('times', 16, ' bold '))
    trainImg.place(x=30, y=430, relwidth=0.30)
 # registretion frame
    lbl=  tkinter.Label(frame1, text="Enter ID:", font=("Goudy old style", 15, "bold"), fg="grey",
          bg="white")
    lbl.place(x=3, y=35)

    txt = tkinter.Entry(frame1, width=32, fg="black", bg="#e1f2f2", highlightcolor="#00aeff", highlightthickness=3,
                        font=('times', 15, ' bold '))
    txt.place(x=55, y=58, relwidth=0.75)

    lbl2 = tkinter.Label(frame1, text="Enter Name:", font=("Goudy old style", 15, "bold"), fg="grey",
                        bg="white")
    lbl2.place(x=3, y=90)

    txt2 = tkinter.Entry(frame1, width=32, fg="black", bg="#e1f2f2", highlightcolor="#00aeff", highlightthickness=3,
                         font=('times', 15, ' bold '))
    txt2.place(x=55, y=123, relwidth=0.75)

    lbl3 = tkinter.Label(frame1, text="Enter Course & Section:", font=("Goudy old style", 15, "bold"), fg="grey",
                        bg="white")
    lbl3.place(x=3, y=160)

    txt3 = tkinter.Entry(frame1, width=32, fg="black", bg="#e1f2f2", highlightcolor="#00aeff", highlightthickness=3,
                         font=('times', 15, ' bold '))
    txt3.place(x=55, y=193, relwidth=0.75)

    message1 = tkinter.Label(frame1, text="1)Take Images  ===> 2)Save Profile", bg="white", fg="black", width=39,
                         height=1, activebackground="yellow", font=('times', 15, ' bold '))
    message1.place(x=7, y=300)

    message2 = tkinter.Label(frame1, text="", bg="white", fg="black", width=39, height=1, activebackground="yellow",
                        font=('times', 16, ' bold '))
    message2.place(x=7, y=500)
    res = 0
    exists = os.path.isfile("StudentDetails\StudentDetails.csv")
    if exists:
        with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for l in reader1:
                res = res + 1
        res = (res // 2) - 1
        csvFile1.close()
    else:
        res = 0
    message2.configure(text='Total Registrations : ' + str(res))

    #  file view==========================================

    frame3 = tk.LabelFrame(window1, text="Excel Data")
    frame3.place(relx=0.50, rely=0.19, relwidth=0.48, relheight=0.58)
    fr_head3 = tkinter.Label(window1, text="Regestered Student", fg="white", bg="black",
                             font=('times', 17, ' bold '))
    fr_head3.place(relx=0.50, rely=0.15, relwidth=.50)
    # Frame for open file dialog
    file_frame = tk.LabelFrame(window1, text="File Path")
    file_frame.place(relx=0.50, rely=0.75, relwidth=0.48, relheight=0.15)

    # The file/file path text
    label_file = ttk.Label(file_frame, text="D:/Face-Recognition-Based-Attendance-System-main/StudentDetails/StudentDetails.csv")
    label_file.place(rely=0, relx=0)

    ## Treeview Widget
    tv1 = ttk.Treeview(frame3)
    tv1.place(relheight=1, relwidth=1)  # set the height and width of the widget to 100% of its container (frame1).

    treescrolly = tk.Scrollbar(frame3, orient="vertical",
                               command=tv1.yview)  # command means update the yaxis view of the widget
    treescrollx = tk.Scrollbar(frame3, orient="horizontal",
                               command=tv1.xview)  # command means update the xaxis view of the widget
    tv1.configure(xscrollcommand=treescrollx.set,
                  yscrollcommand=treescrolly.set)  # assign the scrollbars to the Treeview Widget
    treescrollx.pack(side="bottom", fill="x")  # make the scrollbar fill the x axis of the Treeview widget
    treescrolly.pack(side="right", fill="y")  # make the scrollbar fill the y axis of the Treeview widget

    def File_dialog():
        """This Function will open the file explorer and assign the chosen file path to label_file"""
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select A File",
                                              filetype=(("xlsx files", "*.xlsx"), ("All Files", "*.*")))
        label_file["text"] = filename
        return None

    def Load_excel_data():

        """If the file selected is valid this will load the file into the Treeview"""
        file_path = label_file["text"]
        try:
            excel_filename = r"{}".format(file_path)
            if excel_filename[-4:] == ".csv":
                df = pd.read_csv(excel_filename)
            else:
                df = pd.read_excel(excel_filename)

        except ValueError:
            tk.messagebox.showerror("Information", "The file you have chosen is invalid")
            return None
        except FileNotFoundError:

            tk.messagebox.showerror("Information", f"No such file as {file_path}")

            return None

        clear_data()
        tv1["column"] = list(df.columns)
        tv1["show"] = "headings"
        for column in tv1["columns"]:
            tv1.heading(column, text=column)

        df_rows = df.to_numpy().tolist()  # turns the dataframe into a list of lists
        for row in df_rows:
            tv1.insert("", "end",
                       values=row)  # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
        return None

    def clear_data():
        tv1.delete(*tv1.get_children())
        return None



    # Buttons
    buttonA = tk.Button(file_frame, text="", activebackground="white", fg="white", bg="#13059c",
                        font=('times', 0, ' bold '),
                        command=lambda: File_dialog())
    buttonA.place(rely=0.55, relx=0.20, relwidth=0)

    buttonB = tk.Button(file_frame, text="Load File", activebackground="white", fg="white", bg="#13059c",
                        font=('times', 16, ' bold '),
                        command=lambda: Load_excel_data())
    buttonB.place(rely=0.55, relx=0.02, relwidth=0.19)

def main_display():
    global root
    root = Tk()
    site = Frame(root, bg="green").place(x=0, y=0, relwidth=1, relheight=1)
    root.title("Login System")
    root.geometry("500x500+400+100")
    root.resizable(False, False)
    root.subimg = ImageTk.PhotoImage(file="images/bg.png")
    subimg = Label(root, bg="#26382b", image=root.subimg).place(x=0, y=40, width=500, height=500)

    Label(root, text='Welcome to Log In System', bd=20, font=('arial', 20, 'bold'), relief="groove", fg="white",
      bg="green", width=300).pack()
    Label(root, text="").pack()
    Button(root, text='Log In', height="1", width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
       bg="green", command=login).pack()
    Label(root, text="").pack()

    Button(root, text="Exit", relief="groove", bd=8, font=("Goudy old style", 15, "bold"), bg="green", fg="white",
           command=Exit).pack()
    Label(root, text="").pack()









main_display()
root.mainloop()