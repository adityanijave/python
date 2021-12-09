from tkinter import *

root = Tk()
root.title("my window")
root.geometry("500x500")


def check():
    empty_string = ""
    if variable.get() == 1:
        empty_string += "male"
    elif variable.get() == 0:
        empty_string += "female"
    label.configure(text=empty_string)


frame = Frame(root, width=500, height=500, bg="red")
frame.pack(fill=BOTH, expand=True)
variable = IntVar()
radio_button_one = Radiobutton(frame, text="male", value=1, var=variable)
radio_button_one.pack()
radio_button_two = Radiobutton(frame, text="female", value=0, var=variable)
radio_button_two.pack()
label = Label(frame, width=20, font=("arial", 23, "bold"), bg="yellow", fg="red", text="result!")
label.pack()

button = Button(frame, width=15, text="click here!", command=check)
button.pack()

root.mainloop()
