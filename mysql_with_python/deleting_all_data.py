# importing module;
import pymysql as mysql

# set connection between mysql and python;
connection = mysql.connect(host='localhost', user='root', password='root', database='demo')

# current position of curser;
curser_position = connection.cursor()

# the sql query;
mysql_query = "DELETE FROM student "

#  executing the query;
curser_position.execute(mysql_query)

# committing the connection;
connection.commit()

# closing the connection;
connection.close()