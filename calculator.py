import tkinter as tk

root = tk.Tk()
root.title('Simple Calculator')

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def f_button_execute(number):
#    entry.delete(0, end)
    current = entry.get()
    entry.delete(0, 'end')
    entry.insert(0, str(current) + str(number))

def f_button_clear():
    entry.delete(0, 'end')

def f_button_add():
    first_number = entry.get()
    global f_num
    f_num = int(first_number)
    entry.delete(0, 'end')

def f_button_subtract():
    return

def f_button_multiply():
    return

def f_button_divide():
    return

def f_button_equal():
    second_number = entry.get()
    entry.delete(0, 'end')
    entry.insert(0, f_num + int(second_number))

#Define buttons

button_1 = tk.Button(root, text='1', padx=33, pady=20, command=lambda: f_button_execute(1))
button_2 = tk.Button(root, text='2', padx=33, pady=20, command=lambda: f_button_execute(2))
button_3 = tk.Button(root, text='3', padx=33, pady=20, command=lambda: f_button_execute(3))
button_4 = tk.Button(root, text='4', padx=33, pady=20, command=lambda: f_button_execute(4))
button_5 = tk.Button(root, text='5', padx=33, pady=20, command=lambda: f_button_execute(5))
button_6 = tk.Button(root, text='6', padx=33, pady=20, command=lambda: f_button_execute(6))
button_7 = tk.Button(root, text='7', padx=33, pady=20, command=lambda: f_button_execute(7))
button_8 = tk.Button(root, text='8', padx=33, pady=20, command=lambda: f_button_execute(8))
button_9 = tk.Button(root, text='9', padx=33, pady=20, command=lambda: f_button_execute(9))
button_0 = tk.Button(root, text='0', padx=73, pady=20, command=lambda: f_button_execute(0))

button_add = tk.Button(root, text='+', padx=30, pady=52, command=f_button_add)
button_subtract = tk.Button(root, text='-', padx=33, pady=20, command=f_button_subtract)
button_multiply = tk.Button(root, text='*', padx=33, pady=20, command=f_button_multiply)
button_divide = tk.Button(root, text='/', padx=33, pady=20, command=f_button_divide)

button_equal = tk.Button(root, text='=', padx=30, pady=52, command=f_button_equal)
button_clear = tk.Button(root, text='Clear', padx=22, pady=20, command=f_button_clear)

#Place buttons on screen

button_divide.grid(row=1, column=0)
button_multiply.grid(row=1, column=1)
button_subtract.grid(row=1, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_add.grid(row=2, column=3, rowspan=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_equal.grid(row=4, column=3, rowspan=2)

button_0.grid(row=5, column=0, columnspan=2)
button_clear.grid(row=5, column=2)





root.mainloop()