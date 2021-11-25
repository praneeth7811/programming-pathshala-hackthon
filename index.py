from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.font import BOLD, ITALIC
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
from PIL import ImageTk, Image
import random
from twilio.rest import Client

window = Tk()
window.title("ONLINE APPLICATION")
window.geometry("900x500")

frame1 = Frame(window,pady=100)
frame2 = Frame(window,pady=100)
frame3 = Frame(window,padx=180,pady=80)
frame4 = Frame(window,pady=60)
frame5 = Frame(window,pady=30,)
frame6 = Frame(window,pady=60)
frame7 = Frame(window)

var=IntVar()

bg = PhotoImage(file=r"D:\LPU 3rd sem\INT-213\python_project\home.png")
my_canvas = Canvas(window, width=800, height=500)
my_canvas.pack(fill="both", expand=True)


# Set image in canvas
my_canvas.create_image(0,0, image=bg, anchor="nw")
my_canvas.create_text(450, 170, text="WELCOME TO THE ADDMISSON PLATFORM OF LOTUS INSTITUTE OF TECHNOLOGY", font=("times new roman", 16,BOLD,ITALIC), fill="orange")
my_canvas.create_text(440, 240, text="Click The Below Button To Continue...", font=("times new roman", 16,BOLD), fill="white")

#Apply Now Page
def change_frame1():
    frame1.pack()
    btn5.destroy()    
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()

#Login Page
def change_frame2():
    frame2.pack()
    btn5.destroy()    
    frame1.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()

#Documents subit Page
def change_frame3():
    
    frame3.pack(side=LEFT)
    frame1.pack_forget()
    frame2.pack_forget()
    frame4.pack_forget()

#Apply and Login Now buttons
def change_frame4():  
    frame4.pack()
    window.geometry("900x550")
    btn5.destroy()
    my_canvas.destroy()
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame5.pack_forget()

def change_frame4n():  
    extra=Label(window,text="",width=900,height=500)
    extra.pack()
    frame4.pack()
    window.geometry("900x550")
    btn5.destroy()
    my_canvas.destroy()
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame5.pack_forget()

def frame5_logout():
    window.destroy()

#documents SUBMIT complete page
def change_frame5():
    frame5.pack() 
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame6.pack_forget()

    IMAGE_PATH = "D:\LPU 3rd sem\INT-213\python_project\edit.png"
    WIDTH, HEIGTH = 900, 500

    window.geometry('900x500')

    canvas = tk.Canvas(window, width=WIDTH, height=HEIGTH)
    canvas.pack()

    img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGTH), Image.ANTIALIAS))
    canvas.background = img  # Keep a reference in case this code is put in a function.
    bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)


    hello = "      Dear " + Ename.get() + ", your documents are sucessfully uploded. Our college staff will verify your \n documents and contact you soon..."    
    myLabel = Label(window, text=hello,font=("times new roman",18,BOLD,ITALIC), bg= "black", fg="orange")
    myLabel.place(x=27,y=150)  

    button = tk.Button(window, text="Home",bg="grey", borderwidth=1, command = change_frame4n)
    button_window = canvas.create_window(4, 4, anchor=tk.NW, window=button)

    button1 = tk.Button(window, text="Dash Board", bg="grey", borderwidth=1)
    button_window = canvas.create_window(47, 4, anchor=tk.NW, window=button1)

    button2 = tk.Button(window, text="Admission Status", bg="grey", borderwidth=1)
    button_window = canvas.create_window(117, 4, anchor=tk.NW, window=button2)

    button3 = tk.Button(window, text="Logout", bg="grey",fg="black", width=10,borderwidth=2,command = frame5_logout, font=("times new roman",16,BOLD))
    button_window = canvas.create_window(745, 435, anchor=tk.NW, window=button3)

#getting mobile no. and OTP 
def change_frame6():
    frame6.pack()
    frame1.pack_forget()

#Student Dashboard
def change_frame7():
    frame7.pack()
    frame4.pack_forget()

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
        btn3 = Button(frame1, text="SUBMIT", width=10,bg="orange",fg="white",command=change_frame3,font=("times new roman",16,BOLD))
        btn3.grid(row=11,column=3,padx=30,pady=10)
        label2_das = Label(window,text="                                                         ")
        label2_das.place(x=720,y=220)
    else:
        label2=Label(window,text="please Enter correct OTP",fg="red",font=("times new roman",12,BOLD))
        label2.place(x=720,y=220)

def open_file():
    file = filedialog.askopenfile(mode='r', filetypes=[('Pdf files', '*.pdf')])
    if file:
        content = file.read()
        file.close()
        print("%d characters in this file" % len(content))
def Show_password1():
    if(show_password_btnw.get()==1):
        Epassword.config(show='')
    else:
        Epassword.config(show='*')

