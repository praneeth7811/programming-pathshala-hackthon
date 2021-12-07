from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD, ITALIC
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from tkinter import messagebox
from PIL import ImageTk, Image
import random
from twilio.rest import Client

window = Tk()
window.title("ONLINE APPLICATION")
window.state("zoomed")

frame1 = Frame(window,pady=15,padx=15,highlightbackground="grey",highlightthickness=1,bd=5,borderwidth=0,bg="white",width=1200)
frame2 = Frame(window,highlightbackground="grey",highlightthickness=1,bg="white")
frame3 = Frame(window,)
frame4 = Frame(window,pady=200)
frame5 = Frame(window)
frame7 = Frame(window)
frame8=Frame(window,bd=6,bg="grey")
frame9=Frame(window,bd=6,bg="grey")
frame10=Frame(window,bd=6,bg="grey")
frame11=Frame(window,bd=6,bg="grey")
frame12=Frame(window,bd=6,bg="grey")
frame13=Frame(window,bd=6,bg="grey")
frame14=Frame(window,bd=6,bg="grey")

var=IntVar()
captcha = StringVar()
input = StringVar()

bg = PhotoImage(file=r"D:\LPU 3rd sem\INT-213\python_project\home.png")
my_canvas = Canvas(window, width=800, height=500)
my_canvas.pack(fill="both", expand=True)

# Set image in canvas
my_canvas.create_image(0,0, image=bg, anchor="nw")
my_canvas.create_text(950, 270, text="WELCOME TO THE ADDMISSON PLATFORM OF LOTUS INSTITUTE OF TECHNOLOGY", font=("times new roman", 24,BOLD,ITALIC), fill="orange")
my_canvas.create_text(940, 370, text="Click The Below Button To Continue...", font=("times new roman", 22,BOLD), fill="white")

#Apply Now Page
def change_frame1():
    frame1.pack(pady=250)
    btn5.destroy()    
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()

#Login Page
def change_frame2():
    frame2.pack(pady=250)
    btn5.destroy()    
    frame1.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()

#Documents submit Page
def change_frame3():
    frame3.place(x=10,y=110)
    hello = " Dear " + Ename.get() + ", Please submit your documents"    
    myLabel_f3 = Label(frame3, text=hello,font=("times new roman",18,BOLD,ITALIC),bg="#d9d9d9")
    myLabel_f3.place(x=40,y=10)
    frame1.pack_forget()
    frame2.pack_forget()
    frame4.pack_forget()

#Apply and Login Now buttons
def change_frame4():  
    frame4.pack()
    btn5.destroy()
    my_canvas.destroy()
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame5.pack_forget()

#documents SUBMIT complete page
def change_frame5():
    frame5.pack() 
    btn7.destroy()
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()

    #frame 5 image
    IMAGE_PATH = "D:\LPU 3rd sem\INT-213\python_project\edit.png"
    WIDTH, HEIGTH = 2000, 1300
    canvas = tk.Canvas(frame5, width=WIDTH, height=HEIGTH)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGTH), Image.ANTIALIAS))
    canvas.background = img  # Keep a reference in case this code is put in a function.
    bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)
    hello = "                                        Dear " + Ename.get() + ", your documents are sucessfully uploded. Our college staff will verify your                     \n documents and contact you soon...                           "    
    myLabel = Label(frame5, text=hello,font=("times new roman",26,BOLD,ITALIC), bg= "black", fg="orange")
    myLabel.place(x=1,y=150)  
    button = tk.Button(frame5, text="Home",bg="grey", borderwidth=1, command = change_frame4)
    button_window = canvas.create_window(4, 4, anchor=tk.NW, window=button)
    button1 = tk.Button(frame5, text="Dash Board", bg="grey", borderwidth=1,command = change_frame7)
    button_window = canvas.create_window(47, 4, anchor=tk.NW, window=button1)
    button2 = tk.Button(frame5, text="Admission Status", bg="grey", borderwidth=1)
    button_window = canvas.create_window(117, 4, anchor=tk.NW, window=button2)
    button3 = tk.Button(frame5, text="Logout", bg="grey",fg="black", width=10,borderwidth=2,command = frame14_logout, font=("times new roman",16,BOLD))
    button_window = canvas.create_window(1760, 950, anchor=tk.NW, window=button3)

