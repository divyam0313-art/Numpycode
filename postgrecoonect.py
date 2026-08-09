import psycopg2

try:
    psycopg2.connect(
        host="",
        user="",
        password="",
        databasename=""
    )
    print("postgre sql connected")
except psycopg2.Error as err:
    print(f"error is: {err}")