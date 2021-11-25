from tkinter import *
import tkinter as tk
from tkinter import font
from tkinter.font import BOLD, ITALIC
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
from PIL import ImageTk, Image
import random
from twilio.rest import Client

window = Tk()
window.title("LOTUS addmission management system")
window.state("zoomed")
#window.configure(bg="white")
frame8=Frame(window,bd=6,bg="grey")
frame9=Frame(window,bd=6,bg="grey")

def frame8_dashboard():
    frame8.place(x=360,y=87)
    Label(frame8,text="",width=220,height=60).pack()
    Dash_l1 = Label(frame8,text="Dashboard",font=("nunito-sans sans-serif",22))
    Dash_l1.place(x=15,y=10)
    
    Button(frame8,text="Admission Application User-Guide",width = 30,height = 1,bg="#337ab7",fg="white",font = ("nunito-sans",12,),borderwidth=0).place(x=1250,y=20)
    Dash_l2 = Label(frame8,text="Kindly verify the eligibility of the programme from the university website before taking admission.",font=("nunito-sans sans-serif",16))
    Dash_l2.place(x=350,y=70)

def frame9_Form():
    options =[
        "10th",
        "12th",
        "Degree or cerificate",
        "Graduation",
        "Post Graduation",
        "Ph.D",
    ]
    ten_op = [
        " a ",
        " b ",
        " c ",
    ]
    inter_op = [
        " d ",
        " e ",
        " f ",
    ]
    Degree_op = [
        " g ",
        " h ",
        " i ",
    ]
    Grad_op = [
        " j ",
        " k ",
        " L ",
    ]
    Post_op = [
        " M ",
        " N ",
        " o ",
    ]
    phd_op = [
        " p ",
        " q ",
        " r ",
    ]
    def qual(e):
        if mycombo.get() == "10th":
            color_combo.config(value=ten_op)
            color_combo.current(0)
        if mycombo.get() == "inter_op":
            color_combo.config(value=inter_op)
            color_combo.current(0)
        if mycombo.get() == "Degree_op":
            color_combo.config(value=Degree_op)
            color_combo.current(0)
        if mycombo.get() == "Grad_op":
            color_combo.config(value=Grad_op)
            color_combo.current(0)
        if mycombo.get() == "Post_op":
            color_combo.cofig(value=Post_op)
            color_combo.current(0)
        if mycombo.get() == "phd_op":
            color_combo.config(value=phd_op)
            color_combo.current(0)

    frame9.place(x=360,y=87)
    Label(frame9,text="",width=220,height=60).pack()
    Dash_l1 = Label(frame9,text="All Aplication Form(s)",font=("nunito-sans sans-serif",21))
    Dash_l1.place(x=15,y=10)
    
    Button(frame9,text="Admission Application User-Guide",width = 30,height = 1,bg="#337ab7",fg="white",font = ("nunito-sans",12,),borderwidth=0).place(x=1250,y=20)
    Dash_l2 = Label(frame9,text="Kindly verify the eligibility of the programme from the university website before taking admission.",font=("nunito-sans sans-serif",16))
    Dash_l2.place(x=350,y=70)

    Label(frame9,text="",width = 216,height=5,bg="#d9d9d9").place(x=13,y=105)
    
    mycombo = ttk.Combobox(frame9,value=options,width=22,font=("sans-serif",17))
    mycombo.set("Select Form Qualification")
    mycombo.place(x=25,y=130)
    mycombo.bind("<<ComboboxSelected>>", qual)
    
    color_combo = ttk.Combobox(frame9, value=[" "])
    color_combo.current(0)
    color_combo.bind("<<ComboboxSelected>>")
    color_combo.place(x=50,y=130)


screen_width = window.winfo_screenwidth()
Main_bar = Label(window,text="",bg="white",width=screen_width,height=5)
Main_bar.place(x=0,y=4)

click_btn= PhotoImage(file=r"D:\LPU 3rd sem\INT-213\python_project\Univhomelogo .png")
img_label = Label(image=click_btn)
btn7 = Button(window, image=click_btn,width=195,height=80,borderwidth=0,bg="white")
btn7.place(x=1,y=3)

Side_bar = Label(window,text="",bg="#2c333a",width=50,height=80)
#Side_bar.configure(bg="#2c333a")
Side_bar.place(x=0,y=87)

Side_bar_label1 =Button(window,text="Dashboard",command=frame8_dashboard,bg="#2c333a",fg="white",height=1,font=(" nunito-sans sans-serif",16),borderwidth=0) 
Side_bar_label1.place(x=20,y=93)

Side_bar_label2 =Button(window,text="All Application Form(s)",command = frame9_Form,bg="#2c333a",fg="white",height=1,font=(" nunito-sans sans-serif",16),borderwidth=0) 
Side_bar_label2.place(x=20,y=146)

Side_bar_label3 =Button(window,text="My Profile",bg="#2c3338",fg="white",height=1,font=(" nunito-sans sans-serif",16),borderwidth=0) 
Side_bar_label3.place(x=20,y=199)

Side_bar_label4 =Button(window,text="My Queries",bg="#2c3338",fg="white",height=1,font=(" nunito-sans sans-serif",16),borderwidth=0) 
Side_bar_label4.place(x=20,y=252)

Side_bar_label5 =Button(window,text="My Communication",bg="#2c3338",fg="white",height=1,font=(" nunito-sans sans-serif",16),borderwidth=0) 
Side_bar_label5.place(x=20,y=305)

Side_bar_label6 =Button(window,text="My Payments",bg="#2c3338",fg="white",height=1,font=(" nunito-sans sans-serif",16),borderwidth=0) 
Side_bar_label6.place(x=20,y=358)

Side_bar_label7 =Button(window,text="Logout",bg="#2c3338",fg="white",height=1,font=(" nunito-sans sans-serif",16),borderwidth=0) 
Side_bar_label7.place(x=20,y=411)


canvas=Canvas(window,width=352,height=-3,bg="grey",borderwidth=0)
canvas.place(x=0,y=140)
canvas.create_line(0,10,300,10,fill="grey",width=0)

canvas1=Canvas(window,width=352,height=-3,bg="grey",borderwidth=0)
canvas1.place(x=0,y=193)
canvas1.create_line(0,10,300,10,fill="grey",width=0)

canvas2=Canvas(window,width=352,height=-3,bg="grey",borderwidth=0)
canvas2.place(x=0,y=246)
canvas2.create_line(0,10,300,10,fill="grey",width=0)

canvas3=Canvas(window,width=352,height=-3,bg="grey",borderwidth=0)
canvas3.place(x=0,y=299)
canvas3.create_line(0,10,300,10,fill="grey",width=0)

canvas4=Canvas(window,width=352,height=-3,bg="grey",borderwidth=0)
canvas4.place(x=0,y=352)
canvas4.create_line(0,10,300,10,fill="grey",width=0)

canvas5=Canvas(window,width=352,height=-3,bg="grey",borderwidth=0)
canvas5.place(x=0,y=405)
canvas5.create_line(0,10,300,10,fill="grey",width=0)

canvas6=Canvas(window,width=352,height=-3,bg="grey",borderwidth=0)
canvas6.place(x=0,y=458)
canvas6.create_line(0,10,300,10,fill="grey",width=0)

window.mainloop()