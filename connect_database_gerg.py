
# connecting to mysql database to the python code, from a remote computer

import mysql.connector
import pandas as pd
db_connection = mysql.connector.connect(user='root', password='Gregory2',host='localhost',
                                     port='3306', database='pbl3210 db')
#macrotabl= pd.read_sql_query("SELECT * FROM MACRO",db_connection)

stockidtab=pd.read_sql_query("SELECT * FROM STOCK_ID",db_connection)
stockpricetab=pd.read_sql_query("SELECT * FROM STOCKPRICE",db_connection)

print(stockidtab)
print(stockpricetab)


#print(macrotabl)
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