# home page university logo(frame4)
main_logo= Canvas(frame4, width= 800, height= 800)
main_logo.pack()
img= (Image.open(r"D:\LPU 3rd sem\INT-213\python_project\univ logo.png"))
resized_image= img.resize((800,400), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
main_logo.create_image(5,5, anchor=NW, image=new_image)

#submit Page Label(s)(frame1)
name = Label(frame1,text= "Enter Full Name:",font=("times new roman",20))
namew = StringVar()
mail = Label(frame1,text="Enter Mail Id:",font=("times new roman",20))
mailw = StringVar()
phone = Label(frame1, text="Enter Your Mobile No:",font=("times new roman",20))
phonew = StringVar()
otp = Label(frame1, text="Enter OTP  ",font=("times new roman",20))
otpw = StringVar()
state = Label(frame1,text= "Enter State: ",font=("times new roman",20))
statew = StringVar()
city = Label(frame1,text="Enter  City  ",font=("times new roman",20))
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
show_password_btnw = IntVar(value=0)
show_password_btn = Checkbutton(frame1,text="Show Password",variable=show_password_btnw,onvalue=1,offvalue=0,command=Show_password1,width=12,font=("times new roman",12,BOLD))

Get_otp_btn=Button(frame1,text="GET OTP",command = otp_ver,bg="grey",fg="white",width=12,font=("times new roman",12,BOLD))
Check_otp_btn=Button(frame1,text="SUBMIT OTP",command = otp_ver1,bg="grey",fg="white",width=12,font=("times new roman",12,BOLD))

#Entries For Submit Page(frame1)
Ename = Entry(frame1, textvariable= namew,borderwidth=2)
Email = Entry(frame1, textvariable= mailw)
Ephone = Entry(frame1, textvariable= phonew)
Eotp = Entry(frame1,textvariable= otpw)
Estate = Entry(frame1, textvariable = statew)
Ecity = Entry(frame1,textvariable= cityw)
Epassword = Entry(frame1,textvariable=passwordw,show='*')

#Placing for Submit Page(frame1)
name.grid(row=1,column=1,sticky=tk.W)
Ename.grid(row=1,column=2)
mail.grid(row=2,column=1,sticky=tk.W)
Email.grid(row=2,column=2)
phone.grid(row=3,column=1,sticky=tk.W)
Ephone.grid(row=3,column=2)
Ephone.insert(0,"+91")
otp.grid(row=4,column=1,sticky=tk.W)
Eotp.grid(row=4,column=2)
state.grid(row=5,column=1,sticky=tk.W)
Estate.grid(row=5,column=2)
city.grid(row=6,column=1,sticky=tk.W)
Ecity.grid(row=6,column=2)
genl.grid(row=7,column=1,sticky=tk.W)
gen.grid(row=7,column=2)
quall.grid(row=8,column=1,sticky=tk.W)
qual.grid(row=8,column=2)
password.grid(row=9,column=1,sticky=tk.W)
Epassword.grid(row=9,column=2)
show_password_btn.grid(row=9,column=3,sticky=tk.W)
Get_otp_btn.grid(row=3,column=3,padx=10)
Check_otp_btn.grid(row=4,column=3,padx=10)

#Login Page Label(s)(frame2) 
phonel = Label(frame2,text="Enter Phone/Email",font=("times new roman",20))
phonewl = StringVar()
passwordl = Label(frame2,text="Enter password",font=("times new roman",20))
passwordwl = StringVar()
btn4 = Button(frame2, text="SUBMIT", width=20,bg="orange",fg="white",command=change_frame3,font=("times new roman",16,BOLD))
btn4.place(x=50, y=120)

#Entries For Login page(frame2)
Ephonel = Entry(frame2, textvariable=phonewl)
Epasswordl = Entry(frame2,textvariable=passwordl,show='*')

#Placing for Login Page(fram2)
phonel.grid(row=1,column=1,sticky=tk.W)
Ephonel.grid(row=1,column=2)
passwordl.grid(row=2,column=1,sticky=tk.W)
Epasswordl.grid(row=2,column=2)

#Documents Buttons Submit(frame3)
hello = "\n        Dear " + Ename.get() + ", Please submit your documents"    
myLabel = Label(frame3, text=hello,font=("times new roman",18,BOLD,ITALIC))
myLabel.grid(row=1,column=1)
btnfile1 = Button(frame3,text="10th",width=10,height=1,bg="orange",fg="white",command=open_file,font=("times new roman",16,BOLD))
btnfile2 = Button(frame3,text="INTER",width=10,height=1,bg="orange",fg="white",command=open_file,font=("times new roman",16,BOLD))
btnfile3 = Button(frame3,text="AADHAR",width=10,height=1,bg="orange",fg="white",command=open_file,font=("times new roman",16,BOLD))
btnfile4 = Button(frame3,text="NEXT",width=10,height=1,bg="orange",fg="white",command=change_frame5,font=("times new roman",16,BOLD))

#Placing Documents Buttons
btnfile1.grid(row=2,column=1,pady=10)
btnfile2.grid(row=3,column=1,pady=10)
btnfile3.grid(row=4,column=1,pady=10)
btnfile4.grid(row=60,column=120)

#Hom page Applynow and login Buttons
btn1 = Button(frame4, text="Apply Now", width=10,bg="orange",fg="white",command=change_frame1,font=("times new roman",16,BOLD))
btn1.place(x=200, y=400)
btn2 = Button(frame4, text="Login", width=10,bg="orange",fg="white",command=change_frame7,font=("times new roman",16,BOLD))
btn2.place(x=490,y= 400)

#entering Mobile no. and Verifying OTP Page 
lbl=Label(frame6,text="enter mobile no.",font=("times new roman",16,BOLD))
lblw=StringVar()
Elbl=Entry(frame6,textvariable=lblw)
Elbl.insert(0,"+91")
lbl1=Label(frame6,text="enter OTP",font=("times new roman",16,BOLD))
lblw1 = StringVar()
Elbl1=Entry(frame6,textvariable=lblw1)

#Top-Left Logo
click_btn= PhotoImage(file=r"D:\LPU 3rd sem\INT-213\python_project\Univhomelogo .png")
img_label= Label(image=click_btn)
btn7 = Button(window, image=click_btn,command=change_frame4,width=195,height=100,borderwidth=0)
btn7.place(x=1,y=1)
#main Window Click-here Button
btn5 = Button(window, text="CLICK HERE",bg="grey",fg="white",command=change_frame4,width=12,borderwidth=0,font=("times new roman",16,BOLD))
btn5.place(x=365,y= 290)

window.mainloop()
