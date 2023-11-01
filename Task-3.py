# Task No:3 Password Generator
#CodSoft

from tkinter import *
import random
import string
from tkinter import messagebox

win =Tk()
win.title("Password Generator")
win.minsize(width=280,height=200)
win.maxsize(width=280,height=200)

label1=Label(text="* Password Generator System *",font=('Fantasy 12 bold'),bg='black',fg='white')
label1.place(x=3,y=13,width=273)

length_label = Label(win, text="Enter Password Length:",font=('Fantasy 10 bold'),fg='black')
length_label.place(x=60,y=60)

length_entry = Entry(win,font=('Fantasy 14 bold'))
length_entry.place(x=90,y=85,height=25,width=80)

def generate_password():
    password_length =length_entry.get()    
    if (password_length != ""):
        if str.isdigit(password_length):
            password_length2=int(password_length)
            if password_length2 < 8:
                messagebox.showinfo("showinfo", "Password length must be at least 8")
            else:
                characters = string.ascii_letters + string.digits + string.punctuation
                password = ''.join(random.choice(characters) for _ in range(password_length2))
                messagebox.showinfo("Generated Password ",password).width(width=300)
        else:
            messagebox.showwarning("showwarning","Enter Valid Length")
    else:
        messagebox.showwarning("showwarning","Enter Password Length")
        
btn =Button(win, text="Generate Password",font=('Fantasy 10 bold'),bg='green',fg='white',bd=3,command=generate_password)
btn.place(x=60,y=130)

win.mainloop()