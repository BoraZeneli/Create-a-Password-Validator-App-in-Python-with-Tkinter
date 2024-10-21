import tkinter as tk
from tkinter import messagebox
import string

# Function to check the password and evaluate its strength
def check_password():
    try:
        # Get the password input from the user
        password = entry_password.get()

        # Check if the password meets the minimum length requirement
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long!")

        # Initialize the criteria counters
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in string.punctuation for c in password)

        # Check if the password meets all criteria
        if not has_upper:
            raise ValueError("Password must contain at least one uppercase letter!")
        if not has_lower:
            raise ValueError("Password must contain at least one lowercase letter!")
        if not has_digit:
            raise ValueError("Password must contain at least one digit!")
        if not has_special:
            raise ValueError("Password must contain at least one special character!")

        # Evaluate password strength
        if len(password) >= 12 and has_upper and has_lower and has_digit and has_special:
            strength = "Strong"
            lbl_result.config(text="Password Strength: Strong", fg="green")
        elif has_upper and has_lower and (has_digit or has_special):
            strength = "Medium"
            lbl_result.config(text="Password Strength: Medium", fg="orange")
        else:
            strength = "Weak"
            lbl_result.config(text="Password Strength: Weak", fg="red")

    except ValueError as ve:
        messagebox.showerror("Input Error", f"Input Error: {ve}")
        lbl_result.config(text=f"Error: {ve}", fg="red")

    finally:
        # Automatically clear the input field after checking the password
        entry_password.delete(0, tk.END)

# Initial instructions to the user
def show_initial_message():
    messagebox.showinfo("Instructions", "Your password must:\n"
                                        "- Be at least 8 characters long\n"
                                        "- Contain at least one uppercase letter\n"
                                        "- Contain at least one lowercase letter\n"
                                        "- Contain at least one digit\n"
                                        "- Contain at least one special character")

# Creating the GUI using Tkinter
root = tk.Tk()
root.title("Password Validator")

# Setting the window background color
root.configure(bg="lightblue")

# Label for instructions
lbl_instruction = tk.Label(root, text="Enter your password:", font=("Arial", 12), bg="lightblue", fg="navy")
lbl_instruction.pack(pady=10)

# Entry for the password input
entry_password = tk.Entry(root, font=("Arial", 12), show="*", bg="lightyellow", fg="black")
entry_password.pack(pady=5)

# Button to trigger the password validation
btn_check = tk.Button(root, text="Check Password", command=check_password, font=("Arial", 12), bg="navy", fg="white", activebackground="lightgreen")
btn_check.pack(pady=10)

# Label to display the password strength or errors
lbl_result = tk.Label(root, text="", font=("Arial", 14), bg="lightblue")
lbl_result.pack(pady=10)

# Show initial message box with instructions
show_initial_message()

# Start the Tkinter main loop
root.mainloop()
