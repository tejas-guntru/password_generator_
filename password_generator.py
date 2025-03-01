import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())
        if length < 4:
            messagebox.showerror("Error", "Password length should be at least 4")
            return
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(entry_password.get())
    root.update()
    messagebox.showinfo("Success", "Password copied to clipboard")

def login():
    username = entry_username.get()
    reason = entry_reason.get()
    if username.strip() and reason.strip():
        login_window.destroy()
        open_password_generator()
    else:
        messagebox.showerror("Error", "Please enter both username and reason")

def open_password_generator():
    global root, entry_length, entry_password
    root = tk.Tk()
    root.title("Password Generator")
    root.geometry("400x250")
    root.resizable(False, False)
    root.configure(bg="#2c3e50")  # Background color

    tk.Label(root, text="Password Length:", font=("Arial", 12), fg="white", bg="#2c3e50").pack(pady=5)
    entry_length = tk.Entry(root, font=("Arial", 12), bg="#ecf0f1", fg="black")
    entry_length.pack(pady=5)

    tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12), bg="#3498db", fg="white").pack(pady=5)
    entry_password = tk.Entry(root, font=("Arial", 12), width=30, bg="#ecf0f1", fg="black")
    entry_password.pack(pady=5)

    tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 12), bg="#e74c3c", fg="white").pack(pady=5)
    root.mainloop()

# Login Window
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x200")
login_window.resizable(False, False)
login_window.configure(bg="#34495e")

tk.Label(login_window, text="Username:", font=("Arial", 12), fg="white", bg="#34495e").pack(pady=5)
entry_username = tk.Entry(login_window, font=("Arial", 12), bg="#ecf0f1", fg="black")
entry_username.pack(pady=5)

tk.Label(login_window, text="Reason for Password Generation:", font=("Arial", 12), fg="white", bg="#34495e").pack(pady=5)
entry_reason = tk.Entry(login_window, font=("Arial", 12), bg="#ecf0f1", fg="black")
entry_reason.pack(pady=5)

tk.Button(login_window, text="Login", command=login, font=("Arial", 12), bg="#27ae60", fg="white").pack(pady=10)

login_window.mainloop()
