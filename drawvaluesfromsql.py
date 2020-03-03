import mysql.connector
import pandas as pd
db_connection = mysql.connector.connect(user='root', password='Gregory2',host='localhost',
                                     port='3306', database='pbl3210 db')
#macrotabl= pd.read_sql_query("SELECT * FROM MACRO",db_connection)

stockidtab=pd.read_sql_query("SELECT * FROM STOCK_ID",db_connection)
stockpricetab=pd.read_sql_query("SELECT * FROM STOCKPRICE",db_connection)

print(stockidtab)
print(stockpricetab)
