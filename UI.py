import tkinter as tk
from tkinter import messagebox
import time


# Create a Tkinter UI for Jarvis
def create_jarvis_ui():
    # Create the main window
    root = tk.Tk()
    root.title("Jarvis - AI Assistant")
    root.geometry("400x300")  # Set the size of the window

    # Add a label
    greeting_label = tk.Label(root, text="Welcome to Jarvis!", font=("Helvetica", 16))
    greeting_label.pack(pady=10)

    # Entry for taking user input
    command_entry = tk.Entry(root, font=("Helvetica", 14), width=30)
    command_entry.pack(pady=10)

    # Button to submit command
    submit_button = tk.Button(root, text="Submit", font=("Helvetica", 14), command="")
    submit_button.pack(pady=10)

    # Label to display response
    response_label = tk.Label(root, text="", font=("Helvetica", 12), fg="blue")
    response_label.pack(pady=10)

    # Run the Tkinter event loop
    root.mainloop()

