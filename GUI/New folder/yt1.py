# importing package;
from tkinter import *
# creating class;
root = Tk()
# general geometry("width x height");
root.geometry("733x434")
# min size of root window(width, height);
root.minsize(250, 250)
#  max size of root window(width, height);
root.maxsize(750, 750)
# label :
label = Label(text="WELCOME TO PYCHARM!")
label.pack()
# mainloop;
root.mainloop()