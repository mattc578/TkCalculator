from tkinter import *


root = Tk()
root.title('Personal Calculator')
icon = PhotoImage(file='C:\calcpic.png')
root.iconphoto(True, icon)
e = Entry(root, width=40)
e.grid(row=0, column=0, columnspan=3, padx=5, pady=6)
count = 0

def inputted(x):
    global text_box
    current_num = e.get()
    e.delete(0, END)
    text_box = str(current_num) + str(x)
    e.delete(0, END)
    e.insert(0, text_box)

def clear():
    e.delete(0, END)

def operation(op):
    global current_operation
    current_operation = op
    firstnum = e.get()
    global num1
    num1 = int(firstnum)
    e.delete(0, END)

def eq():
    secondnum = e.get()
    if current_operation == '+':
        e.delete(0, END)
        e.insert(0, num1 + int(secondnum))
    if current_operation == '-':
        e.delete(0, END)
        e.insert(0, num1 - int(secondnum))
    if current_operation == 'x':
        e.delete(0, END)
        e.insert(0, num1 * int(secondnum))
    if current_operation == '/':
        e.delete(0, END)
        e.insert(0, num1 / int(secondnum))
    if current_operation == '^':
        e.delete(0, END)
        e.insert(0, num1 ** int(secondnum))


button_0 = Button(root, text='0', padx=35, pady=15, font=('Arial', 10, 'bold'), command=lambda: inputted(0))
button_0.grid(row=4, column=0)
button_9 = Button(root, text='9', padx=35, pady=15, font=('Arial', 10, 'bold'), command=lambda: inputted(9))
button_9.grid(row=1, column=0)
button_8 = Button(root, text='8', padx=35, pady=15, font=('Arial', 10, 'bold'), command=lambda: inputted(8))
button_8.grid(row=1, column=1)
button_7 = Button(root, text='7', padx=35, pady=15, font=('Arial', 10, 'bold'), command=lambda: inputted(7))
button_7.grid(row=1, column=2)
button_6 = Button(root, text='6', padx=35, pady=15, font=('Arial', 10, 'bold'), command=lambda: inputted(6))
button_6.grid(row=2, column=0)
button_5 = Button(root, text='5', padx=35, pady=15, font=('Arial', 10, 'bold'), command=lambda: inputted(5))
button_5.grid(row=2, column=1)
button_4 = Button(root, text='4', padx=35, pady=15, font=('Arial', 10, 'bold'), command=lambda: inputted(4))
button_4.grid(row=2, column=2)
button_3 = Button(root, text='3', padx=35, pady=15, font=('Arial', 10, 'bold'), command=lambda: inputted(3))
button_3.grid(row=3, column=0)
button_2 = Button(root, text='2', padx=35, pady=15, font=('Arial', 10, 'bold'), command=lambda: inputted(2))
button_2.grid(row=3, column=1)
button_1 = Button(root, text='1', padx=35, pady=15, font=('Arial', 10, 'bold'), command=lambda: inputted(1))
button_1.grid(row=3, column=2)

button_ac = Button(root, text='AC', padx=33, pady=17, font=('Arial', 8, 'bold'), command=clear)
button_ac.grid(row=4, column=2)
button_add = Button(root, text='+', padx=35, pady=15, font=('Arial', 10, 'bold'), command=lambda: operation('+'))
button_add.grid(row=4, column=1)
button_sub = Button(root, text='-', padx=35, pady=15, font=('Arial', 11, 'bold'), command=lambda: operation('-'))
button_sub.grid(row=5, column=1)
button_mul = Button(root, text='x', padx=35, pady=15, font=('Arial', 9, 'bold'), command=lambda: operation('x'))
button_mul.grid(row=5, column=0)
button_div = Button(root, text='/', padx=35, pady=15, font=('Arial', 10, 'bold'), command=lambda: operation('/'))
button_div.grid(row=6, column=0)
button_exp = Button(root, text='^', padx=35, pady=15, font=('Arial', 10, 'bold'), command=lambda: operation('^'))
button_exp.grid(row=6, column=1)

button_eq = Button(root, text='=', padx=35, pady=50, font=('Arial', 10, 'bold'), command=eq)
button_eq.grid(row=5, column=2, rowspan=2)

root.mainloop()










