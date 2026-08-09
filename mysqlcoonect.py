import mysql.connector

try:
    coonection=mysql.connector.connect(
        host='',
        user='',
        password='',
        database='',
        port=""
    )
    print("mysql connected")
except mysql.connector.Error as err:
    print("error is" +err)