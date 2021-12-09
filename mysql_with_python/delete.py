# importing module;
import pymysql as mysql

# set connection between mysql and python;
connection = mysql.connect(host='localhost',user='root',password='root',database='demo')

# current position of curser;
curser_position = connection.cursor()

# my sql query;
mysql_query = "DELETE FROM student WHERE id = 1"

curser_position.execute(mysql_query)

connection.commit()
connection.close()

