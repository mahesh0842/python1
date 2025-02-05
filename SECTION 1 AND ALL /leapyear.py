import tkinter as tk

def on_enter(event):
    event.widget.tk_focusNext().focus()
    return "break"

def calculate_total():
    total_sum = 0
    for i in range(10):
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

# Create main window
root = tk.Tk()
root.title("Milk Cost Calculator")
root.geometry("600x450")

# Configure grid layout
root.columnconfigure(0, weight=1)
root.columnconfigure(3, weight=1)

# Create headers
headers = ["Person", "Cow Milk (L)", "Buffalo Milk (L)", "Total"]
for col, text in enumerate(headers):
    tk.Label(root, text=text, width=15, relief="ridge").grid(row=0, column=col, padx=2, pady=2, sticky="ew")

entries_cow = []
entries_buffalo = []
total_labels = []

# Create input rows
for i in range(10):
    row = i + 1
    
    # Person label
    tk.Label(root, text=f"Person {i+1}", relief="groove").grid(row=row, column=0, padx=2, pady=2, sticky="ew")
    
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

# Calculate button
tk.Button(root, text="Calculate", command=calculate_total, 
         bg="#4CAF50", fg="BLACK").grid(row=11, column=0, columnspan=4, pady=10, sticky="ew")

# Grand total display
total_all_label = tk.Label(root, text="Grand Total: ₹0.00", 
                          font=("Arial", 12, "bold"), bg="#333", fg="white")
total_all_label.grid(row=12, column=0, columnspan=4, pady=10, sticky="ew")

# Start with first entry focused
entries_cow[0].focus_set()

root.mainloop()