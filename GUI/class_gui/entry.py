from tkinter import *


def check():
    un = e1.get()
    p = e2.get()
    if un == "abc" and p == "xyz":
        l1['text'] = "valid entry!"
    else:
        l1["text"] = "not valid entry!"


def clear():
    e1.delete(0, END)
    e2.delete(0, END)


# creating root window;
root = Tk()
# tittle
root.title(" demo window ")
# geometry;
root.geometry("500x500")
# creating frame window;
f1 = Frame(root, width=500, height=500, bg="red")
# packing the 1st frame;
f1.pack(fill=BOTH, expand=True)
# entry username and password;
e1 = Entry(f1, width=15)
e1.pack()
e2 = Entry(f1, width=15, show="*")
e2.pack()
# creating label;
l1 = Label(f1, width=20, font=("arial", 18, "bold"), bg="yellow", fg="red", text="result display here!")
l1.pack()
# button;
b1 = Button(f1, width=15, text="login here!", command=check)
b1.pack()
b2 = Button(f1, width=15, text="clear!", command=clear)
b2.pack()
# main loop
root.mainloop()
