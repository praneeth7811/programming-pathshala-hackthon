from tkinter import *
import tkinter as tk
from tkinter import font
from tkinter import messagebox
from tkinter.font import BOLD, ITALIC
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
from PIL import ImageTk, Image
import random
from twilio.rest import Client

frame7 = Tk()
frame7.title("LOTUS addmission management system")
frame7.state("zoomed")

frame8=Frame(frame7,bd=6,bg="grey")
frame9=Frame(frame7,bd=6,bg="grey")
frame10=Frame(frame7,bd=6,bg="grey")
frame11=Frame(frame7,bd=6,bg="grey")
frame12=Frame(frame7,bd=6,bg="grey")
frame13=Frame(frame7,bd=6,bg="grey")
frame14=Frame(frame7,bd=6,bg="grey")

def frame8_dashboard():
    frame8.place(x=360,y=87)
    Label(frame8,text="",width=220,height=60).pack()
    Dash_l1 = Label(frame8,text="Dashboard",font=("nunito-sans sans-serif",22))
    Dash_l1.place(x=15,y=10)
    
    Button(frame8,text="Admission Application User-Guide",width = 30,height = 1,bg="#337ab7",fg="white",font = ("nunito-sans",12,),borderwidth=0).place(x=1250,y=20)
    Dash_l2 = Label(frame8,text="Kindly verify the eligibility of the programme from the university website before taking admission.",font=("nunito-sans sans-serif",16))
    Dash_l2.place(x=350,y=70)

    Label(frame8,text="",width=68,height=6,bg = "#f68220").place(x=15,y=120)
    Label(frame8,text="NO",bg="#f68220",fg="white",font=("sans-serif",36)).place(x=20,y=125)
    Label(frame8,text="Application(s) In Progress",bg="#f68220",fg="white",font=("sans-serif",16)).place(x=20,y=180)

    Label(frame8,text="",width=68,height=6,bg = "#f68220").place(x=515,y=120)
    Label(frame8,text="NO",bg="#f68220",fg="white",font=("sans-serif",36)).place(x=520,y=125)
    Label(frame8,text="Application(s) Completed",bg="#f68220",fg="white",font=("sans-serif",16)).place(x=520,y=180)

    Label(frame8,text="",width=68,height=6,bg = "#f68220").place(x=1015,y=120)
    Label(frame8,text="NO",bg="#f68220",fg="white",font=("sans-serif",36)).place(x=1020,y=125)
    Label(frame8,text="Application(s) In Progress",bg="#f68220",fg="white",font=("sans-serif",16)).place(x=1020,y=180)

    Label(frame8,text="",width=211,height=2,bg="white").place(x=15,y=240)
    Label(frame8,text="",width=-2,height=2,bg="#666666").place(x=15,y=240)
    Label(frame8,text="Application Form",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",13)).place(x=30,y=245)
    Label(frame8,text="",width=0,height=2,bg="#666666").place(x=515,y=240)
    Label(frame8,text="Application No.",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",13)).place(x=530,y=245)
    Label(frame8,text="",width=0,height=2,bg="#666666").place(x=785,y=240)
    Label(frame8,text="Date",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",13)).place(x=800,y=245)
    Label(frame8,text="",width=0,height=2,bg="#666666").place(x=1015,y=240)
    Label(frame8,text="Action",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",13)).place(x=1040,y=245)
    Label(frame8,text="",width=-10,height=2,bg="#666666").place(x=1200,y=240)
    
def frame9_Form():
    frame9.place(x=360,y=87)
    Label(frame9,text="",width=220,height=60).pack()
    Dash_l1 = Label(frame9,text="All Aplication Form(s)",font=("nunito-sans sans-serif",21))
    Dash_l1.place(x=15,y=10)
    
    Button(frame9,text="Admission Application User-Guide",width = 30,height = 1,bg="#337ab7",fg="white",font = ("nunito-sans",12,),borderwidth=0).place(x=1250,y=20)
    Dash_l2 = Label(frame9,text="Kindly verify the eligibility of the programme from the university website before taking admission.",font=("nunito-sans sans-serif",16))
    Dash_l2.place(x=350,y=70)

    Label(frame9,text="",width=215,height=10,bg = "#d9d9d9").place(x=15,y=115)

    Label(frame9,text="",width=215,height=2,bg="white").place(x=15,y=115)
    Label(frame9,text="",width=0,height=2,bg="#666666").place(x=15,y=115)
    Label(frame9,text="Application Form",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",13)).place(x=30,y=120)
    Label(frame9,text="",width=0,height=2,bg="#666666").place(x=515,y=115)
    Label(frame9,text="Application No.",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",13)).place(x=530,y=120)
    Label(frame9,text="",width=0,height=2,bg="#666666").place(x=785,y=115)
    Label(frame9,text="Date",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",13)).place(x=800,y=120)
    Label(frame9,text="",width=0,height=2,bg="#666666").place(x=1015,y=115)
    Label(frame9,text="Action",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",13)).place(x=1040,y=120)
    Label(frame9,text="",width=0,height=2,bg="#666666").place(x=1250,y=115)
    
    Label(frame9,text="Application Form",fg="#d11f51",font=("Nutino Sans,sans-serif",12)).place(x=15,y=285)

    Label(frame9,text="",width=215,height=5,bg="white").place(x=15,y=315)
    Label(frame9,text="",width=0,height=5,bg="#d11f51").place(x=15,y=315)
    Label(frame9,text="LITE Test | B-tech - 2022",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",13)).place(x=30,y=340)
    Label(frame9,text="",width=0,height=5,bg="#666666").place(x=515,y=315)
    Label(frame9,text=" - ",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",16,BOLD)).place(x=650,y=340)
    Label(frame9,text="",width=0,height=5,bg="#666666").place(x=785,y=315)
    Label(frame9,text=" - ",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",16,BOLD)).place(x=880,y=340)
    Label(frame9,text="",width=0,height=5,bg="#666666").place(x=1015,y=315)
    Button(frame9,text=" Apply For LITE Test",bg="#f68220",fg="white",font=("Nutino Sans,sans-serif",10,BOLD)).place(x=1060,y=340)
    Label(frame9,text="",width=0,height=5,bg="#666666").place(x=1250,y=315)

    Label(frame9,text="",width=215,height=6,bg="white").place(x=15,y=430)
    Label(frame9,text="",width=0,height=6,bg="#d11f51").place(x=15,y=430)
    Label(frame9,text="LITE Test | B-tech - 2022",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",13)).place(x=30,y=455)
    Label(frame9,text="",width=0,height=6,bg="#666666").place(x=515,y=430)
    Label(frame9,text=" - ",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",16,BOLD)).place(x=650,y=455)
    Label(frame9,text="",width=0,height=6,bg="#666666").place(x=785,y=430)
    Label(frame9,text=" - ",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",16,BOLD)).place(x=880,y=455)
    Label(frame9,text="",width=0,height=6,bg="#666666").place(x=1015,y=430)
    Button(frame9,text=" Take Admission",bg="#f68220",fg="white",font=("Nutino Sans,sans-serif",10,BOLD)).place(x=1080,y=450)
    Button(frame9,text=" Apply For LITE Test",bg="#f68220",fg="white",font=("Nutino Sans,sans-serif",10,BOLD)).place(x=1070,y=485)
    Label(frame9,text="",width=0,height=6,bg="#666666").place(x=1250,y=430)

def frame10_profile():
    frame10.place(x=360,y=87)
    Label(frame10,text="",width=220,height=60).pack()
    Dash_l1 = Label(frame10,text="My Profile",font=("nunito-sans sans-serif",21))
    Dash_l1.place(x=15,y=10)
    
    Button(frame10,text="Admission Application User-Guide",width = 30,height = 1,bg="#337ab7",fg="white",font = ("nunito-sans",12,),borderwidth=0).place(x=1250,y=20)
    Dash_l2 = Label(frame10,text="Kindly verify the eligibility of the programme from the university website before taking admission.",font=("nunito-sans sans-serif",16))
    Dash_l2.place(x=350,y=70)

    Label(frame10,text="",width=215,height=15,bg = "#d9d9d9").place(x=15,y=115)
    Label(frame10,text="your documents are still in the process of Verification \n This tab will update your deatils after verification of your documents",
                                            bg = "#d9d9d9",fg="#666666",font=("Nutino Sans,sans-serif",18)).place(x=420,y=200)


def frame11_quires():
    frame11.place(x=360,y=87)
    Label(frame11,text="",width=220,height=60).pack()
    Dash_l1 = Label(frame11,text="My Quires",font=("nunito-sans sans-serif",21))
    Dash_l1.place(x=15,y=10)
    
    Button(frame11,text="Admission Application User-Guide",width = 30,height = 1,bg="#337ab7",fg="white",font = ("nunito-sans",12,),borderwidth=0).place(x=1250,y=20)
    Dash_l2 = Label(frame11,text="Kindly verify the eligibility of the programme from the university website before taking admission.",font=("nunito-sans sans-serif",16))
    Dash_l2.place(x=350,y=70)

    Label(frame11,text="",width=215,height=10,bg = "#d9d9d9").place(x=15,y=130)

    Label(frame11,text="",width=215,height=2,bg="white").place(x=15,y=130)
    Label(frame11,text="",width=0,height=2,bg="#666666").place(x=15,y=130)
    Label(frame11,text="Query",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",13)).place(x=30,y=135)
    Label(frame11,text="",width=0,height=2,bg="#666666").place(x=515,y=130)
    Label(frame11,text="Category",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",13)).place(x=530,y=135)
    Label(frame11,text="",width=0,height=2,bg="#666666").place(x=785,y=130)
    Label(frame11,text="Date",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",13)).place(x=800,y=135)
    Label(frame11,text="",width=0,height=2,bg="#666666").place(x=1015,y=130)
    Label(frame11,text="Status",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",13)).place(x=1030,y=135)
    Label(frame11,text="",width=-10,height=2,bg="#666666").place(x=1200,y=130)
    Label(frame11,text="Feedback",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",13)).place(x=1215,y=135)

    Label(frame11,text="you haven't raised any queries yet",bg = "#d9d9d9",fg="#666666",font=("Nutino Sans,sans-serif",18)).place(x=600,y=200)

def frame12_Communication():
    frame12.place(x=360,y=87)
    Label(frame12,text="",width=220,height=60).pack()
    Dash_l1 = Label(frame12,text="My Communication(s)",font=("nunito-sans sans-serif",21))
    Dash_l1.place(x=15,y=10)
    
    Button(frame12,text="Admission Application User-Guide",width = 30,height = 1,bg="#337ab7",fg="white",font = ("nunito-sans",12,),borderwidth=0).place(x=1250,y=20)
    Dash_l2 = Label(frame12,text="Kindly verify the eligibility of the programme from the university website before taking admission.",font=("nunito-sans sans-serif",16))
    Dash_l2.place(x=350,y=70)

    Label(frame12,text="",width=215,height=15,bg = "#d9d9d9").place(x=15,y=115)
    Label(frame12,text="We will Communicate you soon...",
                                            bg = "#d9d9d9",fg="#666666",font=("Nutino Sans,sans-serif",18)).place(x=420,y=200)

def frame13_pay():
    frame13.place(x=360,y=87)
    Label(frame13,text="",width=220,height=60).pack()
    Dash_l1 = Label(frame13,text="My Payments(s)",font=("nunito-sans sans-serif",21))
    Dash_l1.place(x=15,y=10)
    
    Button(frame13,text="Admission Application User-Guide",width = 30,height = 1,bg="#337ab7",fg="white",font = ("nunito-sans",12,),borderwidth=0).place(x=1250,y=20)
    Dash_l2 = Label(frame13,text="Kindly verify the eligibility of the programme from the university website before taking admission.",font=("nunito-sans sans-serif",16))
    Dash_l2.place(x=350,y=70)

    Label(frame13,text="",width=215,height=50,bg = "#d9d9d9").place(x=15,y=115)

    Label(frame13,text="",width=215,height=5,bg="white").place(x=15,y=115)
    Label(frame13,text="",width=0,height=5,bg="#d11f51").place(x=15,y=115)
    Label(frame13,text="Pay Now And\n Book your Seat in LIT",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",16)).place(x=30,y=120)
    Label(frame13,text="",width=0,height=5,bg="#666666").place(x=460,y=115)
    Label(frame13,text=" Fee For Seat Conformation \n 9000 ",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",16,BOLD)).place(x=490,y=120)
    Label(frame13,text="",width=0,height=5,bg="#666666").place(x=785,y=115)
    Label(frame13,text=" Appliation Charge \n 1000 ",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",16,BOLD)).place(x=800,y=120)
    Label(frame13,text="",width=0,height=5,bg="#666666").place(x=1015,y=115)
    Label(frame13,text=" Total Fee to pay\n 10,000 ",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",16,BOLD)).place(x=1040,y=120)
    Label(frame13,text="",width=0,height=5,bg="#666666").place(x=1250,y=115)
    Button(frame13,text=" Pay Now",bg="#f68220",fg="white",font=("Nutino Sans,sans-serif",14,BOLD)).place(x=1320,y=135)
    Button(frame13,text=" Pay Total Fee",bg="#f68220",fg="white",font=("Nutino Sans,sans-serif",14,BOLD)).place(x=1330,y=815)

def frame14_logout():
    exit = messagebox.askquestion("LOG OUT","Are You Sure You Want To Logout",icon='warning')
    if exit == 'yes':
        frame7.destroy()
    else:
        messagebox.showinfo('Return','You Will Now Return To The Aplication Screen')

screen_width = frame7.winfo_screenwidth()
Main_bar = Label(frame7,text="",bg="white",width=screen_width,height=5)
Main_bar.place(x=0,y=4)

click_btn= PhotoImage(file=r"D:\LPU 3rd sem\INT-213\python_project\Univhomelogo .png")
img_label = Label(image=click_btn)
btn7 = Button(frame7, image=click_btn,width=195,height=80,borderwidth=0,bg="white")
btn7.place(x=1,y=3)

Side_bar = Label(frame7,text="",bg="#2c333a",width=50,height=80)
#Side_bar.configure(bg="#2c333a")
Side_bar.place(x=0,y=87)

Side_bar_label1 =Button(frame7,text="Dashboard",command=frame8_dashboard,bg="#2c333a",fg="white",height=1,font=(" nunito-sans sans-serif",16),borderwidth=0) 
Side_bar_label1.place(x=20,y=93)

Side_bar_label2 =Button(frame7,text="All Application Form(s)",command = frame9_Form,bg="#2c333a",fg="white",height=1,font=(" nunito-sans sans-serif",16),borderwidth=0) 
Side_bar_label2.place(x=20,y=146)

Side_bar_label3 =Button(frame7,text="My Profile",command = frame10_profile,bg="#2c3338",fg="white",height=1,font=(" nunito-sans sans-serif",16),borderwidth=0) 
Side_bar_label3.place(x=20,y=199)

Side_bar_label4 =Button(frame7,text="My Queries",command = frame11_quires,bg="#2c3338",fg="white",height=1,font=(" nunito-sans sans-serif",16),borderwidth=0) 
Side_bar_label4.place(x=20,y=252)

Side_bar_label5 =Button(frame7,text="My Communication",command = frame12_Communication,bg="#2c3338",fg="white",height=1,font=(" nunito-sans sans-serif",16),borderwidth=0) 
Side_bar_label5.place(x=20,y=305)

Side_bar_label6 =Button(frame7,text="My Payments",command = frame13_pay,bg="#2c3338",fg="white",height=1,font=(" nunito-sans sans-serif",16),borderwidth=0) 
Side_bar_label6.place(x=20,y=358)

Side_bar_label7 =Button(frame7,text="Logout",command = frame14_logout,bg="#2c3338",fg="white",height=1,font=(" nunito-sans sans-serif",16),borderwidth=0) 
Side_bar_label7.place(x=20,y=411)


canvas=Canvas(frame7,width=352,height=-3,bg="grey",borderwidth=0)
canvas.place(x=0,y=140)
canvas.create_line(0,10,300,10,fill="grey",width=0)

canvas1=Canvas(frame7,width=352,height=-3,bg="grey",borderwidth=0)
canvas1.place(x=0,y=193)
canvas1.create_line(0,10,300,10,fill="grey",width=0)

canvas2=Canvas(frame7,width=352,height=-3,bg="grey",borderwidth=0)
canvas2.place(x=0,y=246)
canvas2.create_line(0,10,300,10,fill="grey",width=0)

canvas3=Canvas(frame7,width=352,height=-3,bg="grey",borderwidth=0)
canvas3.place(x=0,y=299)
canvas3.create_line(0,10,300,10,fill="grey",width=0)

canvas4=Canvas(frame7,width=352,height=-3,bg="grey",borderwidth=0)
canvas4.place(x=0,y=352)
canvas4.create_line(0,10,300,10,fill="grey",width=0)

canvas5=Canvas(frame7,width=352,height=-3,bg="grey",borderwidth=0)
canvas5.place(x=0,y=405)
canvas5.create_line(0,10,300,10,fill="grey",width=0)

canvas6=Canvas(frame7,width=352,height=-3,bg="grey",borderwidth=0)
canvas6.place(x=0,y=458)
canvas6.create_line(0,10,300,10,fill="grey",width=0)

frame7.mainloop()
