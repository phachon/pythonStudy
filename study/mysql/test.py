import mysql.connector

conn = mysql.connector.connect(user='root', password='123456', database='bms_account')

cursor = conn.cursor()

select = 'select * from bms_account'
cursor.execute(select)

rs = cursor.fetchall()

for row in rs:
	print("name=%s, given_name=%s" % (row[1], row[2]))

cursor.close()
conn.close()
