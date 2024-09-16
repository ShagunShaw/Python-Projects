import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from database_connector import DB_connect

global conn, result
result=[]
conn= DB_connect()

def reset_page():
    global page3a, page3b, page3c, page4a, page4b
    
    page3a= page3a_setup(root)
    page3b= page3b_setup(root)
    page3c= page3c_setup(root)
    page4a= page4a_setup(root)
    page4b= page4b_setup(root)

    page3a.place(x=0, y=0, relwidth=1, relheight=1)
    page3b.place(x=0, y=0, relwidth=1, relheight=1)
    page3c.place(x=0, y=0, relwidth=1, relheight=1)
    page4a.place(x=0, y=0, relwidth=1, relheight=1)
    page4b.place(x=0, y=0, relwidth=1, relheight=1)

def show_page1(frame):
    frame.tkraise()
    frame.after(5100, lambda: show_pages(page2))

def show_pages(frames):
    frames.tkraise()

def register(ID):
    conn.register(ID, name, address, phone, DoB, license_no, issue_date, expiry_date, aadhar_no, experience, duty, password)
    return

def fetch(Id):
    return conn.get_values(Id)

def delete():
    confirm= messagebox.askokcancel('Confirm Delete', 'Are you sure you want to delete the data permanently')
    if confirm:
        conn.delete_info(result[0][0])
        reset_page()
        show_pages(page2)
    else:
        return    

def update():
    messagebox.showerror('Could not update', 
                         '''Some error occured, we could not process your request. Try checking your internet connection and connectivity to the database while we redirect you''')
    reset_page()
    show_pages(page2)

def generate_otp():
    global generated_otp
    import random
    from win10toast import ToastNotifier
    toast = ToastNotifier()
    generated_otp=''

    for i in range(6):
        generated_otp= generated_otp + str(random.randint(0,9))

    toast.show_toast(
                "OTP Generated",
                f'''Your OTP for driver's registration is {generated_otp}''',
                duration = 0,
                threaded = True,
                )    
    
    return

def page1_setup(root):
    page1= tk.Frame(root, background='blue')

    image1= Image.open('Bus_icon.jpg')
    resized_img= image1.resize((230,230))
    icon= ImageTk.PhotoImage(resized_img)
    lb1= tk.Label(page1, image= icon, bg='blue')
    lb1.image= icon
    lb1.place(x=45, y=100)

    lb2= tk.Label(page1, text= "Welcome to Driver's Portal !", font="Arial 16 bold", background= 'blue')
    lb2.place(x=7, y=290)

    return page1

def page2_setup(root):
    page2= tk.Frame(root, background='lightsteelblue1')

    l1= tk.Label(page2, text="What are you looking for?", font="comicsans 17 bold", background='lightsteelblue1')
    l1.place(x=17, y=30)

    img= Image.open('driver registration.jpg')
    img= img.resize((150,130))
    icon= ImageTk.PhotoImage(img)

    l2= tk.Label(page2, image=icon, text="Driver registration")
    l2.image= icon
    l2.place(x=80, y=100)

    b1= tk.Button(page2, text="Driver's Registration", font='agencyfb 13 normal',background='gray61', relief='flat', width=16, height=1, command=lambda: show_pages(page3a))
    b1.place(x=77, y=230)

    img= Image.open('driver login.jpg')
    img= img.resize((150,130))
    icon= ImageTk.PhotoImage(img)

    l3= tk.Label(page2, image=icon, text="Driver registration")
    l3.image= icon
    l3.place(x=80, y=290)

    b2= tk.Button(page2, text="Driver's Login", font='agencyfb 13 normal',background='gray61', relief='flat', width=16, height=1, command=lambda: show_pages(page4a))
    b2.place(x=77, y=420)

    return page2

def page3a_setup(root):
    page3a= tk.Frame(root, background='lightsteelblue1')

    l0 = tk.Label(page3a, text=" Registration ", font="britannicbold 23 bold", fg='blue', bg='lightsteelblue1')
    l0.place(x=50, y=10)

    can=tk.Canvas(page3a,  height=400, width=350)
    can.create_rectangle(3,5,290,550, fill="gray84")
    can.place(x=10, y=50)

    l1 = tk.Label(page3a, text='Name', font='calibri 16 normal', bg='gray84')
    l1.place(x=20, y=60)

    t1= tk.Text(page3a, width=25, height=1.5)
    
    l2 = tk.Label(page3a, text='Address', font='calibri 16 normal', bg='gray84')
    l2.place(x=20, y=140)

    t2= tk.Text(page3a, width=25, height=1.5)
    
    l3 = tk.Label(page3a, text='Phone Number', font='calibri 16 normal', bg='gray84')
    l3.place(x=20, y=220)

    t3= tk.Text(page3a, width=25, height=1.5)
    
    l4 = tk.Label(page3a, text='Date of Birth', font='calibri 16 normal', bg='gray84')
    l4.place(x=20, y=300)

    t4= tk.Text(page3a, width=25, height=1.5)
    
    def get_info():
        global name, address, phone, DoB
        name = t1.get("1.0", "end-1c")
        address= t2.get("1.0", "end-1c")
        phone= t3.get("1.0", "end-1c")
        DoB= t4.get("1.0", "end-1c")
        
        if (name=='' or address=='' or phone=='' or DoB==''):
            messagebox.showwarning("Input Error", "All fields must be filled out.")
            return
        
        else:
            show_pages(page3b)
        
    
    t1.place(x=20, y=90)    
    t2.place(x=20, y=170)
    t3.place(x=20, y=250)
    t4.place(x=20, y=330)


    b1= tk.Button(page3a, text="Next",font="algerian 20 normal" ,fg='white', bg='blue', relief='sunken', width=8, height=1, command= get_info)
    b1.place(x=80,y=400)

    l5= tk.Label(page3a, text="Steps 1 out of 3", fg='blue', bg="lightsteelblue1", font="britannicbold 20 italic")
    l5.place(x=53, y=460)

    return page3a

