from tkinter import Tk, N, E, S, W, StringVar, Button, Label, Frame
from functools import partial

current_expression = ""

def onPress(symbol):
    global current_expression
    current_expression += str(symbol)
    equation_var.set(current_expression)

def backspace():
    global current_expression
    current_expression = current_expression[:-1]
    equation_var.set(current_expression)

def clear():
    global current_expression
    current_expression = ""
    equation_var.set("")

def evaluateEquation():
    global current_expression
    try:
        answer = str(eval(current_expression))
        equation_var.set(answer)
        current_expression = ""
    except:
        equation_var.set("Invalid expression, please try again")

#Sets up the tkinter window
root = Tk()
root.title('Calculator')

# Sets up the grid for use in positioning
mainframe = Frame(root, borderwidth=5)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Sets up the variables and widgets for use in the program
equation_var = StringVar()

# 

# Number buttons
for y in range(2, 5):
    for x in range(0, 3):
        num = (x + 1) + (3 * (y - 2))
        globals()[f"button_{num}"] = Button(mainframe, text=str(num), command=partial(
            onPress, num
        ), width=5, background="white")
        globals()[f"button_{num}"].grid(row=y, column=x)

# Other symbols/actions
button_0 = Button(mainframe, text="0", command=partial(
    onPress, 0
), width=5, background="white")
plus_button = Button(mainframe, text="+", command=partial(
    onPress, "+"
), width=5, background="light grey")
minus_button = Button(mainframe, text="-", command=partial(
    onPress, "-"
), width=5, background="light grey")
times_button = Button(mainframe, text="*", command=partial(
    onPress, "*"
), width=5, background="light grey")
division_button = Button(mainframe, text="/", command=partial(
    onPress, "/"
), width=5, background="light grey")
decimal_button = Button(mainframe, text=".", command=partial(
    onPress, "."
), width=5, background="light grey")
exponent_button = Button(mainframe, text="**", command=partial(
    onPress, "**"
), width=5, background="light grey")
floor_button = Button(mainframe, text="//", command=partial(
    onPress, "//"
), width=5, background="light grey")
open_paren_button = Button(mainframe, text="(", command=partial(
    onPress, "("
), width=5, background="light grey")
closed_paren_button = Button(mainframe, text=")", command=partial(
    onPress, ")"
), width=5, background="light grey")
equals_button = Button(mainframe, text="=", command=evaluateEquation, width=5, background="light green")
back_button = Button(mainframe, text="<-", command=backspace, width=5, background="light blue")
clear_button = Button(mainframe, text="CLR", command=clear, width=5, background="pink")

clear_button.grid(row=1, column=0)
open_paren_button.grid(row=1, column=1)
closed_paren_button.grid(row=1, column=2)
division_button.grid(row=1, column=3)
times_button.grid(row=2, column=3)
minus_button.grid(row=3, column=3)
plus_button.grid(row=4, column=3)
back_button.grid(row=5, column=0)
button_0.grid(row=5, column=1)
decimal_button.grid(row=5, column=2)
equals_button.grid(row=5, column=3)

# Creates the label at the top that contains the equation
equation_label = Label(mainframe, textvariable=equation_var, background="white")
equation_label.grid(row=0, column=0, columnspan=4, sticky=(E, W))

# Starts the window loop
root.mainloop()