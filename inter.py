import serial
import time
from tkinter import *
import pyrebase
top=Tk()
def n4():
    def n5():
        pass

    r1=StringVar()
    l1=Label(top,text=" Water Threshold").place(x=50,y=250)
    e1=Entry(top,textvariable=r1).place(x=150,y=250)
    l2 = Label(top,text= "Temperature Threshold").place(x=20, y=300)
    r2=StringVar()
    e2=Entry(top,textvariable=r2).place(x=150,y=300)
    l2 = Label(top, text="Moisture Threshold").place(x=30, y=400)
    r3 = StringVar()
    e3 = Entry(top, textvariable=r3).place(x=150,y=400)
    l1=Button(top,text="OK",command=n5).place(x=200,y=600)
def n7():
    pass
def n8():
    pass
def n9():
    b3=Button()
    B1=Button(top,text="ON",bg="green",width=10,height=10).place(x=300,y=300)
    B1 =Button(top, text="ON", bg="red", width=10, height=10).place(x=400, y=300)
def n10():
    B2=Button(top,text="ON",bg="green",width=10,height=10).place(x=500,y=300)
    B2 = Button(top, text="OFF", bg="red", width=10, height=10).place(x=600, y=300)
def n11():
    B3 = Button(top, text="ON", bg="green", width=10, height=10).place(x=700, y=300)
    B3= Button(top, text="Off", bg="red", width=10, height=10).place(x=800, y=300)
def n12():
    B4 = Button(top, text="ON", bg="green", width=10, height=10).place(x=900, y=300)
    B4= Button(top, text="OFF", bg="red", width=10, height=10).place(x=1000, y=300)
menubar=Menu(top)
file=Menu(menubar,tearoff=0)
file.add_command(label="Dadhboard")
file.add_command(label="Status")
file.add_command(label="Settings",command=n4)
menubar.add_cascade(label="FILE",menu=file)
Advance=Menu(menubar,tearoff=0)
Advance.add_command(label="Messages",command=n7)
Advance.add_command(label="User Manuel",command=n8)
menubar.add_cascade(label="ADVANCE",menu=Advance)
manual1=Menu(menubar,tearoff=0)
manual1.add_command(label="LIGHT",command=n9)
manual1.add_command(label="MOTOR",command=n10)
manual1.add_command(label="FAN",command=n11)
manual1.add_command(label="EXHAUST FAN",command=n12)
menubar.add_cascade(label="MANUAL",menu=manual1)
top.config(menu=menubar)
top.mainloop()