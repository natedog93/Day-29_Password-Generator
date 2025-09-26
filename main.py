from tkinter import *
from tkinter import messagebox
import random
#message box is not a class, so have to import sepparately


#Constants
YELLOW = "#f7f5dd"
FONT_NAME = "Helvetica"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_random_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    [password_list.append(random.choice(letters)) for letter in range(random.randint(8,10))]
    [password_list.append(random.choice(symbols)) for symbol in range(random.randint(2,4))]
    [password_list.append(random.choice(numbers)) for number in range(random.randint(2, 4))]
    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, END)  # Delete all existing text
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
#TODO 1: Create a function called save()
def save():
    """Saving user inputs for website name, email/username, and password. Saving them to a
    .txt file and then deleting the user entries once they click on the add button"""
    website_name_text = website_name_input.get()
    email_username_text = email_username_input.get()
    password_text = password_input.get()

    if len(website_name_text) == 0 or len(password_text) == 0:
        messagebox.showerror(title="Error - Missing Fields", message= "Please do not leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title= website_name_text, message= f"Save the below details?\n\n Username - {email_username_text}\n\n"
                                                              f"PW - {password_text}?")
        if is_ok:
            with open("Hidden_Reference.txt", "a") as storage_file:
                storage_file.write(f"{website_name_text} | {email_username_text} | {password_text}\n")
                website_name_input.delete(0, END)
                password_input.delete(0, END)
    #Clearing all entry objects once details are saved - Leaving email entry object

# ---------------------------- UI SETUP ------------------------------- #

window = Tk() #Creating the window
window.title("Password Manager")
#create some padding between window and canvas (image)
window.config(padx = 50, pady= 50)

#Creating our canvas (image)
canvas = Canvas(width = 200, height= 200)
password_image = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = password_image)
canvas.grid(column = 1, row = 0)

#Labels
website_name_label = Label(text="Website:")
website_name_label.grid(column = 0, row = 1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column = 0, row = 2)

password_label = Label(text="Password:")
password_label.grid(column = 0, row = 3)

#Entries
website_name_input = Entry(width= 52)
website_name_input.grid(column = 1, row = 1, columnspan= 2)
website_name_input.focus()

email_username_input = Entry(width= 52)
email_username_input.grid(column = 1, row = 2, columnspan= 2)
email_username_input.insert(0, "nmlogon2700@gmail.com") #index of 0 would be inserting text at the very beginning of the entry vs END.

password_input = Entry(show="*", width= 33)
password_input.grid(column = 1, row = 3)

#Buttons
generate_password_button = Button(text= "Generate Password", command=generate_random_password)
generate_password_button.grid(column = 2, row = 3)

add_button = Button(text="Add", width = 44, command=save)
add_button.grid(column= 1, row = 4, columnspan= 2)

window.mainloop()