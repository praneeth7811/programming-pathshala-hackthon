from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.font import BOLD, ITALIC
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
from PIL import ImageTk, Image

window = Tk()
window.title("ONLINE APPLICATION")
window.geometry("900x500")

frame1 = Frame(window,pady=110)
frame2 = Frame(window,pady=100)
frame3 = Frame(window,padx=280,pady=180)
frame4 = Frame(window,pady=60)
frame5 = Frame(window,pady=30)

var=IntVar()

bg = PhotoImage(file="D:\LPU 3rd sem\INT-213\python_project\home.png")

my_canvas = Canvas(window, width=800, height=500)
my_canvas.pack(fill="both", expand=True)

# Set image in canvas
my_canvas.create_image(0,0, image=bg, anchor="nw")

my_canvas.create_text(450, 170, text="WELCOME TO THE ADDMISSON PLATFORM OF LOTUS INSTITUTE OF TECHNOLOGY", font=("times new roman", 16,BOLD,ITALIC), fill="orange")

my_canvas.create_text(440, 240, text="Click The Below Button To Continue...", font=("times new roman", 16,BOLD), fill="white")

def change_frame1():
    frame1.pack()
    btn5.destroy()    
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()

def change_frame2():
    frame2.pack()
    btn5.destroy()    
    frame1.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()

def change_frame3():
    hello = "Dear," + Ename.get() + "Please submit your documents"
    myLabel = Label(window, text=hello,font=("times new roman",18,BOLD,ITALIC))
    myLabel.place(x=0,y=110)  
    frame3.pack(side=LEFT)
    frame1.pack_forget()
    frame2.pack_forget()
    frame4.pack_forget()

def change_frame4():  
    frame4.pack()
    window.geometry("900x550")
    btn5.destroy()
    my_canvas.destroy()
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame5.pack_forget()
    

def change_frame5():
    frame5.pack() 
    myLabel1 = Label(frame5, text="                                                            ",font=("times new roman",18,BOLD,ITALIC))
    myLabel1.place(x=0,y=110) 
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    hello = "Dear," + Ename.get() + "your documents are sucessfully uploded \n we wil verify your documents \n and contact you soon"
    myLabel = Label(window, text=hello,font=("times new roman",18,BOLD,ITALIC))
    myLabel.place(x=0,y=110)  

def open_file():
    file = filedialog.askopenfile(mode='r', filetypes=[('Pdf files', '*.pdf')])
    if file:
        content = file.read()
        file.close()
        print("%d characters in this file" % len(content))

    

canvas= Canvas(frame4, width= 800, height= 800)
canvas.pack()

img= (Image.open(r"D:\LPU 3rd sem\INT-213\python_project\univ logo.png"))

