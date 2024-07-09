from tkinter import *

count = 0
num1 = 0
operation = 0
current_number = 0
reset_number = 0
# command functions

# functions for number buttons
def insert_number_0():
    global reset_number
    if reset_number == 1:
        textbox.delete(0, END)

    textbox.insert(len(textbox.get()), ("0"))
    reset_number = 0

def insert_number_1():
    global reset_number
    if reset_number == 1:
        textbox.delete(0, END)

    textbox.insert(len(textbox.get()), ("1"))
    reset_number = 0

def insert_number_2():
    global reset_number
    if reset_number == 1:
        textbox.delete(0, END)

    textbox.insert(len(textbox.get()), ("2"))
    reset_number = 0

def insert_number_3():
    global reset_number
    if reset_number == 1:
        textbox.delete(0, END)

    textbox.insert(len(textbox.get()), ("3"))
    reset_number = 0

def insert_number_4():
    global reset_number
    if reset_number == 1:
        textbox.delete(0, END)

    textbox.insert(len(textbox.get()), ("4"))
    reset_number = 0

def insert_number_5():
    global reset_number
    if reset_number == 1:
        textbox.delete(0, END)

    textbox.insert(len(textbox.get()), ("5"))
    reset_number = 0

def insert_number_6():
    global reset_number
    if reset_number == 1:
        textbox.delete(0, END)

    textbox.insert(len(textbox.get()), ("6"))
    reset_number = 0

def insert_number_7():
    global reset_number
    if reset_number == 1:
        textbox.delete(0, END)

    textbox.insert(len(textbox.get()), ("7"))
    reset_number = 0

def insert_number_8():
    global reset_number
    if reset_number == 1:
        textbox.delete(0, END)

    textbox.insert(len(textbox.get()), ("8"))
    reset_number = 0

def insert_number_9():
    global reset_number
    if reset_number == 1:
        textbox.delete(0, END)

    textbox.insert(len(textbox.get()), ("9"))
    reset_number = 0

# special functions
def reset():
    global count,num1,num2,reset_number
    count = 0
    num1 = 0
    num2 = 0
    reset_number =0
    textbox.delete(0, END)

def insert_decimal():
    textbox.insert(len(textbox.get()), ("."))
    button_decimal.config(state=DISABLED)

def plus_minus():
    number = textbox.get()

    if number[0] == "-":
        textbox.delete(0,1)

    else:
        print(number[0])
        textbox.insert(0,"-")
def backspace():
    textbox.delete(len(textbox.get())-1, END)

# operation functions

def do_operation(num1,operation,num2):

    if operation == "add":
        newnumber = num1 + num2
        return newnumber

    elif operation == "subtract":
        newnumber = num1 - num2
        return newnumber

    elif operation == "multiply":
        newnumber = num1 * num2
        return newnumber

    elif operation == "divide":
        newnumber = num1 / num2
        return newnumber


def add():
    global count, num1, operation, reset_number
    count = count + 1

    if count == 1:
        num1 = float(textbox.get())
        operation = "add"
        reset_number = 1

    else:
        num2 = float(textbox.get())
        new_number = str(do_operation(num1, operation, num2))
        num1 = float(new_number)
        textbox.delete(0,END)
        textbox.insert(len(textbox.get()), (new_number))
        operation = "add"
        reset_number = 1

def subtract():
    global count, num1, operation, reset_number
    count = count + 1

    if count == 1:
        num1 = float(textbox.get())
        operation = "subtract"
        reset_number = 1

    else:
        num2 = float(textbox.get())
        new_number = str(do_operation(num1, operation, num2))
        num1 = float(new_number)
        textbox.delete(0,END)
        textbox.insert(len(textbox.get()), (new_number))
        operation = "subtract"
        reset_number = 1


def multiply():
    global count, num1, operation, reset_number
    count = count + 1

    if count == 1:
        num1 = float(textbox.get())
        operation = "multiply"
        reset_number = 1

    else:
        num2 = float(textbox.get())
        new_number = str(do_operation(num1, operation, num2))
        num1 = float(new_number)
        textbox.delete(0,END)
        textbox.insert(len(textbox.get()), (new_number))
        operation = "multiply"
        reset_number = 1

def divide():
    global count, num1, operation, reset_number
    count = count + 1

    if count == 1:
        num1 = float(textbox.get())
        operation = "divide"
        reset_number = 1
    else:
        num2 = float(textbox.get())
        new_number = str(do_operation(num1, operation, num2))
        num1 = float(new_number)
        textbox.delete(0,END)
        textbox.insert(len(textbox.get()), (new_number))
        operation = "divide"
        reset_number = 1

def equal():
    global num1, num2, count, reset_number
    num2 = float(textbox.get())
    textbox.delete(0, END)
    new_number = str(do_operation(num1, operation, num2))
    textbox.insert(len(textbox.get()), (new_number))
    count = 0
    reset_number = 1


#window
width, height = 360, 590
string_for_geometry = f"{width}x{height}"

window = Tk()
window.geometry(string_for_geometry)
window.resizable(False, False)

#textbox
textbox = Entry(window, font=("Arial",50))
textbox.place(x=0, y=0, width=360, height=150)

#buttons
button_c = Button(window, text="C", command=reset)
button_c.place(x=0, y=150, width=90, height=90)

button_backspace = Button(window, text="<<", command=backspace)
button_backspace.place(x=90, y=150, width=180, height=90)

button_1 = Button(window, text="1", command=insert_number_1)
button_1.place(x=0, y=240, width=90, height=90)

button_2 = Button(window, text="2", command=insert_number_2)
button_2.place(x=90, y=240, width=90, height=90)

button_3 = Button(window, text="3", command=insert_number_3)
button_3.place(x=180, y=240, width=90, height=90)

button_4 = Button(window, text="4", command=insert_number_4)
button_4.place(x=0, y=330, width=90, height=90)

button_5 = Button(window, text="5", command=insert_number_5)
button_5.place(x=90, y=330, width=90, height=90)

button_6 = Button(window, text="6", command=insert_number_6)
button_6.place(x=180, y=330, width=90, height=90)

button_7 = Button(window, text="7", command=insert_number_7)
button_7.place(x=0, y=420, width=90, height=90)

button_8 = Button(window, text="8", command=insert_number_8)
button_8.place(x=90, y=420, width=90, height=90)

button_9 = Button(window, text="9", command=insert_number_9)
button_9.place(x=180, y=420, width=90, height=90)

button_plusminus = Button(window, text="+/-", command=plus_minus)
button_plusminus.place(x=0, y=500, width=90, height=90)

button_0 = Button(window, text="0", command=insert_number_0)
button_0.place(x=90, y=500, width=90, height=90)

button_decimal = Button(window, text=".", command=insert_decimal)
button_decimal.place(x=180, y=500, width=90, height=90)

button_add = Button(window, text="+", command=add)
button_add.place(x=270, y=150, width=90, height=90)

button_sub = Button(window, text="-", command=subtract)
button_sub.place(x=270, y=240, width=90, height=90)

button_multiply = Button(window, text="x", command=multiply)
button_multiply.place(x=270, y=330, width=90, height=90)

button_divide = Button(window, text="/", command=divide)
button_divide.place(x=270, y=420, width=90, height=90)

button_equal = Button(window, text="=", command=equal)
button_equal.place(x=270, y=500, width=90, height=90)



window.mainloop()