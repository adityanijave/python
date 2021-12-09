from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("trying ")
f = Frame(root, width=500, height=500, bg="red").pack(fill=BOTH,expand=True)
l1 = Label(f, text="hello", bg="black", fg="orange", font="arial 18 bold", width=20).pack(side="top")
root.mainloop()