def page3b_setup(root):
    page3b= tk.Frame(root, background='lightsteelblue1')

    l0 = tk.Label(page3b, text=" Registration ", font="britannicbold 23 bold", fg='blue', bg='lightsteelblue1')
    l0.place(x=50, y=10)

    can=tk.Canvas(page3b, height=400, width=350)
    can.create_rectangle(3,5,290,550, fill="gray84")
    can.place(x=10, y=50)

    l1 = tk.Label(page3b, text='Driving License Number', font='calibri 16 normal', bg='gray84')
    l1.place(x=20, y=60)

    t1= tk.Text(page3b, width=25, height=1.5)
    
    l2 = tk.Label(page3b, text='Issue Date', font='calibri 16 normal', bg='gray84')
    l2.place(x=20, y=130)

    t2= tk.Text(page3b, width=11, height=1.5)
    
    l3 = tk.Label(page3b, text='Expiry Date', font='calibri 16 normal', bg='gray84')
    l3.place(x=150, y=130)

    t3= tk.Text(page3b, width=11, height=1.5)
    
    l4 = tk.Label(page3b, text='Previous Driving Experience', font='calibri 16 normal', bg='gray84')
    l4.place(x=20, y=205)

    var=tk.IntVar()
    var.set(0)

    c1= tk.Radiobutton(page3b, text='0-3 yrs', font='calibri 12 normal', variable=var, value=1, bg='gray84').place(x=20,y=235)
    c1= tk.Radiobutton(page3b, text='4-7 yrs', font='calibri 12 normal', variable=var, value=2, bg='gray84').place(x=100,y=235)
    c1= tk.Radiobutton(page3b, text='>7 yrs', font='calibri 12 normal',  variable=var, value=3, bg='gray84').place(x=180,y=235)

    l6 = tk.Label(page3b, text='Aadhar Number', font='calibri 16 normal', bg='gray84')
    l6.place(x=20, y=265)

    t4= tk.Text(page3b, width=25, height=1.5)
    
    l7 = tk.Label(page3b, text='Which duty do you prefer', font='calibri 16 normal', bg='gray84')
    l7.place(x=20, y=335)

    var2=tk.IntVar()
    var2.set(0)

    c2= tk.Radiobutton(page3b, text='Linked Duty', font='calibri 12 normal', variable=var2, value=1, bg='gray84').place(x=20,y=365)
    c2= tk.Radiobutton(page3b, text='Unlinked Duty', font='calibri 12 normal', variable=var2, value=2, bg='gray84').place(x=150,y=365)

    def get_info():
        global license_no, issue_date, expiry_date, aadhar_no, experience, duty
        license_no=t1.get("1.0", "end-1c")
        issue_date= t2.get("1.0", "end-1c")
        expiry_date= t3.get("1.0", "end-1c")
        aadhar_no= t4.get("1.0", "end-1c")
        experience=var.get()
        duty= var2.get()
        
        if (license_no=='' or issue_date=='' or expiry_date=='' or aadhar_no=='' or experience==0 or duty==0):
            messagebox.showwarning("Input Error", "All fields must be filled out.")
            return
        
        else:
            messagebox.showinfo("OTP Generated", "We have sent an OTP to your device")
            generate_otp()
            show_pages(page3c)        
        
        
    t1.place(x=20, y=90)   
    t2.place(x=20, y=160) 
    t3.place(x=150, y=160)
    t4.place(x=20, y=295)

    b1= tk.Button(page3b, text="Next",font="algerian 20 normal" ,fg='white', bg='blue', relief='sunken', width=8, height=1, command=get_info)
    b1.place(x=80,y=400)

    l5= tk.Label(page3b, text="Steps 2 out of 3", fg='blue', bg="lightsteelblue1", font="britannicbold 20 italic")
    l5.place(x=53, y=460)

    return page3b

