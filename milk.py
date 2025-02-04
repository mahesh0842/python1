import tkinter as tk
from tkinter import ttk, filedialog
from tkcalendar import DateEntry
import pandas as pd
from datetime import datetime

def on_enter(event):
    event.widget.tk_focusNext().focus()
    return "break"

def calculate_total():
    total_sum = 0
    for i in range(10):
        # Get values with error handling
        try:
            cow_milk = float(entries_cow[i].get())
        except ValueError:
            cow_milk = 0.0
        
        try:
            buffalo_milk = float(entries_buffalo[i].get())
        except ValueError:
            buffalo_milk = 0.0
        
        # Calculate total
        total_price = (cow_milk * 40) + (buffalo_milk * 62)
        total_labels[i].config(text=f"₹{total_price:.2f}")
        total_sum += total_price
    
    total_all_label.config(text=f"Grand Total: ₹{total_sum:.2f}")
    entries_name[0].focus_set()

def save_to_excel():
    # Collect all data
    data = []
    for i in range(10):
        name = entries_name[i].get() or f"Person {i+1}"
        cow = entries_cow[i].get() or '0'
        buffalo = entries_buffalo[i].get() or '0'
        
        try:
            cow_float = float(cow)
        except ValueError:
            cow_float = 0.0
            
        try:
            buffalo_float = float(buffalo)
        except ValueError:
            buffalo_float = 0.0
        
        total = cow_float * 40 + buffalo_float * 62
        data.append([
            name,
            cow_float,
            buffalo_float,
            total,
            cal.get_date()
        ])
    
    # Create DataFrame
    df = pd.DataFrame(data, columns=["Name", "Cow Milk (L)", "Buffalo Milk (L)", "Total", "Date"])
    
    # Save file
    file_path = filedialog.asksaveasfilename(
        defaultextension=".xlsx",
        filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
    )
    if file_path:
        df.to_excel(file_path, index=False)
        tk.messagebox.showinfo("Success", "Data saved successfully!")

# Create main window
root = tk.Tk()
root.title("Milk Cost Calculator")
root.geometry("800x500")

# Date Selection
date_frame = ttk.Frame(root)
date_frame.pack(pady=13)

ttk.Label(date_frame, text="Select Date:").pack(side=tk.LEFT)
cal = DateEntry(date_frame, width=12, background='darkblue',
                foreground='white', borderwidth=2)
cal.pack(side=tk.LEFT, padx=10)

# Header Frame
header_frame = ttk.Frame(root)
header_frame.pack(pady=13)

# Create headers
headers = ["Name", "Cow Milk (L)", "Buffalo Milk (L)", "Total"]
for col, text in enumerate(headers):
    ttk.Label(header_frame, text=text, width=15, relief="ridge").grid(row=0, column=col, padx=2, pady=2)

# Input Frame
input_frame = ttk.Frame(root)
input_frame.pack()

entries_name = []
entries_cow = []
entries_buffalo = []
total_labels = []

# Create input rows
for i in range(13):
    row = i + 1
    
    # Name entry
    name_entry = ttk.Entry(input_frame, width=15)
    name_entry.grid(row=row, column=0, padx=2, pady=2)
    entries_name.append(name_entry)
    
    # Cow milk entry
    cow_entry = ttk.Entry(input_frame, width=10, justify="center")
    cow_entry.grid(row=row, column=1, padx=2, pady=2)
    cow_entry.bind("<Return>", on_enter)
    entries_cow.append(cow_entry)
    
    # Buffalo milk entry
    buffalo_entry = ttk.Entry(input_frame, width=10, justify="center")
    buffalo_entry.grid(row=row, column=2, padx=2, pady=2)
    buffalo_entry.bind("<Return>", on_enter)
    entries_buffalo.append(buffalo_entry)
    
    # Total label
    total_label = ttk.Label(input_frame, text="₹0.00", relief="sunken", width=15)
    total_label.grid(row=row, column=3, padx=2, pady=2)
    total_labels.append(total_label)

# Button Frame
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

ttk.Button(button_frame, text="Calculate", command=calculate_total).grid(row=0, column=0, padx=5)
ttk.Button(button_frame, text="Save to Excel", command=save_to_excel).grid(row=0, column=1, padx=5)

# Grand total display
total_all_label = ttk.Label(root, text="Grand Total: ₹0.00", 
                          font=("Arial", 12, "bold"))
total_all_label.pack(pady=10)

# Start with first entry focused
entries_name[0].focus_set()

root.mainloop()