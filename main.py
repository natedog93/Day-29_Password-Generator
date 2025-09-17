from tkinter import *

YELLOW = "#f7f5dd"
FONT_NAME = "Helvetica"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
#TODO 1: Create a function called save()
def save():
    """Saving user inputs for website name, email/username, and password. Saving them to a
    .txt file and then deleting the user entries once they click on the add button"""
    website_name_text = website_name_input.get()
    email_username_text = email_username_input.get()
    password_text = password_input.get()

#TODO 2: Write to the data inside the entries to a data.txt file when the Add button is clicked
    with open("Hidden_Reference.txt", "a") as storage_file:
        storage_file.write(f"{website_name_text} | {email_username_text} | {password_text}\n")

    website_name_input.delete(0, END)
    password_input.delete(0, END)


#TODO 4: All fields need to be cleared after Add button is pressed



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
generate_password_button = Button(text= "Generate Password")
generate_password_button.grid(column = 2, row = 3)

add_button = Button(text="Add", width = 44, command=save)
add_button.grid(column= 1, row = 4, columnspan= 2)

window.mainloop()