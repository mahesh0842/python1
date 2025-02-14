import tkinter as tk
from datetime import datetime
import pandas as pd

def on_enter(event):
    event.widget.tk_focusNext().focus()
    return "break"

def calculate_total():
    total_sum = 0
    for i in range(12):  # Update loop to handle 12 persons
        # Handle cow milk input
        try:
            cow_milk = float(entries_cow[i].get())
        except ValueError:
            cow_milk = 0.0
        
        # Handle buffalo milk input
        try:
            buffalo_milk = float(entries_buffalo[i].get())
        except ValueError:
            buffalo_milk = 0.0
        
        # Calculate and display totals
        total_price = (cow_milk * 40) + (buffalo_milk * 62)
        total_labels[i].config(text=f"₹{total_price:.2f}")
        total_sum += total_price
    
    # Update grand total and reset focus
    total_all_label.config(text=f"Grand Total: ₹{total_sum:.2f}")
    entries_cow[0].focus_set()

def save_to_excel():
    # Create a dictionary to store the data
    data = {
        "Person": names,
        "Cow Milk (L)": [float(entries_cow[i].get() or 0) for i in range(12)],
        "Buffalo Milk (L)": [float(entries_buffalo[i].get() or 0) for i in range(12)],
        "Total (₹)": [float(total_labels[i].cget("text").replace("₹", "")) for i in range(12)]
    }
    
    # Create a DataFrame
    df = pd.DataFrame(data)
    
    # Save to Excel
    filename = f"Milk_Data_{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.xlsx"
    df.to_excel(filename, index=False)
    
    # Show confirmation message
    confirmation_label.config(text=f"Data saved to {filename}")

# Create main window
root = tk.Tk()
root.title("Milk Cost Calculator")
root.geometry("600x500")

# Configure grid layout
root.columnconfigure(0, weight=1)
root.columnconfigure(3, weight=1)

# Create headers
headers = ["Person", "Cow Milk (L)", "Buffalo Milk (L)", "Total"]
for col, text in enumerate(headers):
    tk.Label(root, text=text, width=15, relief="ridge").grid(row=0, column=col, padx=2, pady=2, sticky="ew")

# List of permanent names
names = [
    "Krishna", "New-sai", "Om sai", "Shree sai", "Sunil", "sai", 
    "Anil", "Dinesh", "Subash", "ravi-dairy", "Shyamdhar", "Bhola"
]

entries_cow = []
entries_buffalo = []
total_labels = []

# Create input rows
for i in range(12):
    row = i + 1
    
    # Person name label (permanent)
    tk.Label(root, text=names[i], relief="groove").grid(row=row, column=0, padx=2, pady=2, sticky="ew")
    
    # Cow milk entry
    cow_entry = tk.Entry(root, width=10, justify="center")
    cow_entry.grid(row=row, column=1, padx=2, pady=2)
    cow_entry.bind("<Return>", on_enter)
    entries_cow.append(cow_entry)
    
    # Buffalo milk entry
    buffalo_entry = tk.Entry(root, width=10, justify="center")
    buffalo_entry.grid(row=row, column=2, padx=2, pady=2)
    buffalo_entry.bind("<Return>", on_enter)
    entries_buffalo.append(buffalo_entry)
    
    # Total label
    total_label = tk.Label(root, text="₹0.00", relief="sunken")
    total_label.grid(row=row, column=3, padx=2, pady=2, sticky="ew")
    total_labels.append(total_label)

# Calculate button (smaller size)
tk.Button(root, text="Calculate", command=calculate_total, 
         bg="#4CAF50", fg="BLACK", width=10).grid(row=13, column=1, pady=10)

# Save to Excel button
tk.Button(root, text="Save to Excel", command=save_to_excel, 
         bg="#2196F3", fg="BLACK", width=10).grid(row=13, column=2, pady=10)

# Get current date
current_date = datetime.now().strftime("%d-%m-%Y")

# Date and Grand Total display
date_label = tk.Label(root, text=f"Date: {current_date}", 
                     font=("Arial", 10), bg="#333", fg="white")
date_label.grid(row=13, column=0, padx=2, pady=10, sticky="ew")

total_all_label = tk.Label(root, text="Grand Total: ₹0.00", 
                          font=("Arial", 10, "bold"), bg="#333", fg="white")
total_all_label.grid(row=13, column=3, padx=2, pady=10, sticky="ew")

# Confirmation label for saving to Excel
confirmation_label = tk.Label(root, text="", fg="green", font=("Arial", 10))
confirmation_label.grid(row=14, column=0, columnspan=4, pady=10)

# Start with first entry focused
entries_cow[0].focus_set()

root.mainloop()