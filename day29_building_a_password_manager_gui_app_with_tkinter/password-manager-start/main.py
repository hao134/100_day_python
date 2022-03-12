from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #]
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == "" or password == "":
        messagebox.showwarning(title="OOps", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                web_entry.delete(0,END)
                password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100,image=logo_img)
canvas.grid(column=1,row=0)

website = Label(text="Website: ")
website.grid(column=0,row=1)

web_entry = Entry(width = 35)
web_entry.grid(column=1,row=1,columnspan=2)
web_entry.focus()

email_user = Label(text="Email/Username:")
email_user.grid(column=0,row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0, "example@email.com")

password = Label(text = "Password:")
password.grid(column=0,row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_buttom = Button(text="Generate Password",command=generate_password)
generate_buttom.grid(column=2, row=3)

add_buttom = Button(text="Add",width=36, command = save)
add_buttom.grid(column=1,row=4,columnspan=2)



window.mainloop()