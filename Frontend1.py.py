import math
from tkinter import *
import serial
import time
import pyrebase
top=Tk()
width,height=700,610
d=str(width) + "x" + str(height)
top.geometry(d)
my1=Canvas(top,width=width-50,height=height-50,bg="white")
my1.grid(column=0,row=0)
my2=Canvas(top,width=width-50,height=height-50,bg="white")
my2.grid(column=10,row=0)
arc_w=30
x1,y1,x2,y2=40,40,560,560
x,y,r=300,295,220
c1=my1.create_arc(x1,y1,x2,y2,start=0,extent=45,outline="blue",width=arc_w,style=ARC)
c2=my1.create_arc(x1,y1,x2,y2,start=45,extent=45,outline="violet",width=arc_w,style=ARC)
c2=my1.create_arc(x1,y1,x2,y2,start=90,extent=50,outline="brown",width=arc_w,style=ARC)
c2=my1.create_arc(x1,y1,x2,y2,start=140,extent=40,outline="yellow",width=arc_w,style=ARC)
in_radian=math.radians(0)
pointer=my1.create_line(x,y,(x+r*math.cos(in_radian)),(y-r*math.sin(in_radian)),width=6,arrow="last")
v6=my1.create_text(460,50,text=" MORE WET")
v6=my1.create_text(600,200,text=" LIGHT WET")
v6=my1.create_text(200,20,text=" MORE DRY")
v6=my1.create_text(40,150,text=" LIGHT DRY")
v7=my1.create_text(300,500,text="WATER CONTENT")
x1,y1,x2,y2=40,40,560,560
x,y,r=300,295,220
c1=my2.create_arc(x1,y1,x2,y2,start=0,extent=45,outline="lightyellow",width=arc_w,style=ARC)
c2=my2.create_arc(x1,y1,x2,y2,start=45,extent=45,outline="yellow",width=arc_w,style=ARC)
c2=my2.create_arc(x1,y1,x2,y2,start=90,extent=50,outline="orange",width=arc_w,style=ARC)
c2=my2.create_arc(x1,y1,x2,y2,start=140,extent=40,outline="red",width=arc_w,style=ARC)
in_radian1=math.radians(0)
pointer1=my2.create_line(x,y,(x+r*math.cos(in_radian1)),(y-r*math.sin(in_radian1)),width=6,arrow="last")
v6=my2.create_text(500,40,text="MODERATE")
v6=my2.create_text(600,200,text="LIGHT")
v6=my2.create_text(200,20,text="HIGH")
v6=my2.create_text(40,150,text="ABNORMAL")
v7=my2.create_text(300,500,text="TEMPERATURE")
def my_up(*args):
    global pointer
    in_radian=math.radians(my_scale.get())
    val1=my_scale.get()
    my1.delete(pointer)
    l1.config(text=val1)
    pointer=my1.create_line(x,y,(x+r*math.cos(in_radian)),(y-r*math.sin(in_radian)),width=6,arrow="last")



my_scale=Scale(top,from_=0,to=180,length=300,command=my_up,orient="horizontal")
my_scale.grid(row=2,column=10)
def my_up1(*args):
    global pointer1
    in_radian1=math.radians(my_scale1.get())
    val1=my_scale1.get()
    my2.delete(pointer1)
    pointer1=my2.create_line(x,y,(x+r*math.cos(in_radian1)),(y-r*math.sin(in_radian1)),width=6,arrow="last")



my_scale1=Scale(top,from_=0,to=180,length=300,command=my_up1,orient="horizontal")
my_scale1.grid(row=1,column=10)
l1=Label(top)
l1.grid(column=0,row=3)

top.mainloop()