import mysql.connector as sql
import pandas as pd

def connect_to_database():
    try:
        connection = sql.connect(
            host="35.188.203.147",
            user="root",
            password="root123",
            database="antony",
            auth_plugin='mysql_native_password'
        )
        return connection
    except sql.Error as error:
        print("Error connecting to MySQL:", error)
        return None
