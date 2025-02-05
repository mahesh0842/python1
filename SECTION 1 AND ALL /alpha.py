import tkinter as tk
from tkinter import ttk



class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Advanced Calculator")
        self.geometry("400x600")
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        self.display = ttk.Entry(self, font=("Arial", 24), justify='right')
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        for i, button in enumerate(buttons):
            ttk.Button(self, text=button, command=lambda b=button: self.on_button_click(b)).grid(row=(i//4)+1, column=i%4, sticky="nsew")

        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
            self.grid_rowconfigure(i+1, weight=1)

    def on_button_click(self, button):
        if button == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            self.display.insert(tk.END, button)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()