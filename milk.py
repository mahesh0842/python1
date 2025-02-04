import tkinter as tk

def calculate():
    totals = []
    for i in range(13):
        try:
            cow = float(cow_entries[i].get())
        except ValueError:
            cow = 0.0
        try:
            buffalo = float(buffalo_entries[i].get())
        except ValueError:
            buffalo = 0.0
        
        total = cow * 40 + buffalo * 62
        totals.append(total)
        result_labels[i].config(text=f"₹{total:.2f}")
    
    overall_total = sum(totals)
    total_label.config(text=f"Total for all 13 people: ₹{overall_total:.2f}")

# Create main window
window = tk.Tk()
window.title("Milk Cost Calculator")

# Input Frame
input_frame = tk.Frame(window, padx=13, pady=13)
input_frame.pack()

# Create headers
tk.Label(input_frame, text="Person").grid(row=0, column=0)
tk.Label(input_frame, text="Cow Milk (L)").grid(row=0, column=1)
tk.Label(input_frame, text="Buffalo Milk (L)").grid(row=0, column=2)

cow_entries = []
buffalo_entries = []

# Create input fields
for i in range(13):
    row = i + 1
    tk.Label(input_frame, text=f"Person {i+1}").grid(row=row, column=0)
    
    cow_entry = tk.Entry(input_frame, width=7)
    cow_entry.grid(row=row, column=1, padx=5)
    cow_entries.append(cow_entry)
    
    buffalo_entry = tk.Entry(input_frame, width=7)
    buffalo_entry.grid(row=row, column=2, padx=5)
    buffalo_entries.append(buffalo_entry)

# Calculate Button
tk.Button(window, text="Calculate", command=calculate, padx=20).pack(pady=5)

# Results Frame
results_frame = tk.Frame(window, padx=13, pady=13)
results_frame.pack()

# Results headers
tk.Label(results_frame, text="Person").grid(row=0, column=0)
tk.Label(results_frame, text="Total Cost").grid(row=0, column=1)

result_labels = []
for i in range(13):
    row = i + 1
    tk.Label(results_frame, text=f"Person {i+1}").grid(row=row, column=0)
    total_label = tk.Label(results_frame, text="")
    total_label.grid(row=row, column=1)
    result_labels.append(total_label)

# Total Label
total_label = tk.Label(window, text="Total: ₹0.00", font=("Arial", 12, "bold"))
total_label.pack(pady=13)

window.mainloop()