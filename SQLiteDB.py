import sqlite3
import pandas as pd

connection= sqlite3.connect(":memory:")

cursor = connection.cursor()


createquery="""CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    hire_date DATE,
    salary DECIMAL(10, 2)
);"""

cursor.execute(createquery)


insertquery="""INSERT INTO employees (employee_id, first_name, last_name, hire_date, salary)
VALUES 
(2, 'Bob', 'Jones', '2026-03-22', 62000.00),
(3, 'Charlie', 'Brown', '2026-05-01', 58000.00),
(4, 'Diana', 'Prince', '2026-06-08', 91000.00);"""

cursor.execute(insertquery)

selectquery="select * from employees"
data=pd.read_sql_query(selectquery,connection)
print(data)

cursor.close()
connection.close()