def change_frame7():
    global ext
    frame5.pack_forget()
    ext = Label(window,text="",width=280,height=80)
    ext.pack()
    screen_width = window.winfo_screenwidth()
    Main_bar = Label(window,text="",bg="white",width=screen_width,height=5)
    Main_bar.place(x=0,y=4)

    click_btn2= PhotoImage(file=r"D:\LPU 3rd sem\INT-213\python_project\Univhomelogo .png")
    img_label2 = Label(image=click_btn2)
    btn8 = Button(window, image=click_btn2,width=195,height=80,borderwidth=0,bg="white",command=change_frame4)
    btn8.place(x=1,y=3)

    Side_bar = Label(window,text="",bg="#2c333a",width=50,height=80)
    #Side_bar.configure(bg="#2c333a")
    Side_bar.place(x=0,y=87)

    Side_bar_label1 =Button(window,text="Dashboard",command=frame8_dashboard,bg="#2c333a",fg="white",height=1,font=(" nunito-sans sans-serif",16),borderwidth=0) 
    Side_bar_label1.place(x=20,y=93)

    Side_bar_label2 =Button(window,text="All Application Form(s)",command = frame9_Form,bg="#2c333a",fg="white",height=1,font=(" nunito-sans sans-serif",16),borderwidth=0) 
    Side_bar_label2.place(x=20,y=146)

    Side_bar_label3 =Button(window,text="My Profile",command = frame10_profile,bg="#2c3338",fg="white",height=1,font=(" nunito-sans sans-serif",16),borderwidth=0) 
    Side_bar_label3.place(x=20,y=199)

    Side_bar_label4 =Button(window,text="My Queries",command = frame11_quires,bg="#2c3338",fg="white",height=1,font=(" nunito-sans sans-serif",16),borderwidth=0) 
    Side_bar_label4.place(x=20,y=252)

    Side_bar_label5 =Button(window,text="My Communication",command = frame12_Communication,bg="#2c3338",fg="white",height=1,font=(" nunito-sans sans-serif",16),borderwidth=0) 
    Side_bar_label5.place(x=20,y=305)

    Side_bar_label6 =Button(window,text="My Payments",command = frame13_pay,bg="#2c3338",fg="white",height=1,font=(" nunito-sans sans-serif",16),borderwidth=0) 
    Side_bar_label6.place(x=20,y=358)

    Side_bar_label7 =Button(window,text="Logout",command = frame14_logout,bg="#2c3338",fg="white",height=1,font=(" nunito-sans sans-serif",16),borderwidth=0) 
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

