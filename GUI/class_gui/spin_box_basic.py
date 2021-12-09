from tkinter import *

root = Tk()
root.title("my window")
root.geometry("500x500")


frame = Frame(root, height=500, width=500, bg="red").pack(fill=BOTH, expand=True)
variable = StringVar()

spain_box = Spinbox(frame, values=("aurangabad", "pune", "beed"), textvariable=variable).pack(side="top")

root.mainloop()