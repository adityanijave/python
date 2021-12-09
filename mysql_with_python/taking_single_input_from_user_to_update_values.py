# importing module 'pymysql';
import pymysql as mysql

# after importing module now, set up the connection between python and mysql databases;
connection = mysql.connect(host="localhost", user="root", password="root", database="demo")

# after setting connection between python and mysql now , set position of curser;
current_position_curser = connection.cursor()


identification_number = int(input("enter the id where you want to update the data: "))
fname = input("enter the fname to update : ")
lname = input("enter the lname to update : ")


# taking query to execute;
mysql_query = "UPDATE student SET fname=%s, lname=%s WHERE id=%s"
multiple_values_to_update =(fname,lname,identification_number)

current_position_curser.execute(mysql_query, multiple_values_to_update)

connection.commit()
connection.close()

