import tkinter as tk
import math

# Create a function to handle button clicks
def button_click(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Create a function to handle the "clear" button click
def clear():
    global expression
    expression = ""
    equation.set("0")

# Create a function to handle the "equal" button click
def calculate():
    global expression
    result = str(eval(expression))
    equation.set(result)
    expression = ""

# Create a function to handle the "square root" button click
def sqrt():
    global expression
    result = str(math.sqrt(float(expression)))
    equation.set(result)
    expression = ""

# Create a function to handle the "log" button click
def log():
    global expression
    result = str(math.log10(float(expression)))
    equation.set(result)
    expression = ""

# Create a function to handle the "sin" button click
def sin():
    global expression
    result = str(math.sin(float(expression)))
    equation.set(result)
    expression = ""

# Create a function to handle the "cos" button click
def cos():
    global expression
    result = str(math.cos(float(expression)))
    equation.set(result)
    expression = ""

# Create a function to handle the "tan" button click
def tan():
    global expression
    result = str(math.tan(float(expression)))
    equation.set(result)
    expression = ""

# Initialize the GUI
root = tk.Tk()
root.title("Scientific Calculator")

# Create a variable for the equation to be displayed
equation = tk.StringVar()
expression = ""

# Create the entry widget to display the equation
entry = tk.Entry(root, textvariable=equation, font=('Arial', 20), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
equation.set("0")

# Create the buttons
button_sqrt = tk.Button(root, text='sqrt', font=('Arial', 15), command=sqrt)
button_sqrt.grid(row=1, column=0, padx=10, pady=10)

button_log = tk.Button(root, text='log', font=('Arial', 15), command=log)
button_log.grid(row=1, column=1, padx=10, pady=10)

button_sin = tk.Button(root, text='sin', font=('Arial', 15), command=sin)
button_sin.grid(row=1, column=2, padx=10, pady=10)

button_cos = tk.Button(root, text='cos', font=('Arial', 15), command=cos)
button_cos.grid(row=1, column=3, padx=10, pady=10)

button_tan = tk.Button(root, text='tan', font=('Arial', 15), command=tan)
button_tan.grid(row=2, column=0, padx=10, pady=10)

button_7 = tk.Button(root, text='7', font=('Arial', 15), command=lambda: button_click(7))
button_7.grid(row=2, column=1, padx=10, pady=10)

button_8 = tk.Button(root, text='8', font=('Arial', 15), command=lambda: button_click(8))
button_8.grid(row=2, column=2, padx=10, pady=10)

button_9 = tk.Button(root, text='9', font=('Arial', 15), command=lambda: button_click(9))
button_9.grid(row=2, column=3, padx=10, pady=10)

button_4 = tk.Button(root, text='4', font=('Arial', 15), command=lambda: button_click(4))
button_4.grid(row=3, column=0, padx=10, pady=10)

button_5 = tk.Button(root, text='5', font=('Arial', 15), command=lambda: button_click(5))
button_5.grid(row=3, column=1, padx=10, pady=10)

button_6 = tk.Button(root, text='6', font=('Arial', 15), command=lambda: button_click(6))
button_6.grid(row=3, column=2, padx=10, pady=10)

button_multiply = tk.Button(root, text='', font=('Arial', 15), command=lambda: button_click(''))
button_multiply.grid(row=3, column=3, padx=10, pady=10)

button_1 = tk.Button(root, text='1', font=('Arial', 15), command=lambda: button_click(1))
button_1.grid(row=4, column=0, padx=10, pady=10)

button_2 = tk.Button(root, text='2', font=('Arial', 15), command=lambda: button_click(2))
button_2.grid(row=4, column=1, padx=10, pady=10)

button_3 = tk.Button(root, text='3', font=('Arial', 15), command=lambda: button_click(3))
button_3.grid(row=4, column=2, padx=10, pady=10)

button_subtract = tk.Button(root, text='-', font=('Arial', 15), command=lambda: button_click('-'))
button_subtract.grid(row=4, column=3, padx=10, pady=10)

button_0 = tk.Button(root, text='0', font=('Arial', 15), command=lambda: button_click(0))
button_0.grid(row=5, column=0, padx=10, pady=10)

button_decimal = tk.Button(root, text='.', font=('Arial', 15), command=lambda: button_click('.'))
button_decimal.grid(row=5, column=1, padx=10, pady=10)

button_clear = tk.Button(root, text='C', font=('Arial', 15), command=clear)
button_clear.grid(row=5, column=2, padx=10, pady=10)

button_add = tk.Button(root, text='+', font=('Arial', 15), command=lambda: button_click('+'))
button_add.grid(row=5, column=3, padx=10, pady=10)

button_equal = tk.Button(root, text='=', font=('Arial', 15), command=calculate)
button_equal.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

root.mainloop()