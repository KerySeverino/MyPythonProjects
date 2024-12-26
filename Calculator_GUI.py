from tkinter import *

#Initializes the window and sets the title
window = Tk()
window.title("Calculator")

#Sets the icon of the calculator program when is opened
icon_image = PhotoImage(file = "/Users/keryseverinodiaz/Desktop/MyProjects/100DaysOfPython/MyPythonProjects/icon.png") 
window.iconphoto(True, icon_image)

#Creates the entry window, where the user sees the input numbers
entry = Entry(window, width=10, font=("Arial", 60), bg="#8ed1c1", fg="#000000")
entry.grid(row=0, column=0, columnspan=4)

#All the definitons
#Gets the number the user clicks, while deleting the older number from view
def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(number))
    
#Clears the entry window
def clear():
    entry.delete(0, END)

#Adds the numbers
def add():
    global f_num
    global math
    first_number = entry.get()
    math = "addition"
    f_num = float(first_number)
    entry.delete(0, END)

#Substracts the numbers
def sub():
    global f_num
    global math
    first_number = entry.get()
    math = "substraction"
    f_num = float(first_number)
    entry.delete(0, END)

#Multiplies the numbers
def mul():
    global f_num
    global math
    first_number = entry.get()
    math = "multiplication"
    f_num = float(first_number)
    entry.delete(0, END)

#Divides the numbers
def div():
    global f_num
    global math
    first_number = entry.get()
    math = "division"
    f_num = float(first_number)
    entry.delete(0, END)

#Raises a number to the power
def raised():
    global f_num
    global math
    first_number = entry.get()
    math = "raisedTo"
    f_num = float(first_number)
    entry.delete(0, END)

#Calculates the squared root directly on the def
def sqrt():
    global f_num
    global math
    first_number = entry.get()
    f_num = float(first_number)

    if f_num >= 0:
        result = f_num ** 0.5 
        entry.delete(0, END)
        entry.insert(0, result)

    math = "sqrt"
    
#Inserts a dot/point 
def dot():
    current = entry.get()
    if '.' not in current:
        entry.delete(0, END)
        entry.insert(0, current + '.')

#Calculates the percentage
def percentage():
    global f_num
    global math
    first_number = entry.get()
    math = "percentage"
    f_num = float(first_number)
    entry.delete(0, END)

#Calculates the input numbers
def calculate():
    second_number = entry.get()
    entry.delete(0, END)
    if math == "addition":
        entry.insert(0, f_num + float(second_number))
    if math == "substraction":
        entry.insert(0,f_num - float(second_number))
    if math == "multiplication":
        entry.insert(0,f_num * float(second_number))
    if math == "division":
        entry.insert(0,f_num / float(second_number))
    if math == "percentage":
        entry.insert(0, f_num * (float(second_number) / 100))
    if math == "raisedTo":
        entry.insert(0, f_num ** float(second_number))
        
#Creates the number buttons from 0 to 9
button_0 = Button(window, text="0", padx=20, pady=20, command=lambda: button_click(0))
button_1 = Button(window, text="1", padx=20, pady=20, command=lambda: button_click(1))
button_2 = Button(window, text="2", padx=20, pady=20, command=lambda: button_click(2))
button_3 = Button(window, text="3", padx=20, pady=20, command=lambda: button_click(3))
button_4 = Button(window, text="4", padx=20, pady=20, command=lambda: button_click(4))
button_5 = Button(window, text="5", padx=20, pady=20, command=lambda: button_click(5))
button_6 = Button(window, text="6", padx=20, pady=20, command=lambda: button_click(6))
button_7 = Button(window, text="7", padx=20, pady=20, command=lambda: button_click(7))
button_8 = Button(window, text="8", padx=20, pady=20, command=lambda: button_click(8))
button_9 = Button(window, text="9", padx=20, pady=20, command=lambda: button_click(9))

#Creates the operator buttons
button_add = Button(window, text="+", padx=37, pady=20, command=add, fg = "#276fdb")
button_sub = Button(window, text="-", padx=37, pady=20, command=sub, fg = "#276fdb")
button_mul = Button(window, text="x", padx=37, pady=20, command=mul, fg = "#276fdb")
button_div = Button(window, text="/", padx=24, pady=20, command=div, fg = "#276fdb")
button_raised = Button(window, text="^", padx=20, pady=20, command=raised, fg = "#276fdb")

#Creates the special buttons
button_equal = Button(window, text="=", padx=37, pady=20, command=calculate, fg = "#276fdb")
button_clear = Button(window, text="CLEAR", padx=20, pady=20, command=clear, fg = "#e64e4e")
button_dot = Button(window, text=".", padx=20, pady=20, command=dot)
button_percentage = Button(window, text="%", padx=20, pady=20, command=percentage)
button_sqrt = Button(window, text="√", padx=20, pady=20, command=sqrt, fg = "#276fdb")

#Places the numbers on the grid
#First Row
# 0, (.), (%), (=)  
button_0.grid(row=7, column=0)
button_dot.grid(row=7, column=1)
button_percentage.grid(row=7, column=2)
button_equal.grid(row=7, column=3)

#Second Row
# 1 - 3, (clear)
button_1.grid(row=6, column=0)
button_2.grid(row=6, column=1)
button_3.grid(row=6, column=2)
button_clear.grid(row=6, column=3)

#Third Row
# 4 - 6, (+)
button_4.grid(row=5, column=0)
button_5.grid(row=5, column=1)
button_6.grid(row=5, column=2)
button_add.grid(row=5, column=3)

#Fourth Row
# 7 - 9, (-)
button_7.grid(row=4, column=0)
button_8.grid(row=4, column=1)
button_9.grid(row=4, column=2)
button_sub.grid(row=4, column=3)

#Fifth Row
# (*), (/), (^), (√)
button_mul.grid(row=3, column=3)
button_div.grid(row=3, column=2)
button_raised.grid(row=3, column=1)
button_sqrt.grid(row=3, column=0)

window.mainloop()