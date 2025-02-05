
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import time

def calculate_age():
    try:
        birth_date = datetime.strptime(birth_entry.get(), "%Y-%m-%d")
        if custom_date_entry.get():
            custom_date = datetime.strptime(custom_date_entry.get(), "%Y-%m-%d")
            current_date = custom_date
        else:
            current_date = datetime.now()

        delta = current_date - birth_date
        total_seconds = delta.total_seconds()

        years = int(total_seconds // (365.25 * 24 * 3600))
        remaining_seconds = total_seconds % (365.25 * 24 * 3600)
        months = int(remaining_seconds // (30.44 * 24 * 3600))
        remaining_seconds %= (30.44 * 24 * 3600)
        days = int(remaining_seconds // (24 * 3600))
        remaining_seconds %= (24 * 3600)
        hours = int(remaining_seconds // 3600)
        remaining_seconds %= 3600
        minutes = int(remaining_seconds // 60)

        current_time = time.strftime("%H:%M:%S")

        result_label.config(text=f"Age: {years} years, {months} months, {days} days\n"
                                 f"{hours} hours, {minutes} minutes\n"
                                 f"Current time: {current_time}")

    except ValueError:
        messagebox.showerror("Invalid Date Format", "Please enter the date in YYYY-MM-DD format.")

# Main application window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("450x350")

# Labels and entry fields
tk.Label(root, text="Enter Birth Date (YYYY-MM-DD):").pack(pady=5)
birth_entry = tk.Entry(root, width=30)
birth_entry.pack(pady=5)

tk.Label(root, text="Enter Custom Date (YYYY-MM-DD) [Optional]:").pack(pady=5)
custom_date_entry = tk.Entry(root, width=30)
custom_date_entry.pack(pady=5)

# Calculate Button
tk.Button(root, text="Calculate Age", command=calculate_age).pack(pady=10)

# Result Label
result_label = tk.Label(root, text="Age: ", font=("Helvetica", 12), justify="left")
result_label.pack(pady=10)

# Run the application
root.mainloop()
