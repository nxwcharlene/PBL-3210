import mysql.connector as sql
import pandas as pd

db_connection = sql.connect(user='valerie', password='sharedpassword',host='172.22.143.201',
                                     port='3306', database='bf3210_database')
db_cursor = db_connection.cursor()
db_cursor.execute('SELECT * FROM macro') #change tablename

table_rows = db_cursor.fetchall()

db_cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME=N'macro' order by ordinal_position")
column_name=db_cursor.fetchall()
print(column_name)
list1=[]
for i in column_name:
    list1.append(''.join(i))
print(list1)

df = pd.DataFrame(table_rows,columns=list1)
print(df)   
# close connection to mysql database
db_connection.close()
