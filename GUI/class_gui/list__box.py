from tkinter import *


def opertation():
    s1=""
    arr = list1.curselection()
    for i in arr :
        s1 += ","+ list1.get(i)

    label["text"] = s1




root = Tk()
root.title("my window")
root.geometry("500x500")
frame = Frame(root, height=500, width=500, bg="red").pack(fill=BOTH, expand=True)
label = Label(frame, font=("arial", 18, "bold"), bg="orange", fg="black", text="result is here!").pack()
button = Button(frame, width=15, text="click here!", command=opertation).pack()


# listbox
list1 = Listbox(frame, selectmode=MULTIPLE)
arr = ["a","b","c","d"]
for i in range(len(arr)):
    list1.insert(i,arr[i])
list1.pack()


root.mainloop()
