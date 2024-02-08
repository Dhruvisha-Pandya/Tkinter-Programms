from tkinter import *
root = Tk()
e = Entry(root, width=50)
e.pack()
e.insert(0,"Enter your name")

def name():
    hi = "hello" + e.get()
    l1 = Label(root, text= hi).pack()

b = Button(root, text="Submit", command=name). pack()
root.mainloop()
