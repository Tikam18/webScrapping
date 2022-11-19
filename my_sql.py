import mysql.connector

mydb = mysql.connector.connect(host='localhost', user="tikam", passwd="4231",database="telusko")

mycursor = mydb.cursor()

mycursor.execute("select * from student")

result = mycursor.fetchone()

for i in mycursor:
    print(i)

