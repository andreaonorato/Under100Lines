import tkinter as tk
from tkinter import ttk
import random
import string


def generate_password():
    password_length = int(length_entry.get())
    include_numbers = numbers_var.get()
    include_symbols = symbols_var.get()

    characters = string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


def check_strength():
    password = password_entry.get()

    # Define criteria for strong password
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)
    length_ok = len(password) >= 8

    # Evaluate strength
    strength = ""
    if length_ok and has_upper and has_lower and has_digit and has_symbol:
        strength = "Very Strong"
    elif length_ok and (has_upper or has_lower) and has_digit and has_symbol:
        strength = "Strong"
    elif length_ok and (has_upper or has_lower) and has_digit:
        strength = "Moderate"
    elif length_ok and (has_upper or has_lower):
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Set appropriate text and color based on strength
    strength_label.config(text=strength, foreground="green" if strength in ["Strong", "Very Strong"] else "red")



# Create Tkinter window
root = tk.Tk()
root.title("Password Generator")

# Length Entry
length_label = ttk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

length_entry = ttk.Entry(root, width=10)
length_entry.grid(row=0, column=1, padx=5, pady=5)
length_entry.insert(0, "12")  # Default length

# Numbers Checkbox
numbers_var = tk.BooleanVar(value=True)  # Set initial value to True (checked)
numbers_checkbox = ttk.Checkbutton(root, text="Include Numbers", variable=numbers_var)
numbers_checkbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="w")

# Symbols Checkbox
symbols_var = tk.BooleanVar(value=True)  # Set initial value to True (checked)
symbols_checkbox = ttk.Checkbutton(root, text="Include Symbols", variable=symbols_var)
symbols_checkbox.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="w")


# Generate Button
generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Password Entry
password_label = ttk.Label(root, text="Generated Password:")
password_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")

password_entry = ttk.Entry(root, width=30)
password_entry.grid(row=4, column=1, padx=5, pady=5)

# Strength Check Button
strength_button = ttk.Button(root, text="Check Strength", command=check_strength)
strength_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Strength Label
strength_label = ttk.Label(root, text="")
strength_label.grid(row=6, column=0, columnspan=2, padx=5, pady=5)


root.mainloop()
