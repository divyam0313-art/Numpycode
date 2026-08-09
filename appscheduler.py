import psycopg2
import pandas as pd
import schedule
import time
##dburl="postgresql://postgres:99Manvik99@localhost:5432/Python"
def dbcall():
    try:
        coonection=psycopg2.connect(
            host="localhost",
            port="5432",
            user="postgres",
            password="99Manvik99",
            dbname="Python"
        )
        print("postgre sql connected")
        querysql="""call public."Dailyupdate"();"""
        coonection.autocommit=True

        cur=coonection.cursor()
        cur.execute(querysql)
        print("update executed")
    except psycopg2.Error as err:
        print(f"error is: {err}")

    except Exception as e:
        print(e is +e)


    cur.close()
    coonection.close()

def job():
    print("job started");
    dbcall()

schedule.every().day.at("17:18").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)