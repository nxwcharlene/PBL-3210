## To connect python code to mysql database from a remote computer
## users: valerie, cheklin, yuren, lisa, greg
## password: sharedpassword
## host: 172.22.143.201

# Copy the below chunk into your python code. Change the user and host accordingly.
# IMPT: ALWAYS COPY THE db_connection.close() to the end of your code to end the connection.
# Otherwise the connection will be left hanging and the database will be flooded with too many connections.

# -----------------------------------------------------------------------------------------------

import mysql.connector
db_connection = mysql.connector.connect(user='root', password='sharedpassword',host='127.0.0.1',
                                     port='3306', database='bf3210_database')
db_cursor = db_connection.cursor()  # create database cursor to perform SQL operations


## INSERT ANY SQL STATEMENTS AND DATA EXTRACTION CODES HERE
## SOME EXAMPLE CODES ARE SHOWN BELOW


# IMPT: close connection to mysql database
db_connection.close()

# -----------------------------------------------------------------------------------------------

# Example codes:

# SQL = "SHOW TABLES"
# db_cursor.execute(SQL)
# for table in db_cursor:
#     print(table)

# SQL = "SELECT * FROM macro"
# db_cursor.execute(SQL)
# for each in db_cursor:
#     print(each)