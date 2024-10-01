from customtkinter import *
from tkinter import *
from PIL import ImageTk,Image
import mysql.connector as mc
from CTkMessagebox import CTkMessagebox
from pygame import mixer


set_appearance_mode("Light")
set_default_color_theme("green")
app = CTk()
app.geometry("1000x600")
app.title("Planet Dynamics")
'''
img = CTkImage(light_image=Image.open("demo_bg_pic.png"), size= (1000,600))
image_place = CTkLabel(master = app,text = "", image = img)
image_place.pack(pady = 0,padx = 0,expand = True)
'''
#==================Establishing Database Connection=========================================
host = "localhost"
user = "root"
password = ""
db = "planet_dynamics"

con = mc.connect(
    host = host,
    user = user,
    password = password,
    database = db
)

cur = con.cursor()

#==================Login Frame Raise=========================================
def login_frame_raise():
    welcome_btn_frame.pack_forget()
    login_frame.pack(side=BOTTOM, pady=10, padx=10, fill=BOTH, expand=True)


#==================go to welcome btn frame=========================================
def cancel_login_account():
    login_frame.pack_forget()
    welcome_btn_frame.pack(side=BOTTOM, pady=10, padx=10, fill=BOTH, expand=True)

#==================go to welcome btn frame=========================================
def login_part():
    signup_frame.pack_forget()
    login_frame.pack(side=BOTTOM, pady=10, padx=10, fill=BOTH, expand=True)


#==================Signup Frame Raise=========================================
def signup_frame_raise():
    welcome_btn_frame.pack_forget()
    signup_frame.pack(side=BOTTOM, pady=10, padx=10, fill=BOTH, expand=True)

#==================Welcome new user=========================================
def welcome_new_user():
    registration_message = CTkMessagebox(title = "Registration Successful", message = "You have successfully created an account.\nPress the 'Login' button to enter the login page!!",icon = "check" ,option_1="Login")
    if registration_message.get() == "Login":
        login_frame.pack(side=BOTTOM, pady=10, padx=10, fill=BOTH, expand=True)

#==================Warn User at account creation=========================================
def warn_new_user():
    registration_message = CTkMessagebox(title = "Registration Unsuccessful", message = "Registration Failed.\n 1) Check your Gmail and name\n2)Insert password more than 5 letters",icon = "warning", option_1="Sign Up Again",option_2="Cancel")
    if registration_message.get() == "Sign Up Again":
        signup_frame.pack(side=BOTTOM, pady=10, padx=10, fill=BOTH, expand=True)
    if registration_message.get() == "Cancel":
        signup_frame.pack_forget()
        welcome_btn_frame.pack(side=BOTTOM, pady=10, padx=10, fill=BOTH, expand=True)

#==================Warn User for existed account=========================================
def warn_existence():
    registration_message = CTkMessagebox(title = "Account Already Existed", message = "You are already a member. Login your account",icon = "info", option_1="Login",option_2="Cancel")
    if registration_message.get() == "Login":
        signup_frame.pack_forget()
        login_frame.pack(side=BOTTOM, pady=10, padx=10, fill=BOTH, expand=True)
    if registration_message.get() == "Cancel":
        welcome_btn_frame.pack(side=BOTTOM, pady=10, padx=10, fill=BOTH, expand=True)

#==================Warn User for creating account=========================================
def warn_for_create_account():
    registration_message = CTkMessagebox(title = "No account found", message = "You have no account.\nPlease Sign Up..",icon = "info", option_1="Sign Up",option_2="Cancel")
    if registration_message.get() == "Sign Up":
        login_frame.pack_forget()
        signup_frame.pack(side=BOTTOM, pady=10, padx=10, fill=BOTH, expand=True)
    if registration_message.get() == "Cancel":
        login_frame.pack_forget()
        welcome_btn_frame.pack(side=BOTTOM, pady=10, padx=10, fill=BOTH, expand=True)

