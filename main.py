from tkinter import *

YELLOW = "#f7f5dd"
FONT_NAME = "Helvetica"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk() #Creating the window
window.title("Password Manager")
#create some padding between window and canvas (image)
window.config(padx = 20, pady= 20)

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

password_input = Entry(width= 33)
password_input.grid(column = 1, row = 3)

#Buttons
generate_password_button = Button(text= "Generate Password")
generate_password_button.grid(column = 2, row = 3)

add_button = Button(text="Add", width = 44)
add_button.grid(column= 1, row = 4, columnspan= 2)

window.mainloop()