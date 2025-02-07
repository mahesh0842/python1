import tkinter as tk
from tkinter import filedialog, messagebox
from tkcalendar import DateEntry
import pandas as pd

def on_enter(event):
    event.widget.tk_focusNext().focus()
    return "break"

def calculate_total():
    total_sum = 0
    for i in range(12):
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
    
    # Update grand total
    total_all_label.config(text=f"Grand Total: ₹{total_sum:.2f}")
    
    # Move focus to the next entry box
    current_focus = root.focus_get()
    current_focus.tk_focusNext().focus()

def save_to_excel():
    data = []
    for i in range(12):
        name = entries_name[i].get()
        cow_milk = entries_cow[i].get()
        buffalo_milk = entries_buffalo[i].get()
        total = total_labels[i].cget("text").replace("₹", "")
        date = cal.get_date()
        data.append([name, cow_milk, buffalo_milk, total, date])
    
    df = pd.DataFrame(data, columns=["Name", "Cow Milk (L)", "Buffalo Milk (L)", "Total", "Date"])
    
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
    if file_path:
        df.to_excel(file_path, index=False)
        messagebox.showinfo("Success", "Data saved successfully!")

def reset_names():
    for entry in entries_name:
        entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Milk Cost Calculator")
root.geometry("800x600")

# Configure grid layout
for col in range(4):
    root.columnconfigure(col, weight=1)

# Create headers
headers = ["Name", "Cow Milk (L)", "Buffalo Milk (L)", "Total"]
for col, text in enumerate(headers):
    tk.Label(root, text=text, width=20, relief="ridge").grid(
        row=0, column=col, padx=2, pady=2, sticky="ew"
    )

entries_name = []
entries_cow = []
entries_buffalo = []
total_labels = []

# Create input rows
for i in range(12):
    row = i + 1
    
    # Name entry
    name_entry = tk.Entry(root, width=20)
    name_entry.grid(row=row, column=0, padx=2, pady=2)
    name_entry.bind("<Return>", on_enter)
    entries_name.append(name_entry)
    
    # Cow milk entry
    cow_entry = tk.Entry(root, width=15, justify="center")
    cow_entry.grid(row=row, column=1, padx=2, pady=2)
    cow_entry.bind("<Return>", on_enter)
    entries_cow.append(cow_entry)
    
    # Buffalo milk entry
    buffalo_entry = tk.Entry(root, width=15, justify="center")
    buffalo_entry.grid(row=row, column=2, padx=2, pady=2)
    buffalo_entry.bind("<Return>", on_enter)
    entries_buffalo.append(buffalo_entry)
    
    # Total label
    total_label = tk.Label(root, text="₹0.00", relief="sunken", width=15)
    total_label.grid(row=row, column=3, padx=2, pady=2, sticky="ew")
    total_labels.append(total_label)

# Date picker
tk.Label(root, text="Date:", width=15, relief="ridge").grid(row=13, column=0, padx=2, pady=2, sticky="ew")
cal = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
cal.grid(row=13, column=1, padx=2, pady=2, sticky="ew")

# Buttons
button_frame = tk.Frame(root)
button_frame.grid(row=14, column=0, columnspan=4, pady=10, sticky="ew")

tk.Button(button_frame, text="Calculate", command=calculate_total, bg="#4CAF50", width=15).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Save to Excel", command=save_to_excel, bg="#2196F3", width=15).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Reset Names", command=reset_names, bg="#ff0000", fg="Black", width=15).pack(side=tk.LEFT, padx=5)

# Grand total display
total_all_label = tk.Label(root, text="Grand Total: ₹0.00", font=("Arial", 12, "bold"), bg="#333", fg="white")
total_all_label.grid(row=15, column=0, columnspan=4, pady=10, sticky="ew")

# Start with first entry focused
entries_name[0].focus_set()

root.mainloop()