def page3c_setup(root):
    page3c= tk.Frame(root, background='lightsteelblue1')

    l0 = tk.Label(page3c, text=" Registration ", font="britannicbold 23 bold", fg='blue', bg='lightsteelblue1')
    l0.place(x=50, y=10)

    can=tk.Canvas(page3c,  height=400, width=350)
    can.create_rectangle(3,5,290,550, fill="gray84")
    can.place(x=10, y=50)


    def generate_unique_id():
        import time
        curr= time.strftime("%Y%H%S%M")
        curr= curr[2:]
        return curr

    unique_id = generate_unique_id()

    l1= tk.Label(page3c, text=f'Your new id generated\n is: {unique_id}', font="arial 19 bold", bg='gray84')
    l1.place(x=20, y=80)

    l2= tk.Label(page3c, text="Please enter a password ", font='calibri 18 bold', bg='gray84')
    l2.place(x=20, y=180)

    t1= tk.Text(page3c, width=25, height=2)

    l3= tk.Label(page3c, text="Enter the OTP ", font='calibri 18 bold', bg='gray84')
    l3.place(x=20, y=270)

    t2= tk.Text(page3c, width=25, height=2)

    def get_info():
        global password, otp
        password= t1.get("1.0", "end-1c")
        otp= t2.get("1.0", "end-1c")

        if (password=='' or otp==''):
            messagebox.showwarning("Input Error", "All fields must be filled out.")
            return
        
        else:
            if (otp!= generated_otp):
                messagebox.showerror("Invalid OTP", "Please enter the correct OTP")
                show_pages(page3c)
            else:
                register(unique_id)
                reset_page()
                show_page1(page1)

    t1.place(x=55, y=225)
    t2.place(x=55, y=310)

    b1= tk.Button(page3c, text="Register",font="algerian 20 normal" ,fg='white', bg='blue', relief='sunken', width=8, height=1, command= get_info)
    b1.place(x=80,y=400)

    l5= tk.Label(page3c, text="Steps 3 out of 3", fg='blue', bg="lightsteelblue1", font="britannicbold 20 italic")
    l5.place(x=53, y=460)

    return page3c

def page4a_setup(root):
    page4a= tk.Frame(root, background='lightsteelblue1')

    l0 = tk.Label(page4a,  text=" Login ! ", font="britannicbold 27 bold", fg='blue', bg='lightsteelblue1')
    l0.place(x=80, y=35)

    l1= tk.Label(page4a, text= "Enter your id", font= "comicsans 17 bold")
    l1.place(x=25, y=115)

    t1= tk.Text(page4a, width=25, height=2)

    l2= tk.Label(page4a, text= "Enter your password", font= "comicsans 17 bold")
    l2.place(x=25, y=255)

    t2= tk.Text(page4a, width=25, height=2)

    def get_info():
        global login_id, login_password
        login_id= t1.get("1.0", "end-1c")
        login_password= t2.get("1.0", "end-1c")

        if (login_id=='' or login_password==''):
            messagebox.showwarning("Input Error", "All fields must be filled out.")
            return
        
        else:
            global result
            result= fetch(login_id)
            try:
                if (login_password != result[0][11]):
                    messagebox.showerror("Wrong Password","Please enter your valid password.")
                else:    
                    show_pages(page4b)

            except:
                messagebox.showerror('Invalid Id', 'Please enter a valid login id')  
                return      

    t1.place(x=25, y=160)
    t2.place(x=25, y=300)

    b1= tk.Button(page4a, text="Login",font="algerian 20 normal" ,fg='white', bg='blue', relief='sunken', width=8, height=1, command= get_info)
    b1.place(x=80,y=400)

    return page4a     

def page4b_setup(root):
    page4b=tk.Frame(root, background='lightsteelblue1')

    l0 = tk.Label(page4b, text=f"Welcome,\n John! ", font="britannicbold 27 bold", fg='blue', bg='lightsteelblue1')
    l0.place(x=70, y=35)

    l1= tk.Label(page4b, text=' We have fetched your details\n and want to know for \nwhat are you looking futher?', bg='lightsteelblue1', 
             font='comicsand 17 normal')
    l1.place(x=5, y=145)

    b1= tk.Button(page4b, text="Update",font="algerian 20 normal" ,fg='white', bg='blue', relief='sunken', width=7, height=1, command= update)
    b1.place(x=90,y=265)

    b2= tk.Button(page4b, text="Delete",font="algerian 20 normal" ,fg='white', bg='blue', relief='sunken', width=7, height=1, command= delete)
    b2.place(x=90,y=365)

    return page4b

root= tk.Tk()
root.geometry("310x560")
root.maxsize(310,560)
root.title("Welcome")

global page1, page2, page3a, page3b, page3c, page4a, page4b
global name, address, phone, DoB, license_no, issue_date, expiry_date, aadhar_no, experience, duty, password, otp
global generated_otp

global login_id, login_password

page1= page1_setup(root)
page2= page2_setup(root)

page1.place(x=0, y=0, relwidth=1, relheight=1)
page2.place(x=0, y=0, relwidth=1, relheight=1)

reset_page()

show_page1(page1)

root.tk.mainloop()
