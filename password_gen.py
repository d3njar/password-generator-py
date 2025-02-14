import customtkinter as ctk
import random
import string
import pyperclip

# Initialize the app
ctk.set_appearance_mode("dark") # Themes are "System", "Dark", "Light"
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("400x300")
app.title("Password Generator")

# Function to generate a password
def generate_password():
    length = length_slider.get()
    characters = string.ascii_letters
    if numbers_var.get():
        characters += string.digits
    if special_var.get():
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(int(length)))
    password_entry.delete(0, "end")
    password_entry.insert(0, password)

# Function to copy the password
def copy_password():
    pyperclip.copy(password_entry.get())
        
# UI Elements
ctk.CTkLabel(app, text="Select Password Length:").pack(pady=5)
length_slider = ctk.CTkSlider(app, from_=4, to=32, number_of_steps=28)
length_slider.pack(pady=5)
length_slider.set(12)

numbers_var = ctk.BooleanVar()
special_var = ctk.BooleanVar()

ctk.CTkCheckBox(app, text="Include Numbers", variable=numbers_var).pack(pady=3)
ctk.CTkCheckBox(app, text="Include Special Characters", variable=special_var).pack(pady=3)

password_entry = ctk.CTkEntry(app, width=250)
password_entry.pack(pady=10)

button_frame = ctk.CTkFrame(app)
button_frame.pack()

generate_button = ctk.CTkButton(button_frame, text="Generate", command=generate_password)
generate_button.grid(row=0, column=0, padx=5)

copy_button = ctk.CTkButton(button_frame, text="Copy", command=copy_password)
copy_button.grid(row=0, column=1, padx=5)

app.mainloop()