import json
from tkinter import *
import pyperclip
from tkinter import messagebox
from random import randint, shuffle, choice

# ---------------------------- SAVE PASSWORD ------------------------------- #


def search():
    with open("data.json") as data_file:
        website = website_input.get()
        data = json.load(data_file)
        try:
            messagebox.showinfo(title=website, message=f"Email: {data[website]['email']} \nPassword: "
                                                       f"{data[website]['password']}")
        except KeyError:
            messagebox.showerror(title="error", message="The website that you wrote is empty")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for char in range(randint(8, 10))]
    symbols_list = [choice(symbols) for char in range(randint(2, 4))]
    numbers_list = [choice(numbers) for char in range(randint(2, 4))]
    password_list = letter_list + symbols_list + numbers_list

    shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)

    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_info():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please, don't leave any of the fields empty")

    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w+") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(height=200, width=250)
mypass_img = PhotoImage(file="logo.png")
canvas.create_image(170, 100, image=mypass_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry()
website_input.focus()
website_input.grid(column=1, row=1, sticky="EW", pady=3)

search_button = Button(text="Search", bd=1, command=search)
search_button.grid(column=2, row=1, sticky="EW", padx=(3, 0))

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_input = Entry()
email_input.insert(0, "justthunterr@gmail.com")
email_input.grid(column=1, row=2, columnspan=2, sticky="EW", pady=3)

password_label = Label(text="Password:", pady=2)
password_label.grid(column=0, row=3)

password_input = Entry()
password_input.grid(column=1, row=3, sticky="EW", pady=3)

generate_button = Button(text="Generate Password", command=generate_password, bd=1)
generate_button.grid(column=2, row=3, sticky="EW", padx=(3, 0))

add_button = Button(text="Add", width=36, command=save_info, bd=1)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW", pady=3)

window.mainloop()
