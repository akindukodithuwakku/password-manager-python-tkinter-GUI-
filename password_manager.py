import os
from tkinter import *
import random
from tkinter import messagebox
import pyperclip

# Constants
WHITE = "#FFFFFF"
AnimatedFont = "Courier"

# Path to the image file
script_dir = os.path.dirname(__file__)
image_path = os.path.join(script_dir , 'logo.png')


# Function to create a random password
def generatePwd():
    letters = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' ,
               'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' , 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' ,
               'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' ,
               'Z']
    numbers = ['0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']
    symbols = ['!' , '#' , '$' , '%' , '&' , '(' , ')' , '*' , '+']

    letter = random.randint(8 , 10)
    symbol = random.randint(2 , 4)
    number = random.randint(2 , 4)

    pwdList = []

    for x in range(letter):
        pwdList.append(random.choice(letters))
    for x in range(symbol):
        pwdList.append((random.choice(symbols)))
    for x in range(number):
        pwdList.append((random.choice(numbers)))

    random.shuffle(pwdList)

    password = "".join(pwdList)

    pwd_entry.insert(0 , password)
    pyperclip.copy(password)


# Function to save data
def saveData():
    website = web_entry.get()
    email = email_entry.get()
    password = pwd_entry.get()

    if (len(website or email or password) == 0):
        messagebox.showwarning(title="oops" , message="Some fields are empty.")
    else:
        is_ok = messagebox.askyesno(title=website , message=f"These are the details to save"
                                                            f"\n Email:{email} \nPassword:{password}\n"
                                                            f"Do You want to save them?")

        if is_ok:
            with open("mypasswords.txt" , "a") as data_file:
                data_file.write(f"{website} | {email} | {password} \n")
                web_entry.delete(0 , END)
                pwd_entry.delete(0 , END)
                email_entry.delete(0 , END)


# UI Setup
window = Tk()
window.title("My Password Manager")
window.config(padx=20 , pady=20)

title = Label(window , text="Password Manager" , font=(AnimatedFont , 35))
title.grid(column=0 , row=0 , columnspan=3 , pady=10)

canvas = Canvas(window , height=200 , width=200 , bg=WHITE)
password_img = PhotoImage(file=image_path)
canvas.create_image(100 , 100 , image=password_img)
canvas.grid(column=1 , row=1 , pady=10)

websiteName = Label(window , text="Website:")
websiteName.grid(column=0 , row=2 , sticky=E)
web_entry = Entry(window , width=35)
web_entry.grid(column=1 , row=2 , columnspan=2 , pady=5)

userEmail = Label(window , text="Email/Username:")
userEmail.grid(column=0 , row=3 , sticky=E)
email_entry = Entry(window , width=35)
email_entry.grid(column=1 , row=3 , columnspan=2 , pady=5)

userPassword = Label(window , text="Password:")
userPassword.grid(column=0 , row=4 , sticky=E)
pwd_entry = Entry(window , width=27)
pwd_entry.grid(column=1 , row=4 , pady=5)

generatePass = Button(window , text="Generate" , command=generatePwd)
generatePass.grid(column=2 , row=4 , padx=5 , pady=5)

addPassword = Button(window , text="ADD" , width=36 , command=saveData)
addPassword.grid(column=1 , row=5 , columnspan=2 , pady=10)

window.mainloop()
