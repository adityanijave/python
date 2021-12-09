import pymysql as mysql

connection = mysql.connect(host='localhost', user='root', password='root', database='demo')
current_curser_position = connection.cursor()

mysql_query = "insert into student values(%s,%s,%s)"
multiple_values_to_insert = ((10,'a10','b10'),(11,'a11','b11'),(12,'a12','b12'))
current_curser_position.executemany(mysql_query,multiple_values_to_insert)

connection.commit()

connection.close()