#==================Warn User for invalid credential=========================================
def warn_for_invalid_credential(name):
    registration_message = CTkMessagebox(title = "Invalid Password", message = f"{name}\nPlease Check Your Password",icon = "warning", option_1="OK")


#==================Warn User for empty credential=========================================
def warn_for_empty_credential():
    registration_message = CTkMessagebox(title = "Empty Credential", message = "Provide accurate credentials",icon = "warning", option_1="OK")


#==================sign up to account=========================================
def signup_account():
    #print(signupemail_entry.get()," and ",signuppass_entry.get(),"and", namesignup_entry.get())
    name = namesignup_entry.get()
    email = signupemail_entry.get()
    pwd = signuppass_entry.get()
    if email.endswith("@gmail.com") and name!="" and len(pwd)>=5:
        sql_for_account_creation = f"INSERT INTO learner (email,name,code) values('{email}','{name}','{pwd}')"
        sql_for_check_existence = f"SELECT email From learner where email = '{email}'"
        cur.execute(sql_for_check_existence)
        total_accounts = cur.fetchall()
        if len(total_accounts)!=0:
            warn_existence()
        else:
            cur.execute(sql_for_account_creation)
            con.commit()
            welcome_new_user()
            signup_frame.pack_forget()
    else:
        warn_new_user()

##==================Dashboard Creation=========================================
def dashboard():
    image_frame.pack_forget()
    welcome_frame.pack_forget()
    mytab = CTkTabview(app, width = 800, height = 550)
    mytab.pack(side = RIGHT, expand = True, fill = Y)
    tab1 = mytab.add("Tab_1")
    tab2 = mytab.add("Tab_2")
    l1 = CTkLabel(tab1, text = "Hello", font=("Arial", 30))
    l1.pack()
    frame = CTkFrame(app, width = 200, height = 550)
    frame.pack(side= LEFT, expand = True, fill = Y)
    b1 = CTkButton(tab2, text="Play")
    b1.pack()
    b4 = CTkButton(tab2, text="Stop")
    b4.pack()
    b2 = CTkButton(frame, text="Pause")
    b2.pack()
    b3 = CTkButton(frame, text="Unpause")

    b1 = CTkButton(frame, text="Hello")
    b1.pack()

#==================Login to account=========================================
def login_account():
    email = email_entry.get()
    pwd = pass_entry.get()
    if len(email)>0 and len(pwd)>0:
        sql = f"SELECT * FROM learner where email = '{email}'"
        cur.execute(sql)
        result = cur.fetchall()
        if len(result) == 0:
            warn_for_create_account()
        else:
            if result[0][2] != pwd:
                warn_for_invalid_credential(result[0][1])
            else:
                dashboard()
    else:
        warn_for_empty_credential()



#==================go to welcome btn frame - signup=========================================
def cancel_signup_account():
    signup_frame.pack_forget()
    welcome_btn_frame.pack(side=BOTTOM, pady=10, padx=10, fill=BOTH, expand=True)


#==================image frame=========================================
image_frame = CTkFrame(master = app, width = 650, corner_radius=3,border_width=3, border_color="green")
image_frame.pack(side = LEFT, fill = BOTH, expand = True)

