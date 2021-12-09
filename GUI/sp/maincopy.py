from tkinter import *
import pymysql as mysql
connection = mysql.connect(host="localhost", user="root", password="root", database="student")
current_position_of_curser = connection.cursor()


def insert():
    # taking enters;
    id = int(entry_for_id.get())
    name = str(entry_for_name.get())
    surname = str(entry_for_surname.get())

    # my sql query;
    mysql_query = "insert into info values(%s, %s, %s)"

    # format;
    required_format = (id, name, surname)
    multi_input = tuple(required_format)

    # executing code;
    current_position_of_curser.execute(mysql_query, multi_input)

    # label on status;
    Label(frame_one, width=50, font=("arial", 10, "bold"), bg="orange", text="ALL DATA IS INSERTED SUCCESSFULLY",
          fg="black").pack(side="bottom", anchor="s")


def update_some_data():

    # taking enters;
    id = int(entry_for_id.get())
    name = str(entry_for_name.get())
    surname = str(entry_for_surname.get())

    # my sql query;
    mysql_query = "UPDATE info SET name=%s, surname=%s WHERE id = %s"

    # format;
    required_format = (name, surname, id)
    multi_input = tuple(required_format)

    # executing code;
    current_position_of_curser.execute(mysql_query, multi_input)

    # label on status;
    Label(frame_one, width=50, font=("arial", 10, "bold"), bg="orange", text="DATA IS UPDATED SUCCESSFULLY",
          fg="black").pack(side="bottom", anchor="s")


def update_all_data():

    # taking enters;
    id = int(entry_for_id.get())
    name = str(entry_for_name.get())
    surname = str(entry_for_surname.get())

    # my sql query;
    mysql_query = " UPDATE info SET name = %s, surname = %s "

    # format;
    required_format = (name, surname)
    multi_input = tuple(required_format)

    # executing code;
    current_position_of_curser.execute(mysql_query, multi_input)

    # label on status;
    Label(frame_one, width=50, font=("arial", 10, "bold"), bg="orange", text="ALL DATA IS UPDATED SUCCESSFULLY",
          fg="black").pack(side="bottom", anchor="s")


def delete_some_data():

    # taking enters;
    id = int(entry_for_id.get())
    name = str(entry_for_name.get())
    surname = str(entry_for_surname.get())

    # my sql query;
    mysql_query = "DELETE FROM info WHERE id = %s"

    # format;
    required_format = id
    multi_input = tuple(required_format)

    # executing code;
    current_position_of_curser.execute(mysql_query, multi_input)

    # label on status;
    Label(frame_one, width=50, font=("arial", 10, "bold"), bg="orange", text="DATA IS DELETED SUCCESSFULLY",
          fg="black").pack(side="bottom", anchor="s")


def delete_all_data():
    # the sql query;
    mysql_query = "DELETE FROM info "

    #  executing the query;
    current_position_of_curser.execute(mysql_query)

    # committing the connection;
    connection.commit()

    # replay on curser;
    print("ALL DATA IS DELETED SUCCESSFULLY")

    # label on status;
    Label(frame_one, width=50, font=("arial", 10, "bold"), bg="orange", text="ALL DATA IS DELETED SUCCESSFULLY", fg="black").pack(side="bottom", anchor="s")


def clear():
    entry_for_id.delete(0, END)
    entry_for_name.delete(0, END)
    entry_for_surname.delete(0, END)


# class;
root = Tk()

# tittle;
root.title("student info")

# dimensions;
root.geometry("972x500")
root.maxsize(972, 500)
root.minsize(500, 500)

# frames;
frame_one = Frame(root, width=2000, height=500, bg="lightblue")

# labels;
label_at_top = Label(frame_one, width=200, font=("arial", 10, "bold"), bg="grey", fg="black",
                     text="hello welcome to aditya's window").pack(side="top")
label_at_bottom = Label(frame_one, width=200, font=("arial", 10, "bold"), bg="yellow", fg="red",
                        text="DATABASE OF MODERN COLLEGE OF ENGINEERING STUDENTS").pack(side="bottom")
label_for_status = Label(frame_one, width=8, font=("arial", 10, "bold"), bg="blue", text="status : ", fg="white").pack(side="bottom", anchor="sw")

# buttons;
button_insert = Button(frame_one, width=15, text="insert", command=insert, bg="orange").pack(side="left", pady=100)
button_update_some_data = Button(frame_one, width=15, text="update some data", command=update_some_data, bg="orange").pack(side="left")
button_update_all_data = Button(frame_one, width=15, text="update all data", command=update_all_data, bg="orange").pack(side="left")
button_delete_some_data = Button(frame_one, width=15, text="delete some data", command=delete_some_data, bg="orange").pack(side="left")
button_delete_all_data = Button(frame_one, width=15, text="delete all data", command=delete_all_data, bg="orange").pack(side="left")
button_for_delete = Button(frame_one, width=15, text="clear", command=clear, bg="orange").pack(side="left")

# entry;
entry_for_id = Entry(frame_one, width=15)
entry_for_id.pack(side="left")
entry_for_name = Entry(frame_one, width=15)
entry_for_name.pack(side="left")
entry_for_surname = Entry(frame_one, width=15)
entry_for_surname.pack(side="left")


# packing frame one;
frame_one.pack(fill=BOTH, expand=True)

#  main loop;
root.mainloop()
# committing connection of mysql;
connection.commit()

# closing the connection of mysql with python;
connection.close()
