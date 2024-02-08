from tkinter import *
calc = Tk()
calc.title("CALCULATOR")

e = Entry(calc, width=45, borderwidth=5).grid(row=0, column= 0 , columnspan=4, padx=10, pady=10)

def b_click(number):
    e.delete(0, END)
    e.insert(0, number)

b1 = Button(calc, text="1", padx=25, pady=25, command=lambda:b_click(1))
b2 = Button(calc, text="2", padx=25, pady=25, command=lambda:b_click(2))
b3 = Button(calc, text="3", padx=25, pady=25, command=lambda:b_click(3))
b4 = Button(calc, text="4", padx=25, pady=25, command=lambda:b_click(4))
b5 = Button(calc, text="5", padx=25, pady=25, command=lambda:b_click(5))
b6 = Button(calc, text="6", padx=25, pady=25, command=lambda:b_click(6))
b7 = Button(calc, text="7", padx=25, pady=25, command=lambda:b_click(7))
b8 = Button(calc, text="8", padx=25, pady=25, command=lambda:b_click(8))
b9 = Button(calc, text="9", padx=25, pady=25, command=lambda:b_click(9))
b0 = Button(calc, text="0", padx=25, pady=25, command=lambda:b_click(0))
# b_equal = Button(calc, text="=", padx=25, pady=25, command=lambda:b_click())
# b_clear = Button(calc, text="CLEAR", padx=85, pady=25, command=lambda:b_click())
# b_pn = Button(calc, text="+/-", padx=20, pady=25, command=lambda:b_click())
# b_dot = Button(calc, text=".", padx= 25, pady=25, command=lambda:b_click())
# b_ad = Button(calc, text="+", padx=25, pady=25, command=lambda:b_click())
# b_sub = Button(calc, text="-", padx=25, pady=25, command=lambda:b_click())
# b_mul = Button(calc, text="x", padx=25, pady=25, command=lambda:b_click())
# b_div = Button(calc, text="/", padx=25, pady=25, command=lambda:b_click())

# b_clear.grid(row=5, columnspan=3)
# b_equal.grid(row=5, column=3)

# b_pn.grid(row=4, column=0)
b0.grid(row=4, column=1)
# b_dot.grid(row=4, column=2)
# b_ad.grid(row=4, column=3) 

b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2) 
# b_sub.grid(row=3, column=3)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
# b_mul.grid(row=2, column=3)

b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)
# b_div.grid(row=1, column=3)

calc.mainloop()