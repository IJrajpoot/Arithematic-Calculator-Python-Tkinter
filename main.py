import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Arithmetic Calculator")


def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + value)


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


def clear():
    entry.delete(0, tk.END)


def backspace():
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text[:-1])


# Set the size of the window
root.geometry("400x500")

# Create the display
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='solid', justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=20)

# Define button style
button_style = {
    "font": ('Arial', 18),
    "width": 5,
    "height": 2,
    "relief": "raised",
    "bd": 2,
}

# Add clear and backspace buttons
tk.Button(root, text='C', font=('Arial', 18), width=5, height=2, relief="raised", bd=2, bg="#f44336", fg="white",
          command=clear).grid(row=1, column=0, padx=5, pady=5)
tk.Button(root, text='<-', font=('Arial', 18), width=5, height=2, relief="raised", bd=2, bg="#ff9800", fg="white",
          command=backspace).grid(row=1, column=1, padx=5, pady=5)

# Create buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
]
row = 2
col = 0
for button in buttons:
    if button == "=":
        tk.Button(root, text=button, font=('Arial', 18), width=5, height=2, relief="raised", bd=2, bg="#4CAF50",
                  fg="white", command=calculate).grid(row=row, column=2, padx=5, pady=5)
        tk.Button(root, text=button, font=('Arial', 18), width=5, height=2, relief="raised", bd=2, bg="#4CAF50",
                  fg="white", command=calculate).grid(row=row, column=3, padx=5, pady=5)
    else:
        tk.Button(root, text=button, **button_style, command=lambda b=button: button_click(b)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the application
root.mainloop()
