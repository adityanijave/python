import pymysql as mysql
connection = mysql.connect(host='localhost', user='root', password='root', database='demo')

curser_position = connection.cursor()

mysql_query = "insert into student values(9,'mayur','gavnde')"

curser_position.execute(mysql_query)
connection.commit()
connection.close()