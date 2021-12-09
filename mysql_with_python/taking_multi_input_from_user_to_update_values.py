# importing module and setting connection between python and mysql
import pymysql as mysql

connection = mysql.connect(host='localhost', user='root', password='root', database='demo')

# setting cursor current position in databases
current_cursor_position = connection.cursor()

# required empty list
list = list()

# setting while loop for  to take number of inputs from user and then  barking it's  need complete!
while True:
    user = input("enter your response in 'y' or 'n' terms : ")
    if user == 'y' or user == 'n':
        if user == "n":
            print(f"DATA IS UPDATED (if provided!)")
            break

        elif user == "y":

            identification_number = int(input("ENTER THE ID WHERE YOU WANT TO UPDATE THE DATA : "))
            fname = input("ENTER THE FIRST NAME : ")
            lname = input("ENTER THE LAST NAME : ")
            data = (fname, lname, identification_number)
            list.append(data)



    else:
        print("please , enter valid entry!")

mysql_query = "UPDATE student SET fname=%s, lname=%s WHERE id=%s"
mysql_multi_argument = tuple(list)

current_cursor_position.executemany(mysql_query, mysql_multi_argument)

connection.commit()
connection.close()