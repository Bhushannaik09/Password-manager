from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

PINK = "#e2979c"
RED = "#e7298b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLUE = "#3498dd"
FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ---------------------------- #

def Generate_Password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    pass_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD --------------------------------- #

def Save():

    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {website:{
        "Email": email,
        "Password": password
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please enter all fields")
    else:

        # is_ok = messagebox.askokcancel(title=website, message=f"These are the detailed entered: \nEmail: {email} "
        #                                                       f"\nPassword: {password} \n Is it ok to save?")
        # if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    #Reading old data
                    data = json.load(data_file)

            except:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                #Updating old data eith new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    #Saving updated data
                    json.dump(data, data_file, indent=4)

            finally:
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                pass_entry.delete(0, END)



# ---------------------------- FIND PASSWORD --------------------------------- #

def Find_Password():
    website = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except:
        messagebox.showinfo(title="Error", message="No Data File Found.")

    else:
        if website in data:
            email = data[website]["Email"]
            password = data[website]["Password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")









# ---------------------------- UI SETUP -------------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website : ")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username :")
email_label.grid(row=2, column=0)
pass_label = Label(text="Password :")
pass_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "naikbhushan101@gmail.com")
pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

#Buttons
pass_gen_button = Button(text="Generate Password", command=Generate_Password)
pass_gen_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=Save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", command=Find_Password, width=13)
search_button.grid(row=1, column=2)











window.mainloop()
