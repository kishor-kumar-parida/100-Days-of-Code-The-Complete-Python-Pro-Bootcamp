import tkinter
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


def generate():
    P_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]

    P_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    P_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = P_letters + P_numbers + P_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {"email": email, "password": password}}

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Warning", message="Please don't leave any fields blank."
        )
    else:
        try:
            with open("data.json", "r") as data_file:
                # Try reading old data
                data = json.load(data_file)
        except (FileNotFoundError, json.JSONDecodeError):
            # If file not found or empty/corrupted file, initialize data as empty dictionary
            data = {}

        # Update old data with new data
        data.update(new_data)

        with open("data.json", "w") as data_file:
            # Save updated data
            json.dump(data, data_file, indent=4)

        # Clear entries after saving
        website_entry.delete(0, tkinter.END)
        password_entry.delete(0, tkinter.END)


# ---------------------------- FIND PASSWORD ------------------------------- #


def search():
    website = website_entry.get()

    try:
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data Found")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website, message=f"Email: {email}\nPassword: {password}"
            )

        else:
            messagebox.showinfo(title="Error", message="No details exists")


# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Password Manager App")
window.config(padx=50, pady=50)

# Canvas for logo
canvas = tkinter.Canvas(height=200, width=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, pady=5)

# Labels
website_label = tkinter.Label(text="Website :")
website_label.grid(row=1, column=0, padx=5, pady=5)

email_label = tkinter.Label(text="Email / Username :")
email_label.grid(row=2, column=0, padx=5, pady=5)

password_label = tkinter.Label(text="Password :")
password_label.grid(row=3, column=0, padx=5, pady=5)

# Entries
website_entry = tkinter.Entry(width=35)
website_entry.grid(row=1, column=1, padx=5, pady=5)
website_entry.focus()

email_entry = tkinter.Entry(width=35)
email_entry.grid(row=2, column=1, padx=5, pady=5)
email_entry.insert(0, "example@gmail.com")

password_entry = tkinter.Entry(width=35)
password_entry.grid(row=3, column=1, padx=5, pady=5)

# Buttons
search_button = tkinter.Button(text="Search", command=search)
search_button.grid(row=1, column=2, padx=5, pady=5)

generate_password_button = tkinter.Button(text="Generate Password", command=generate)
generate_password_button.grid(row=3, column=2, padx=5, pady=5)

add_button = tkinter.Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, padx=5, pady=5)


window.mainloop()
