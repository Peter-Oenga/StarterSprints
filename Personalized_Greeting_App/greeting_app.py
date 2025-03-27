import tkinter as tk
from tkinter import messagebox

# Function to display greeting
def show_greeting():
    name = name_entry.get()
    color = color_entry.get()
    
    if name and color:
        messagebox.showinfo("Greeting", f"Hello, {name}! Your favorite color, {color}, is awesome!")
    else:
        messagebox.showwarning("Input Error", "Please enter both your name and favorite color.")

# Create the main window
root = tk.Tk()
root.title("Personalized Greeting App")

# Create labels and entry fields
tk.Label(root, text="Enter your name:").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter your favorite color:").grid(row=1, column=0, padx=10, pady=5)
color_entry = tk.Entry(root)
color_entry.grid(row=1, column=1, padx=10, pady=5)

# Create the submit button
submit_button = tk.Button(root, text="Greet Me!", command=show_greeting)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
