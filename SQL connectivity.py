import pymysql

conn =pymysql.connect(

    host= 'localhost',
    user ='root',
    password='iLikethisOne#05',
    database='myclass'

)

print("connection successful")
cursor = conn.cursor()
cursor.execute("show tables")
for table in cursor:
    print(table)

cursor.execute(f"select * from {'project'}")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()




