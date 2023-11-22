from tkinter import *
from tkinter import messagebox
import random
import pyperclip

counter = 0


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]

    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    result = "".join(password_list)

    password_entry.insert(0, string=f"{result}")

    pyperclip.copy(result)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    global counter
    counter += 1
    website = web_entry.get()
    e_mail = email_entry.get()
    pass_word = password_entry.get()

    if len(website) == 0 or len(pass_word) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {e_mail} "
                                                              f"\nPassword: {pass_word} \nIs it ok to save?")
        if is_ok:
            with open("password.txt", mode='a') as password_file:
                password_file.write(f"{counter}. {website} | {e_mail} | {pass_word} \n")
                web_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(pady=20, padx=20)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# website
web_name = Label(text='Website: ')
web_name.grid(row=1, column=0)
web_entry = Entry(width=40)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

# email
email = Label(text='Email/Username: ')
email.grid(row=2, column=0)
email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "princenims1994@gmail.com")

# password
password = Label(text='Password: ')
password.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
generate = Button(text='Generate Password', command=generate_password)
generate.grid(row=3, column=2)

# add
add = Button(text="Add", width=38, command=save_password)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
