from tkinter import *

# root window ;
root = Tk()

# window tittle ;
root.title("demo window!")

# geometry ;
root.geometry("500x500")

#  creating frame with bg
frame1 = Frame(root,width = 500, height = 500, bg = "red")
frame1.pack(fill = BOTH, expand = True)
# main loop
root.mainloop()