resized_image= img.resize((800,400), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

canvas.create_image(5,5, anchor=NW, image=new_image)

name = Label(frame1,text= "Enter Full Name:",font=("times new roman",20))
namew = StringVar()
mail = Label(frame1,text="Enter Mail Id:",font=("times new roman",20))
mailw = StringVar()
phone = Label(frame1, text="Enter Your Mobile No:",font=("times new roman",20))
phonew = StringVar()
otp = Label(frame1, text="  Enter OTP  ",font=("times new roman",20))
otpw = StringVar()
state = Label(frame1,text= "Enter State: ",font=("times new roman",20))
statew = StringVar()
city = Label(frame1,text="  Enter  City  ",font=("times new roman",20))
cityw = StringVar()
genl=Label(frame1,text="Select Gender:",font=("times new roman",20))
genw=StringVar()
genw.set("Select Gender")
gen = OptionMenu(frame1, genw,"Male", "Female","Other")
quall=Label(frame1,text="Select Your Qualification ",font=("times new roman",20))
qualw= StringVar()
qualw.set("Qualification ")
qual = OptionMenu(frame1, qualw,"10th", "12th","Degree Or Certifiacate","Graduation","Post Graduation","Ph.D")
password = Label(frame1,text="Enter Your Password:",font=("times new roman",20))
passwordw = StringVar()
repassword = Label(frame1,text="Confirm Password:",font=("times new roman",20))
repasswordw = StringVar()
btn3 = Button(frame1, text="SUBMIT", width=10,bg="orange",fg="white",command=change_frame3,font=("times new roman",16,BOLD))
btn3.place(x=570, y=360)

Ename = Entry(frame1, textvariable= namew)
Email = Entry(frame1, textvariable= mailw)
Ephone = Entry(frame1, textvariable= phonew)
Eotp = Entry(frame1,textvariable= otpw)
Estate = Entry(frame1, textvariable = statew)
Ecity = Entry(frame1,textvariable= cityw)
Epassword = Entry(frame1,textvariable=passwordw,show='*')
Erepassword = Entry(frame1,textvariable=repasswordw,show='*')

name.grid(row=1,column=1,sticky=tk.W)
Ename.grid(row=1,column=2)
mail.grid(row=2,column=1,sticky=tk.W)
Email.grid(row=2,column=2)
phone.grid(row=3,column=1,sticky=tk.W)
Ephone.grid(row=3,column=2)
otp.grid(row=3,column=3)
Eotp.grid(row=3,column=4)
state.grid(row=4,column=1,sticky=tk.W)
Estate.grid(row=4,column=2)
city.grid(row=4,column=3)
Ecity.grid(row=4,column=4)
genl.grid(row=5,column=1,sticky=tk.W)
gen.grid(row=5,column=2)
quall.grid(row=6,column=1,sticky=tk.W)
qual.grid(row=6,column=2)
password.grid(row=7,column=1,sticky=tk.W)
Epassword.grid(row=7,column=2)
repassword.grid(row=8,column=1,sticky=tk.W)
Erepassword.grid(row=8,column=2)

phonel = Label(frame2,text="Enter Phone/Email",font=("times new roman",20))
phonewl = StringVar()
passwordl = Label(frame2,text="Enter password",font=("times new roman",20))
passwordwl = StringVar()
btn4 = Button(frame2, text="SUBMIT", width=20,bg="orange",fg="white",command=change_frame3,font=("times new roman",16,BOLD))
btn4.place(x=50, y=120)

Ephonel = Entry(frame2, textvariable=phonewl)
Epasswordl = Entry(frame2,textvariable=passwordl,show='*')

phonel.grid(row=1,column=1,sticky=tk.W)
Ephonel.grid(row=1,column=2)
passwordl.grid(row=2,column=1,sticky=tk.W)
Epasswordl.grid(row=2,column=2)

ofile = Label(frame3,text= "Submit Your Documents",font=("times new roman",20),pady=10)
btnfile1 = Button(frame3,text="10th",width=10,height=1,bg="orange",fg="white",command=open_file,font=("times new roman",16,BOLD))
btnfile2 = Button(frame3,text="INTER",width=10,height=1,bg="orange",fg="white",command=open_file,font=("times new roman",16,BOLD))
btnfile3 = Button(frame3,text="AADHAR",width=10,height=1,bg="orange",fg="white",command=open_file,font=("times new roman",16,BOLD))
btnfile4 = Button(frame3,text="NEXT",width=10,height=1,bg="orange",fg="white",command=change_frame5,font=("times new roman",16,BOLD))

click_btn= PhotoImage(file=r"D:\LPU 3rd sem\INT-213\python_project\Univhomelogo .png")
img_label= Label(image=click_btn)

btn7 = Button(window, image=click_btn,command=change_frame4,width=195,height=100,borderwidth=0)
btn7.place(x=1,y=1)

ofile.grid(row=1,column=1)
btnfile1.grid(row=2,column=1,pady=10)
btnfile2.grid(row=3,column=1,pady=10)
btnfile3.grid(row=4,column=1,pady=10)
btnfile4.grid(row=5,column=1,pady=10)

btn1 = Button(frame4, text="Apply Now", width=10,bg="orange",fg="white",command=change_frame1,font=("times new roman",16,BOLD))
btn1.place(x=200, y=400)

btn2 = Button(frame4, text="Login", width=10,bg="orange",fg="white",command=change_frame2,font=("times new roman",16,BOLD))
btn2.place(x=490,y= 400)

btn5 = Button(window, text="CLICK HERE",bg="grey",fg="white",command=change_frame4,width=12,borderwidth=0,font=("times new roman",16,BOLD))
btn5.place(x=365,y= 290)

lbl5=Label(frame5,text="")

window.mainloop()