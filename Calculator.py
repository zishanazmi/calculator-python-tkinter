# Simple calculator using python 

import tkinter as tk


# Function to handel button clicks
def on_button_click(value):
    current_value = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_value+value)

# Function to clear the entry field
def on_clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def on_equals():
    try:
        current_value = entry.get()
        result = eval(current_value)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Creating the main window
window = tk.Tk()
window.title("Calculator usinng python")
window.configure(bg='#3c3c3c')
window.geometry("400x550")

# Entry widget to show the input/output
entry = tk.Entry(window, width=17, font=('Arial', 28), borderwidth=5, relief="solid", justify='right', bg='#f2f2f2')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=15, ipady=15)

# Button colors
button_bg_color = '#4d4d4d'
button_fg_color = '#ffffff'
operator_bg_color = '#ff9500'
operator_fg_color = '#ffffff'

# Button labels
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 3)
]

# Loop to create buttons and place them in the window
for (text, row, col) in buttons:
    if text in ['+', '-', '*', '/']:
        bg_color = operator_bg_color
        fg_color = operator_fg_color
    else:
        bg_color=button_bg_color
        fg_color = button_fg_color
    action = lambda x=text: on_button_click(x)
    button = tk.Button(window, text=text, width=5, height=2, font=('Arial', 18), bg=bg_color, fg=fg_color, command=action)
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Creating the'=' button
equals_button = tk.Button(window, text="=", width=5, height=2, font=('Arial', 18), bg="#32cd32", fg="white", command=on_equals)
equals_button.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")

# Creating the 'C' button
clear_button = tk.Button(window, text="C", width=5, height=2, font=("Arial", 18), bg="#FF6347", fg="white", command=on_clear)
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

# Making buttons responsive to window resizing
for i in range(4):
    window.grid_columnconfigure(i, weight=1)
for i in range(1, 6):
    window.grid_rowconfigure(i, weight=1)

# Start the GUI event loop
window.mainloop()




































































