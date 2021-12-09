from tkinter import *


def b1():
    l['text'] = 'hello world'


root = Tk()
root.geometry("500x500")
root.title("demo")
f = Frame(root, width=500, height=500, bg="red")
f.pack(fill=BOTH, expand=True)
l = Label(f, width=20, font=("arial", 25, "bold"), bg="yellow", fg="red", text="result will be show here!")
l.pack()
b = Button(f, width=15, text="click here", command=b1)
b.pack()
root.mainloop()
