
import pymysql as mysql
connection = mysql.connect(host='localhost',user='root',password='root',database='demo')
current_position_curser = connection.cursor()

id = int(input("ENTER THE ID : "))
fname = input("ENTER THE FIRST NAME : ")
lname = input("ENTER THE LAST NAME : ")

mysql_query = "insert into student values(%s,%s,%s)"
single_mysql_query = (id,fname,lname)

current_position_curser.execute(mysql_query,single_mysql_query)

connection.commit()
connection.close()

