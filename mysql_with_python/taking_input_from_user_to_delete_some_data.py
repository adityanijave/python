# importing module;
import pymysql as mysql

# set connection between mysql and python;
connection = mysql.connect(host='localhost', user='root', password='root', database='demo')

# current position of curser;
curser_position = connection.cursor()

# taking id number to delete some data;
id = int(input("enter the id number to delete data : "))

# the sql query;
mysql_query = "DELETE FROM student WHERE id = %s"

#  executing the query;
curser_position.execute(mysql_query, id)

# committing the connection;
connection.commit()

# closing the connection;
connection.close()