#==================Welcome Frame=========================================
welcome_frame = CTkFrame(master = app, width = 350, corner_radius=5,border_width=3, border_color="red")
welcome_frame.pack(side = RIGHT,padx = 1,fill = BOTH, expand = True)
#========welcome frame label============
welcome_label = CTkLabel(welcome_frame, text="Welcome\nTo\nPlanet Dynamics!!", font = ("Comic Sans MS", 28))
welcome_label.pack(pady=10)
#==================Welcome Button Frame=========================================
welcome_btn_frame = CTkFrame(welcome_frame,fg_color="blue",width=350)
welcome_btn_frame.pack(side = BOTTOM ,pady = 10, padx = 10,fill = BOTH, expand = True)
#welcome_btn_frame.pack_forget()
#========Login Frame Raise Button=========
login_page = CTkButton(welcome_btn_frame, text="Login", font=("Comic Sans MS", 15), corner_radius=7, border_width = 3, command = login_frame_raise)
login_page.pack(expand = True)
#===========OR Label==========
or_label =  CTkLabel(welcome_btn_frame, text="OR", font = ("Comic Sans MS", 15), text_color="white")
or_label.pack()
#===========SignUp Frame Raise Button========
signup_page = CTkButton(welcome_btn_frame, text="Be a Member Today!", font=("Comic Sans MS", 15), corner_radius=7, border_width = 3, command = signup_frame_raise)
signup_page.pack(expand = True)
#==================Login Frame=========================================
login_frame = CTkFrame(welcome_frame,fg_color="red",width=350)
login_frame.pack(side = BOTTOM ,pady = 10, padx = 10,fill = BOTH, expand = True)
login_frame.pack_forget()
#==================positioning frame=========================================
gap_frame = CTkFrame(login_frame,height=100,fg_color="red")
gap_frame.pack()
#==========Login Frame Email==========
email_entry = CTkEntry(login_frame, placeholder_text="Email", width = 300, corner_radius=7, font = ("Arial",15))
email_entry.pack(ipady = 10,pady= 10)
#=======Login Frame Pass=====
pass_entry = CTkEntry(login_frame, placeholder_text="Password", width = 300, corner_radius=7, font = ("Arial",15))
pass_entry.pack(ipady = 10)
#=======Login Button======
login_btn = CTkButton(login_frame, text="Login", font=("Comic Sans MS", 15), corner_radius=7, border_width = 3, command = login_account)
login_btn.pack(side = LEFT,expand = True)

cancel_login_btn = CTkButton(login_frame, text="Cancel", font=("Comic Sans MS", 15), corner_radius=7, border_width = 3, command = cancel_login_account)
cancel_login_btn.pack(side = LEFT,expand = True)

#=====================Sign Up Frame==================================================
signup_frame = CTkFrame(welcome_frame,fg_color="yellow",width=350)
signup_frame.pack(side = BOTTOM ,pady = 10, padx = 10,fill = BOTH, expand = True)
signup_frame.pack_forget()
#====positioning frame=======
gap_frame = CTkFrame(signup_frame,height=100,fg_color="yellow")
gap_frame.pack()
#========Sign up Frame Name (namesignup_entry)========
namesignup_entry = CTkEntry(signup_frame, placeholder_text="Name", width = 300, corner_radius=7, font = ("Arial",15))
namesignup_entry.pack(ipady = 10,pady= 10)
#======Sign Up Frame Email================
signupemail_entry = CTkEntry(signup_frame, placeholder_text="Email", width = 300, corner_radius=7, font = ("Arial",15))
signupemail_entry.pack(ipady = 10,pady= 10)
#=====Sign Up Frame Pass=========
signuppass_entry = CTkEntry(signup_frame, placeholder_text="Password", width = 300, corner_radius=7, font = ("Arial",15))
signuppass_entry.pack(ipady = 10,pady = 10)
#=====Sign Up Button=========
signup_btn = CTkButton(signup_frame, text="Sign Up", font=("Comic Sans MS", 15), corner_radius=7, border_width = 3, command = signup_account)
signup_btn.pack(side = LEFT,expand = True)

cancel_signup_btn = CTkButton(signup_frame, text="Cancel", font=("Comic Sans MS", 15), corner_radius=7, border_width = 3, command = cancel_signup_account)
cancel_signup_btn.pack(side = LEFT,expand = True)

#=======Login Button=========
login_btn = CTkButton(signup_frame, text="Login", font=("Comic Sans MS", 15), corner_radius=7, border_width = 3, command = login_part)
login_btn.pack(side = BOTTOM,expand = True)

#login_frame.pack_forget()

app.mainloop()