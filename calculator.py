from tkinter import *
from PIL import ImageTk, Image
root = Tk()

# changing background color of GUI interface
root.configure(background="black")

# defining title of project
root.title("Simple Calculator")

# icon images
root.iconbitmap('C:/Users/RUPA/Desktop/simplecalc.ico')

# display entry
e = Entry(root, width = 40, borderwidth = 8, font=('arial',10, 'bold'))
e.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

# defining the buttons
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    num1 = e.get()
    global num_one
    global math
    math = "addition"
    num_one = int(num1)
    e.delete(0, END)

def button_subtract():
    num1 = e.get()
    global num_one
    global math
    math = "subtraction"
    num_one = int(num1)
    e.delete(0, END)

def button_multiply():
    num1 = e.get()
    global num_one
    global math
    math = "multiplication"
    num_one = int(num1)
    e.delete(0, END)

def button_divide():
    num1 = e.get()
    global num_one
    global math
    math = "division"
    num_one = int(num1)
    e.delete(0, END)

def button_mod():
    num1 = e.get()
    global num_one
    global math
    math = "modulo"
    num_one = int(num1)
    e.delete(0, END)

def button_exponent():
    num1 = e.get()
    global num_one
    global math
    math = "exponential"
    num_one = int(num1)
    e.delete(0, END)

def button_equal():
    num2 = e.get()
    e.delete(0, END)

    if math == "addition":
     e.insert(0, num_one + int(num2))

    if math == "subtraction":
     e.insert(0, num_one - int(num2))

    if math == "multiplication":
     e.insert(0, num_one * int(num2))

    if math == "division":
     e.insert(0, num_one / int(num2))

    if math == "modulo":
     e.insert(0, num_one % int(num2))

    if math == "exponential":
     e.insert(0, num_one ** int(num2))



# defining the buttons
one=Button(root, text="1",fg= "white", bg= "grey",font=('arial',10, 'bold'), padx=41, pady=20, command=lambda : button_click(1))
two=Button(root, text="2",fg= "white", bg= "grey", font=('arial',10, 'bold'),padx=41, pady=20, command=lambda : button_click(2))
three=Button(root, text="3",fg= "white", bg= "grey",font=('arial',10, 'bold'), padx=41, pady=20, command=lambda : button_click(3))
four=Button(root, text="4",fg= "white", bg= "grey",font=('arial',10, 'bold'), padx=41, pady=20, command=lambda : button_click(4))
five=Button(root, text="5",fg= "white", bg= "grey",font=('arial',10, 'bold'),padx=41, pady=20, command=lambda : button_click(5))
six=Button(root, text="6",fg= "white", bg= "grey",font=('arial',10, 'bold'), padx=41, pady=20, command=lambda : button_click(6))
seven=Button(root, text="7",fg= "white", bg= "grey",font=('arial',10, 'bold'), padx=43, pady=20, command=lambda : button_click(7))
eight=Button(root, text="8",fg= "white", bg= "grey", font=('arial',10, 'bold'),padx=41, pady=20, command=lambda : button_click(8))
nine=Button(root, text="9",fg= "white", bg= "grey",font=('arial',10, 'bold'), padx=41, pady=20, command=lambda : button_click(9))
zero=Button(root, text="0",fg= "white", bg= "grey",font=('arial',10, 'bold'), padx=92, pady=20, command=lambda : button_click(0))

add=Button(root, text="+", fg="white", bg="orange",font=('arial',15, 'bold'), padx=41, pady=20, command=button_add)
subtract=Button(root, text="-",fg="white", bg="orange", font=('arial',15, 'bold'),padx=44, pady=20, command=button_subtract)
multiply=Button(root, text="*",  fg="white", bg="orange",font=('arial',15, 'bold'),padx=44, pady=20, command=button_multiply)
divide=Button(root, text="/", fg="white", bg="orange",font=('arial',15, 'bold'), padx=45, pady=20, command=button_divide)
mod=Button(root, text="%", font=('arial',15, 'bold'),padx=39, pady=20, command=button_mod)
exponent=Button(root, text="^", font=('arial',15, 'bold'),padx=39, pady=20, command=button_exponent)

equal=Button(root, text="=", fg="white", bg="orange",font=('arial',15, 'bold'), padx=97, pady=20, command=button_equal)
clear=Button(root, text="Clear", font=('arial',15, 'bold'),padx=30, pady=20, command=button_clear)


# putting buttons on the screen
clear.grid(row=1, column=0)
exponent.grid(row=1, column=1)
mod.grid(row=1, column=2)
divide.grid(row=1, column=3)

one.grid(row=4, column=0)
two.grid(row=4, column=1)
three.grid(row=4, column=2)
add.grid(row=4, column=3)

four.grid(row=3, column=0)
five.grid(row=3, column=1)
six.grid(row=3, column=2)
subtract.grid(row=3, column=3)

seven.grid(row=2, column=0)
eight.grid(row=2, column=1)
nine.grid(row=2, column=2)
multiply.grid(row=2, column=3)

zero.grid(row=5, column=0, columnspan = 2)
equal.grid(row=5, column=2, columnspan = 2)

mainloop()