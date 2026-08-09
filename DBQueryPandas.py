import psycopg2
import pandas as pd
##dburl="postgresql://postgres:99Manvik99@localhost:5432/Python"
try:
    coonection=psycopg2.connect(
        host="localhost",
        port="5432",
        user="postgres",
        password="99Manvik99",
        dbname="Python"
    )
    print("postgre sql connected")
except psycopg2.Error as err:
    print(f"error is: {err}")

querysql="""SELECT * FROM public."Product" ORDER BY id ASC"""

dfdata=pd.read_sql_query(querysql,coonection)
print(dfdata)

coonection.close()