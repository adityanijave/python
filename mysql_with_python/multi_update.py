# importing module 'pymysql';
import pymysql as mysql

# after importing module now, set up the connection between python and mysql databases;
connection = mysql.connect(host="localhost", user="root", password="root", database="demo")

# after setting connection between python and mysql now , set position of curser;
current_position_curser = connection.cursor()

# taking query to execute;
mysql_query = "UPDATE student SET fname=%s, lname=%s WHERE id=%s"
multiple_values_to_update =(("aditya","nijaqqqqqqqqqqqqqqqve",1),("adu","ruhi",2))

current_position_curser.executemany(mysql_query, multiple_values_to_update)

connection.commit()
connection.close()