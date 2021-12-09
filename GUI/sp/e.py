from tkinter import *
import pymysql as mysql


# connection = mysql.connect(host="localhost", user="root", password="root", database="student")
# current_position_of_curser = connection.cursor()

root = Tk()
root.geometry("500x500")
root.title("my window")

f1 = Frame(height="500", width="500", bg="red")

b1 = Button(f1, width="18", bg="yellow", fg="black", text="click here!")
b1.grid()
























# connection.commit()
# connection.close()

f1.grid()
root.mainloop()