
# connecting to mysql database to the python code, from a remote computer

import mysql.connector
import pandas as pd
db_connection = mysql.connector.connect(user='greg', password='sharedpassword',host='172.22.143.201',
                                     port='3306', database='bf3210_database')
macrotabl= pd.read_sql_query("SELECT * FROM MACRO",db_connection)



print(macrotabl)
db_cursor = db_connection.cursor()  # create database cursor to perform SQL operations

SQL = "SHOW TABLES"
db_cursor.execute(SQL)
for table in db_cursor:
    print(table)

'''SQL = "SELECT * FROM macro"
db_cursor.execute(SQL)
for each in db_cursor:
    print(each)'''

# close connection to mysql database
db_connection.close()