def frame8_dashboard():
    ext.destroy()
    frame8.place(x=355,y=87)
    Label(frame8,text="",width=221,height=60).pack()
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
    frame9.place(x=355,y=87)
    Label(frame9,text="",width=221,height=60).pack()
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
    Label(frame9,text="",width=0,height=2,bg="#666666").place(x=1200,y=115)

    Label(frame9,text="Application Form",fg="#d11f51",font=("Nutino Sans,sans-serif",12)).place(x=15,y=285)

    Label(frame9,text="",width=215,height=5,bg="white").place(x=15,y=315)
    Label(frame9,text="",width=0,height=5,bg="#d11f51").place(x=15,y=315)
    Label(frame9,text="LITE Test | B-tech - 2022",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",13)).place(x=30,y=340)
    Label(frame9,text="",width=0,height=5,bg="#666666").place(x=515,y=315)
    Label(frame9,text=" - ",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",16,BOLD)).place(x=650,y=340)
    Label(frame9,text="",width=0,height=5,bg="#666666").place(x=785,y=315)
    Label(frame9,text=" - ",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",16,BOLD)).place(x=880,y=340)
    Label(frame9,text="",width=0,height=5,bg="#666666").place(x=1015,y=315)
    Button(frame9,text=" Apply For LITE Test",bg="#f68220",fg="white",borderwidth=0,font=("Nutino Sans,sans-serif",10,BOLD)).place(x=1060,y=340)
    Label(frame9,text="",width=0,height=5,bg="#666666").place(x=1250,y=315)

    Label(frame9,text="",width=215,height=6,bg="white").place(x=15,y=430)
    Label(frame9,text="",width=0,height=6,bg="#d11f51").place(x=15,y=430)
    Label(frame9,text="LITE Test | B-tech - 2022",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",13)).place(x=30,y=455)
    Label(frame9,text="",width=0,height=6,bg="#666666").place(x=515,y=430)
    Label(frame9,text=" - ",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",16,BOLD)).place(x=650,y=455)
    Label(frame9,text="",width=0,height=6,bg="#666666").place(x=785,y=430)
    Label(frame9,text=" - ",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",16,BOLD)).place(x=880,y=455)
    Label(frame9,text="",width=0,height=6,bg="#666666").place(x=1015,y=430)
    Button(frame9,text=" Take Admission",bg="#f68220",fg="white",borderwidth=0,font=("Nutino Sans,sans-serif",10,BOLD)).place(x=1080,y=450)
    Button(frame9,text=" Apply For LITE Test",bg="#f68220",fg="white",borderwidth=0,font=("Nutino Sans,sans-serif",10,BOLD)).place(x=1070,y=485)
    Label(frame9,text="",width=0,height=6,bg="#666666").place(x=1250,y=430)

def frame10_profile():
    frame10.place(x=355,y=87)
    Label(frame10,text="",width=221,height=60).pack()
    Dash_l1 = Label(frame10,text="My Profile",font=("nunito-sans sans-serif",21))
    Dash_l1.place(x=15,y=10)
    
    Button(frame10,text="Admission Application User-Guide",width = 30,height = 1,bg="#337ab7",fg="white",font = ("nunito-sans",12,),borderwidth=0).place(x=1250,y=20)
    Dash_l2 = Label(frame10,text="Kindly verify the eligibility of the programme from the university website before taking admission.",font=("nunito-sans sans-serif",16))
    Dash_l2.place(x=350,y=70)

    Label(frame10,text="",width=215,height=15,bg = "#d9d9d9").place(x=15,y=115)
    Label(frame10,text="your documents are still in the process of Verification \n This tab will update your deatils after verification of your documents",
                                            bg = "#d9d9d9",fg="#666666",font=("Nutino Sans,sans-serif",18)).place(x=420,y=200)

def frame11_quires():
    frame11.place(x=355,y=87)
    Label(frame11,text="",width=221,height=60).pack()
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

    Button(frame11,text=" Any Queries?Ask Us",bg="#f68220",fg="white",font=("Nutino Sans,sans-serif",14,BOLD)).place(x=1330,y=815)

def frame12_Communication():
    frame12.place(x=355,y=87)
    Label(frame12,text="",width=221,height=60).pack()
    Dash_l1 = Label(frame12,text="My Communication(s)",font=("nunito-sans sans-serif",21))
    Dash_l1.place(x=15,y=10)
    
    Button(frame12,text="Admission Application User-Guide",width = 30,height = 1,bg="#337ab7",fg="white",font = ("nunito-sans",12,),borderwidth=0).place(x=1250,y=20)
    Dash_l2 = Label(frame12,text="Kindly verify the eligibility of the programme from the university website before taking admission.",font=("nunito-sans sans-serif",16))
    Dash_l2.place(x=350,y=70)

    Label(frame12,text="",width=215,height=15,bg = "#d9d9d9").place(x=15,y=115)
    Label(frame12,text="We will Communicate you soon...",
                                            bg = "#d9d9d9",fg="#666666",font=("Nutino Sans,sans-serif",18)).place(x=420,y=200)

def frame13_pay():
    frame13.place(x=355,y=87)
    Label(frame13,text="",width=221,height=60).pack()
    Dash_l1 = Label(frame13,text="My Payments(s)",font=("nunito-sans sans-serif",21))
    Dash_l1.place(x=15,y=10)
    
    Button(frame13,text="Admission Application User-Guide",width = 30,height = 1,bg="#337ab7",fg="white",font = ("nunito-sans",12,),borderwidth=0).place(x=1250,y=20)
    Dash_l2 = Label(frame13,text="Kindly verify the eligibility of the programme from the university website before taking admission.",font=("nunito-sans sans-serif",16))
    Dash_l2.place(x=350,y=70)

    Label(frame13,text="",width=215,height=50,bg = "#d9d9d9").place(x=15,y=115)

    Label(frame13,text="",width=215,height=6,bg="white").place(x=15,y=115)
    Label(frame13,text="Pay Now And\n Book your Seat in LIT",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",16)).place(x=90,y=135)
    Label(frame13,text="",width=0,height=6,bg="#666666").place(x=460,y=115)
    Label(frame13,text=" Fee For Seat Conformation \n \n 9000 ",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",16,BOLD)).place(x=490,y=125)
    Label(frame13,text="",width=0,height=6,bg="#666666").place(x=785,y=115)
    Label(frame13,text=" Appliation Charge \n \n 1000 ",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",16,BOLD)).place(x=800,y=125)
    Label(frame13,text="",width=0,height=6,bg="#666666").place(x=1015,y=115)
    Label(frame13,text=" Total Fee to pay\n \n 10,000 ",bg="white",fg="#666666",font=("Nutino Sans,sans-serif",16,BOLD)).place(x=1040,y=125)
    Label(frame13,text="",width=0,height=6,bg="#666666").place(x=1250,y=115)
    Button(frame13,text=" Pay Now",bg="#f68220",fg="white",font=("Nutino Sans,sans-serif",14,BOLD)).place(x=1320,y=135)
    Button(frame13,text=" Pay Total Fee",bg="#f68220",fg="white",font=("Nutino Sans,sans-serif",14,BOLD)).place(x=1330,y=815)


def frame14_logout():
    exit = messagebox.askquestion("LOG OUT","Are You Sure You Want To Logout",icon='warning')
    if exit == 'yes':
        window.destroy()
    else:
        messagebox.showinfo('Return','You Will Now Return To The Aplication Screen')

#otp verification
def otp_ver():
    global k
    global otp
    global msg
    otp = random.randint(1000,9999)
    k=str(otp)
    print(k)
    client = Client("AC892a914ba3785f5c6b9c3bf7c529bd37", "5f6f041f8a9a34fdf6002e3f35d04d76")
    msg=client.api.account.messages.create(
            to=phonew.get(),
            from_="+18507895934",
            body="your otp is" +str(otp))
def otp_ver1():
    global label2
    global btnf6
    if k == otpw.get():
        # label2.destroy()
        btn3 = Button(frame1, text="SUBMIT", width=10,bg="orange",fg="white",command=change_frame3,font=("times new roman",16,BOLD))
        btn3.grid(row=11,column=3,padx=30,pady=10)
    else:
        messagebox.showinfo("OTP error","PLEASE ENTER CORRECT OTP")

def open_file1():
    global file1
    file1 = filedialog.askopenfile(mode='r', filetypes=[('Pdf files', '*.pdf')])
    if file1:
        Label(frame3,text="Document Submitted",font=("times new roman",18)).place(x=220,y=320)
def open_file2():
    global file2
    file2 = filedialog.askopenfile(mode='r', filetypes=[('Pdf files', '*.pdf')])
    if file2:
        Label(frame3,text="Document Submitted",font=("times new roman",18)).place(x=850,y=320)
def open_file3():
    global file3
    file3 = filedialog.askopenfile(mode='r', filetypes=[('Pdf files', '*.pdf')])
    if file3:
        Label(frame3,text="Document Submitted",font=("times new roman",18)).place(x=1480,y=320)

def open_file4():
    global file4
    file4 = filedialog.askopenfile(mode='r', filetypes=[('Pdf files', '*.pdf')])
    if file4:
        Label(frame3,text="Document Submitted",font=("times new roman",18)).place(x=220,y=730)
def open_file5():
    global file5
    file5 = filedialog.askopenfile(mode='r', filetypes=[('Pdf files', '*.pdf')])
    if file5:
        Label(frame3,text="Document Submitted",font=("times new roman",18)).place(x=850,y=730)
def open_file6():
    global file6
    file6 = filedialog.askopenfile(mode='r', filetypes=[('Pdf files', '*.pdf')])
    if file6:
        Label(frame3,text="Document Submitted",font=("times new roman",18)).place(x=1480,y=730)                

def Show_password1():
    if(show_password_btnw.get()==1):
        Epassword.config(show='')
    else:
        Epassword.config(show='*')
def Show_password2():
    if(show_password_btnw.get()==1):
        Epasswordl.config(show='')
    else:
        Epasswordl.config(show='*')

# home page university logo(frame4)
main_logo= Canvas(frame4, width= 800, height= 800)
main_logo.pack()
img= (Image.open(r"D:\LPU 3rd sem\INT-213\python_project\univ logo.png"))
resized_image= img.resize((800,400), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
main_logo.create_image(5,5, anchor=NW, image=new_image)

#submit Page Label(s)(frame1)
Label(frame1,text="",bg="white").grid(row=1,column=1,pady=25)
Label(frame1,text="Registration Form",fg="black",bg="white",font=("Google Sans,Noto Sans Myanmar UI,arial,sans-serif",24)).place(x=185,y=10)
name = Label(frame1,text= "Enter Full Name:",bg="white",font=("times new roman",20))
namew = StringVar()
mail = Label(frame1,text="Enter Mail Id:",bg="white",font=("times new roman",20))
mailw = StringVar()
phone = Label(frame1, text="Enter Your Mobile No:",bg="white",font=("times new roman",20))
phonew = StringVar()
otp = Label(frame1, text="Enter OTP  ",bg="white",font=("times new roman",20))
otpw = StringVar()
state = Label(frame1,text= "Enter State: ",bg="white",font=("times new roman",20))
statew = StringVar()
city = Label(frame1,text="Enter  City  ",bg="white",font=("times new roman",20))
cityw = StringVar()
genl=Label(frame1,text="Select Gender:",bg="white",font=("times new roman",20))
genw=StringVar()
genw.set("Select Gender")
gen = OptionMenu(frame1, genw,"Male", "Female","Other")
gen.config(width=15,bg="white",font=("times new roman",12))
quall=Label(frame1,text="Select Your Qualification ",bg="white",font=("times new roman",20))
qualw= StringVar()
qualw.set("Qualification ")
qual = OptionMenu(frame1, qualw,"10th", "12th","Degree Or Certifiacate","Graduation","Post Graduation","Ph.D")
qual.config(width=15,bg="white",font=("times new roman",12))
password = Label(frame1,text="Enter Your Password:",bg="white",font=("times new roman",20))
passwordw = StringVar()
show_password_btnw = IntVar(value=0)
show_password_btn = Checkbutton(frame1,text="Show Password",variable=show_password_btnw,bg="white",onvalue=1,offvalue=0,command=Show_password1,width=12,font=("times new roman",12,BOLD))

Get_otp_btn=Button(frame1,text="GET OTP",command = otp_ver,bg="grey",fg="white",width=12,font=("times new roman",12,BOLD))
Check_otp_btn=Button(frame1,text="SUBMIT OTP",command = otp_ver1,bg="grey",fg="white",width=12,font=("times new roman",12,BOLD))

Button(frame1,text="sign in instead",command=change_frame2,bg="white",fg="#337ab7",font=("sans-serif",11,ITALIC,BOLD),relief=tk.SUNKEN,borderwidth=0).grid(row=11,column=1,sticky=tk.W,padx=0,pady=10)

#Entries For Submit Page(frame1)
Ename = Entry(frame1, textvariable= namew,font=("sans-serif",12),width=20,borderwidth=0,highlightbackground="#337ab7",highlightthickness=1)
Email = ttk.Entry(frame1, textvariable= mailw,font=("sans-serif",12),width=20,)
Ephone = Entry(frame1, textvariable= phonew,font=("sans-serif",12),width=20,borderwidth=0,highlightbackground="#337ab7",highlightthickness=1)
Eotp = ttk.Entry(frame1,textvariable= otpw,font=("sans-serif",12),width=20,)
Estate = ttk.Entry(frame1, textvariable = statew,font=("sans-serif",12),width=20,)
Ecity = ttk.Entry(frame1,textvariable= cityw,font=("sans-serif",12),width=20,)
Epassword = ttk.Entry(frame1,textvariable=passwordw,show='*',font=("sans-serif",12),width=20,)

#Placing for Submit Page(frame1)
name.grid(row=2,column=1,sticky=tk.W)
Ename.grid(row=2,column=2)
mail.grid(row=3,column=1,sticky=tk.W)
Email.grid(row=3,column=2)
phone.grid(row=4,column=1,sticky=tk.W)
Ephone.grid(row=4,column=2)
Ephone.insert(0,"+91")
otp.grid(row=5,column=1,sticky=tk.W)
Eotp.grid(row=5,column=2)
state.grid(row=6,column=1,sticky=tk.W)
Estate.grid(row=6,column=2)
city.grid(row=7,column=1,sticky=tk.W)
Ecity.grid(row=7,column=2)
genl.grid(row=8,column=1,sticky=tk.W)
gen.grid(row=8,column=2)
quall.grid(row=9,column=1,sticky=tk.W)
qual.grid(row=9,column=2)
password.grid(row=10,column=1,sticky=tk.W)
Epassword.grid(row=10,column=2)
show_password_btn.grid(row=10,column=3,sticky=tk.W,padx=10)
Get_otp_btn.grid(row=4,column=3,padx=10)
Check_otp_btn.grid(row=5,column=3,padx=10)

#Login Page Label(s)(frame2)
Label(frame2,text="",bg="white",width=70,height=40).pack()
Label(frame2,text="Sign in",fg="black",bg="white",font=("Google Sans,Noto Sans Myanmar UI,arial,sans-serif",24)).place(x=185,y=30)
Label(frame2,text="to continue to Dashboard",fg="black",bg="white",font=("Google Sans,Noto Sans Myanmar UI,arial,sans-serif",12)).place(x=155,y=70)

phonel = Label(frame2,text="Enter Phone/Email  ",font=("times new roman",12),bg="white")
phonewl = StringVar()
passwordl = Label(frame2,text="Enter Password  ",font=("times new roman",12),bg="white")
passwordwl = StringVar()
btn4 = Button(frame2, text="SUBMIT", width=10,bg="orange",fg="white",command=change_frame5,font=("times new roman",16,BOLD))
btn4.place(x=330, y=400)
show_password_btnl = Checkbutton(frame2,text=" Show Password",variable=show_password_btnw,bg="white",fg="#202124",onvalue=1,offvalue=0,command=Show_password2,width=12,font=("roboto,Noto Sans Myanmar UI,sans-serif",12,BOLD)).place(x=90,y=265)
Button(frame2,text="Register Now!",command=change_frame1,
                                bg="white",fg="#1a73e8",font=("sans-serif",11,ITALIC,BOLD),
                                relief=tk.SUNKEN,borderwidth=0).place(x=90,y=410)
Button(frame2,text="Forget Password?",bg="white",fg="#1a73e8",
                                font=("sans-serif",8,ITALIC,BOLD),
                                relief=tk.SUNKEN,borderwidth=0).place(x=300,y=265)

#Entries For Login page(frame2)
Ephonel = ttk.Entry(frame2, textvariable=phonewl,width=25,font=("times new roman",18),)
Epasswordl = ttk.Entry(frame2,textvariable=passwordl,show='*',width=25,font=("times new roman",18),)

#Placing for Login Page(frame2)
phonel.place(x=90,y=120)
Ephonel.place(x=90,y=145)
passwordl.place(x=90,y=200)
Epasswordl.place(x=90,y=225)

#Documents Buttons Submit(frame3)
Label(frame3,text="",bg="#d9d9d9",width=270,height=59).pack()

Label(frame3,text="",width=80,height=25).place(x=40,y=50)
Label(frame3,text="",width=80,height=25,).place(x=670,y=50)
Label(frame3,text="",width=80,height=25).place(x=1300,y=50)

Label(frame3,text="",width=80,height=25).place(x=40,y=460)
Label(frame3,text="",width=80,height=25,).place(x=670,y=460)
Label(frame3,text="",width=80,height=25).place(x=1300,y=460)

Label(frame3,text="10th - Marksheet",fg="black",bg="orange",width=43,height=2,font=("times new roman",18)).place(x=40,y=50)
Label(frame3,text="12th - Marksheet",fg="black",bg="orange",width=43,height=2,font=("times new roman",18)).place(x=670,y=50)
Label(frame3,text="AADHAR",fg="black",bg="orange",width=43,height=2,font=("times new roman",18)).place(x=1300,y=50)

Label(frame3,text="Canditate Signature",fg="black",bg="orange",width=43,height=2,font=("times new roman",18)).place(x=40,y=460)
Label(frame3,text="Father Signature",fg="black",bg="orange",width=43,height=2,font=("times new roman",18)).place(x=670,y=460)
Label(frame3,text="Mother Signature",fg="black",bg="orange",width=43,height=2,font=("times new roman",18)).place(x=1300,y=460)

Button(frame3,text="UPLOAD",fg="white",bg="orange",width=10,height=1,command=open_file1,font=("times new roman",16,BOLD)).place(x=250,y=220)
Button(frame3,text="UPLOAD",fg="white",bg="orange",width=10,height=1,command=open_file2,font=("times new roman",16,BOLD)).place(x=880,y=220)
Button(frame3,text="UPLOAD",fg="white",bg="orange",width=10,height=1,command=open_file3,font=("times new roman",16,BOLD)).place(x=1510,y=220)

Button(frame3,text="UPLOAD",fg="white",bg="orange",width=10,height=1,command=open_file4,font=("times new roman",16,BOLD)).place(x=250,y=630)
Button(frame3,text="UPLOAD",fg="white",bg="orange",width=10,height=1,command=open_file5,font=("times new roman",16,BOLD)).place(x=880,y=630)
Button(frame3,text="UPLOAD",fg="white",bg="orange",width=10,height=1,command=open_file6,font=("times new roman",16,BOLD)).place(x=1510,y=630)

Button(frame3,text="Next",fg="white",bg="#337ab7",width=10,height=1,command=change_frame5,font=("times new roman",14,BOLD)).place(x=1738,y=5)

#Home page Applynow and login Buttons
btn1 = Button(frame4, text="Apply Now", width=10,bg="orange",fg="white",command=change_frame1,font=("times new roman",16,BOLD))
btn1.place(x=200, y=400)
btn2 = Button(frame4, text="Login", width=10,bg="orange",fg="white",command=change_frame2,font=("times new roman",16,BOLD))
btn2.place(x=490,y= 400)

#Top-Left Logo
click_btn= PhotoImage(file=r"D:\LPU 3rd sem\INT-213\python_project\Univhomelogo .png")
img_label= Label(image=click_btn)
btn7 = Button(window, image=click_btn,command=change_frame4,width=195,height=100,borderwidth=0)
btn7.place(x=1,y=1)

#main Window Click-here Button
btn5 = Button(window, text="CLICK HERE",bg="grey",fg="white",command=change_frame4,width=12,borderwidth=0,font=("times new roman",16,BOLD))
btn5.place(x=865,y= 470)

window.mainloop()
