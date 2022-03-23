from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# commands
def find_password():
    website = website_tb.get()

    try:
        with open("Day 29 Passwords.json", "r") as file:
            data = json.load(file)
            if website in data:
                email = data[website]['email']
                password = data[website]['password']
                messagebox.showinfo(title=f"{website} info:", message=f"Username:{email}\nPassword:{password}")
            else:
                messagebox.showinfo(title=f"Error", message=f"There are no saved details for: {website}")
                
    except KeyError:
        messagebox.showinfo(title="Oops", message="There is no password for the entered site.")


def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pass_letter = [random.choice(letters) for _ in range(nr_letters)]
    pass_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    pass_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = pass_letter + pass_symbols + pass_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    password_tb.insert(0, password)
    pyperclip.copy(password)


def save():
    new_data = {
        website_tb.get(): {
            "email": user_tb.get(),
            "password": password_tb.get()
        }
    }

    if len(website_tb.get()) == 0 or len(password_tb.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website_tb.get, message=f"These are the entered details:"
                                                             f"\nEmail: {user_tb.get()}"
                                                             f"\nPassword: {password_tb.get()}"
                                                             f"\nIs it ok to save?")
        if is_ok:
            with open("Day 29 Passwords.json", "r") as file:
                data = json.load(file)
                data.update(new_data)

            with open("Day 29 Passwords.json", "w") as file:
                json.dump(data, file, indent=4)
                website_tb.delete(0, END)
                password_tb.delete(0, END)


# window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=2, row=1)

# labels
website_lbl = Label(text="Website:")
user_lbl = Label(text="Email/Username:")
password_lbl = Label(text="Password:")

website_lbl.grid(column=1, row=2)
user_lbl.grid(column=1, row=3)
password_lbl.grid(column=1, row=4)

# text boxes
website_tb = Entry(width=21)
website_tb.focus()

user_tb = Entry(width=35)
user_tb.insert(0, "oscaresteban04@gmail.com")

password_tb = Entry(width=25)

website_tb.grid(column=2, row=2)
user_tb.grid(column=2, row=3, columnspan=2)
password_tb.grid(column=2, row=4)

# buttons
generate_pass = Button(text="Generate Password", command=generate_pass)
add_pass = Button(text="Add", width=36, command=save)
search = Button(text="Search", command=find_password)

generate_pass.grid(column=3, row=4, columnspan=2)
add_pass.grid(column=2, row=5, columnspan=2)
search.grid(column=3, row=2)

window.mainloop()
