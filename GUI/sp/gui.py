from tkinter import *


def check():
    name = e1.get()
    print(name)


# root window;
root = Tk()
root.geometry("500x500")
root.title("my window!")

frame_one = Frame(root, width=500, height=500, bg="red")

e1 = Entry(frame_one, width=10)
e1.pack()
b1 = Button(frame_one, width=15, text="NAME", command=check).pack()
frame_one.pack(fill=BOTH, expand=True)


root.mainloop()
