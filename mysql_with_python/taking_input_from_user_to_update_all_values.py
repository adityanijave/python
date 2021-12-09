# importing module;
import pymysql as mysql

# setting connection between python and mysql databases;
connection = mysql.connect(host='localhost', user='root', password='root', database='demo')

# setting cursor current position in databases;
current_cursor_position = connection.cursor()




# taking input;
fname = input("enter the fname for update : ")
lname = input("enter the lname for update : ")
data = (fname, lname)

# SETTING QUERY FOR UPDATE ALL DATA;
mysql_query = "UPDATE student SET fname = %s, lname = %s "
array = tuple(data)
# after query let's execute it;
current_cursor_position.execute(mysql_query, array)

# now, commit our connection;
connection.commit()

# at the end let's  close the connection;
connection.close()