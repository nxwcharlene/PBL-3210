"""
BUILDING OUR OWN DATABASE
    database name: bf3210_database
    table 1: macro (economic releases) (data source: csv file)
    table 2: list of dates and US share prices (data source: API)
    table 3: US company earnings releases

PART 1: Creating the database and tables: 
    1. create_database(db_name): Create remote database in MySQL
    2. create_table(table_name): Create table with headers in database
"""

def create_database(db_name):
    import csv, os, mysql.connector
    db_connection = mysql.connector.connect(user='root', password='sharedpassword', host='127.0.0.1', port='3306')
    db_cursor = db_connection.cursor()  # create database cursor to perform SQL operations

    SQL = "CREATE DATABASE " + db_name
    db_cursor.execute(SQL)
    db_cursor.execute("SHOW DATABASES")  # to get a list of all databases
    print("New database successfully created. Existing databases:")
    for db in db_cursor:
        print(db)  # print all databases

    db_connection.close()


def create_macro_table(db_name, table_name):
    import csv, os, mysql.connector
    db_connection = mysql.connector.connect(user='root', password='sharedpassword', host='127.0.0.1',
                                            port='3306', database=db_name)
    db_cursor = db_connection.cursor()  # create database cursor to perform SQL operations

    SQL = "CREATE TABLE {} (Date DATE, Time VARCHAR(5), Event VARCHAR(100), Ticker VARCHAR(15), " \
          "Period VARCHAR(10), Actual VARCHAR(10), Prior VARCHAR(10), SurvM VARCHAR(10), SurvA VARCHAR(15), " \
          "NoEstimates VARCHAR(5), Surprise VARCHAR(10), StdDev VARCHAR(10), C VARCHAR(10))".format(table_name)
    db_cursor.execute(SQL)
    db_cursor.execute("SHOW TABLES") # get a list of all databases
    print("New table successfully created. Existing tables:")
    for table in db_cursor:
        print(table) # print all tables

    db_connection.close()


def create_stockprice_table(db_name, table_name):
    import csv, os, mysql.connector
    db_connection = mysql.connector.connect(user='root', password='sharedpassword', host='127.0.0.1',
                                            port='3306', database=db_name)
    db_cursor = db_connection.cursor()  # create database cursor to perform SQL operations

    SQL = "CREATE TABLE {} (stock_id INT, Date DATE, Price FLOAT)".format(table_name)
    db_cursor.execute(SQL)
    db_cursor.execute("SHOW TABLES") # get a list of all databases
    print("New table successfully created. Existing tables:")
    for table in db_cursor:
        print(table) # print all tables

    db_connection.close()


"""
PART 2: INSERTING DATA INTO TABLES FROM CSV FILE
1. Erase all data in table rows (optional)
2. Ensure table headers correspond to the same csv file headers
3. Read out the csv file's content (transactions.csv)
4. Insert those data into existing (blank) table
"""

def erase_table(db_name, table_name): # to clear all rows from table before inserting data again
    import csv, os, mysql.connector
    db_connection = mysql.connector.connect(user='root', password='sharedpassword', host='127.0.0.1',
                                            port='3306', database=db_name)
    db_cursor = db_connection.cursor()  # create database cursor to perform SQL operations

    sql_delete_query = "TRUNCATE TABLE {}".format(table_name)
    db_cursor.execute(sql_delete_query)
    db_connection.commit()

    db_connection.close()


def modify_column_specs(db_name, table_name, column_header):
    import csv, os, mysql.connector
    db_connection = mysql.connector.connect(user='root', password='sharedpassword', host='127.0.0.1',
                                            port='3306', database=db_name)
    db_cursor = db_connection.cursor()  # create database cursor to perform SQL operations

    column_specification = input("Please enter column specification (e.g. VARCHAR(100)): ")
    sql_modify_column = "ALTER TABLE {} MODIFY {} {}".format(table_name, column_header, column_specification)
    db_cursor.execute(sql_modify_column)
    db_connection.commit()

    db_connection.close()


def insert_csv_macrodata(db_name, table_name): # Inserting csv data into BLANK table
    import csv, os, mysql.connector
    db_connection = mysql.connector.connect(user='root', password='sharedpassword', host='127.0.0.1',
                                            port='3306', database=db_name)
    db_cursor = db_connection.cursor()  # create database cursor to perform SQL operations

    infile = "macro_cleandata_2000to2020.csv"
    with open(infile, "r") as infile_obj:
        data = list(csv.reader(infile_obj))

        for index, each in enumerate(data):
            print(index)
            if index != 0: # this skips the first line of data in the csv, which are headers
                SQL = "INSERT INTO {} (Date,Time,Event,Ticker,Period,Actual,Prior,SurvM,SurvA," \
                      "NoEstimates,Surprise,StdDev,C) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(table_name)
                data_tuple = (each[0], each[1], each[2], each[3], each[4], each[5], each[6],
                              each[7], each[8], each[9], each[10], each[11], each[12])
                db_cursor.execute(SQL, data_tuple)
                db_connection.commit()
                print(db_cursor.rowcount, "Record Inserted.")

    db_connection.close()


def insert_csv_stockpricedata(db_name, table_name): # Inserting csv data into BLANK table
    import csv, os, mysql.connector
    db_connection = mysql.connector.connect(user='root', password='sharedpassword', host='127.0.0.1',
                                            port='3306', database=db_name)
    db_cursor = db_connection.cursor()  # create database cursor to perform SQL operations

    infile = "stockprice_347to505.csv"
    with open(infile, "r") as infile_obj:
        data = list(csv.reader(infile_obj))

        for index, each in enumerate(data):
            print(index)
            if index != 0: # this skips the first line of data in the csv, which are headers
                SQL = "INSERT INTO {} (stock_id, Date, Price) VALUES (%s,%s,%s)".format(table_name)
                data_tuple = (each[0], each[1], each[2])
                db_cursor.execute(SQL, data_tuple)
                db_connection.commit()
                print(db_cursor.rowcount, "Record Inserted.")

    db_connection.close()


"""
MAIN PROGRAM: 
1. Create database
2. Create table with headers
3. Insert data from csv file into macro table
"""
# create_database('bf3210_database') # only needs to be created once
# create_macro_table('bf3210_database', 'macro') # only needs to be created once
# create_stockprice_table('bf3210_database', 'stockprice') # only needs to be created once
# modify_column_specs("bf3210_database","macro","NoEstimates") # only when necessary
# erase_table('bf3210_database', 'macro') # erase only when necessary
# insert_csv_macrodata('bf3210_database', 'macro') # insert each time there is an updated csv file
# erase_table('bf3210_database', 'stockprice') # erase only when necessary
# insert_csv_stockpricedata('bf3210_database', 'stockprice') # insert from previous row (check last record!)