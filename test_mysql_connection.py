# test_mysql_connection.py
import mysql.connector

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='employees_db'
    )

    if connection.is_connected():
        print("Connected to MySQL database")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
