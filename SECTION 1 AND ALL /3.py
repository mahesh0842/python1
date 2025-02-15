import tkinter as tk
from datetime import datetime
import pandas as pd
import os
import subprocess

# Constants
COW_MILK_PRICE = 40  # Price per liter
BUFFALO_MILK_PRICE = 62  # Price per liter
SAVE_FOLDER = "Milk_Data_Records"

# Ensure save folder exists
if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)

# List of permanent names
NAMES = [
    "Krishna", "New-sai", "Om sai", "Shree sai", "Sunil", "sai", 
    "Anil", "Dinesh", "Subash", "ravi-dairy", "Shyamdhar", "Bhola"
]

def get_float(entry):
    """Safely gets a float from an entry widget."""
    try:
        return float(entry.get().strip()) if entry.get().strip() else 0.0
    except ValueError:
        return 0.0

def on_enter(event):
    """Move to the next entry on pressing Enter."""
    event.widget.tk_focusNext().focus()
    return "break"

def calculate_total():
    """Calculates the total cost for each person and grand total."""
    total_sum = 0
    for i in range(12):
        cow_milk = get_float(entries_cow[i])
        buffalo_milk = get_float(entries_buffalo[i])
        
        total_price = (cow_milk * COW_MILK_PRICE) + (buffalo_milk * BUFFALO_MILK_PRICE)
        total_labels[i].config(text=f"₹{total_price:.2f}")
        total_sum += total_price
    
    total_all_label.config(text=f"Grand Total: ₹{total_sum:.2f}")
    entries_cow[0].focus_set()
    return total_sum

def save_to_excel():
    """Saves data to an Excel file and opens it automatically."""
    total_sum = calculate_total()
    
    data = {
        "Person": NAMES,
        "Cow Milk (L)": [get_float(entries_cow[i]) for i in range(12)],
        "Buffalo Milk (L)": [get_float(entries_buffalo[i]) for i in range(12)],
        "Total (₹)": [float(total_labels[i].cget("text").replace("₹", "")) for i in range(12)]
    }
    
    df = pd.DataFrame(data)
    grand_total_row = pd.DataFrame({
        "Person": ["Grand Total"],
        "Cow Milk (L)": [""],
        "Buffalo Milk (L)": [""],
        "Total (₹)": [total_sum]
    })
    
    df = pd.concat([df, grand_total_row], ignore_index=True)
    filename = f"Milk_Data_{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.xlsx"
    filepath = os.path.join(SAVE_FOLDER, filename)
    df.to_excel(filepath, index=False)
    
    confirmation_label.config(text=f"Data saved to {filepath}")
    
    # Open the Excel file automatically
    subprocess.run(["open", filepath], check=True)

# Create main window
root = tk.Tk()
root.title("Milk Cost Calculator")
root.geometry("600x500")

# Create headers
headers = ["Person", "Cow Milk (L)", "Buffalo Milk (L)", "Total"]
for col, text in enumerate(headers):
    tk.Label(root, text=text, width=15, relief="ridge").grid(row=0, column=col, padx=2, pady=2, sticky="ew")

entries_cow, entries_buffalo, total_labels = [], [], []

# Create input rows
for i in range(12):
    row = i + 1
    tk.Label(root, text=NAMES[i], relief="groove").grid(row=row, column=0, padx=2, pady=2, sticky="ew")
    
    cow_entry = tk.Entry(root, width=10, justify="center")
    cow_entry.grid(row=row, column=1, padx=2, pady=2)
    cow_entry.bind("<Return>", on_enter)
    entries_cow.append(cow_entry)
    
    buffalo_entry = tk.Entry(root, width=10, justify="center")
    buffalo_entry.grid(row=row, column=2, padx=2, pady=2)
    buffalo_entry.bind("<Return>", on_enter)
    entries_buffalo.append(buffalo_entry)
    
    total_label = tk.Label(root, text="₹0.00", relief="sunken")
    total_label.grid(row=row, column=3, padx=2, pady=2, sticky="ew")
    total_labels.append(total_label)

# Buttons
tk.Button(root, text="Calculate", command=calculate_total, bg="#4CAF50", fg="BLACK", width=10).grid(row=13, column=1, pady=10)
tk.Button(root, text="Save to Excel", command=save_to_excel, bg="#2196F3", fg="BLACK", width=10).grid(row=13, column=2, pady=10)

# Date and Grand Total display
date_label = tk.Label(root, text=f"Date: {datetime.now().strftime('%d-%m-%Y')}", font=("Arial", 10), bg="#333", fg="white")
date_label.grid(row=13, column=0, padx=2, pady=10, sticky="ew")

total_all_label = tk.Label(root, text="Grand Total: ₹0.00", font=("Arial", 10, "bold"), bg="#333", fg="white")
total_all_label.grid(row=13, column=3, padx=2, pady=10, sticky="ew")

# Confirmation label
confirmation_label = tk.Label(root, text="", fg="green", font=("Arial", 10))
confirmation_label.grid(row=14, column=0, columnspan=4, pady=10)

entries_cow[0].focus_set()
root.mainloop()
