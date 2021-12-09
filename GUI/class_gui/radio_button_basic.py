# root, width, height, bg, fg, text, font

# importing package;
from tkinter import *

# creating object of tkinter;
root = Tk()

# after creating object , let's give title to root window;
root.title("My Window")

# after title, let's set the general geometry of root window;
root.geometry("500x500")

# now , create the frame window ;
frame = Frame(root, width=500, height=500, bg="red")
frame.pack(fill=BOTH, expand=True)

# creating radiobutton;
v = IntVar()
radio_button_one = Radiobutton(frame, text="male", value=0, var=v)
radio_button_one.pack()

radio_button_two = Radiobutton(frame, text="female", value=1, var=v)
radio_button_two.pack()

# at the end let's call the main loop,
root.mainloop()