import csv
oldfilename = "stockprice_cleandata_001to020.csv"
tempfilename = "stockprice_temp_cleandata.csv"


def is_integer_tryexcept(any_string):
    # Returns True if string is an integer.
    try:
        int(any_string)
        return True
    except ValueError:
        return False


def clean_stockid(oldfilename,tempfilename): # check if stockid is an integer
    with open(oldfilename,"r") as oldfile:
        reader = csv.reader(oldfile)
        readerlist = list(reader)
        with open(tempfilename,"w") as newfile:
            writer = csv.writer(newfile)

            for eachrow in readerlist:
                if is_integer_tryexcept(eachrow[0]):
                    None
                else:
                    print("Error in stock_id format:", eachrow) # Does not overwrite old file


def clean_dates(oldfilename,tempfilename): # datetime format in mysql is YYYY-MM-DD
    with open(oldfilename,"r") as oldfile:
        reader = csv.reader(oldfile)
        readerlist = list(reader)
        with open(tempfilename,"w") as newfile:
            writer = csv.writer(newfile)

            for eachrow in readerlist:
                # Keep YYYY-MM-DD
                if len(eachrow[1]) == 10 and eachrow[1][4] == "-" and eachrow[1][7] == "-":
                    # print(eachrow) # just to check
                    None
                # Convert all mm/dd/yyyy to YYYY-MM-DD
                elif len(eachrow[1]) == 10 and eachrow[1][2] == "/" and eachrow[1][5] == "/":
                    olddate = eachrow[1]
                    eachrow[1] = "{}-{}-{}".format(olddate[-4:], olddate[:2], olddate[3:5])
                    # print(eachrow[1]) # just to check
                # Convert all mm/dd/yy to YYYY-MM-DD
                elif len(eachrow[1]) == 8 and eachrow[1][2] == "/" and eachrow[1][5] == "/":
                    olddate = eachrow[1]
                    eachrow[1] = "20{}-{}-{}".format(olddate[-2:],olddate[:2],olddate[3:5])
                    # print(eachrow[1]) # just to check
                # Convert m/d/yy to YYYY-MM-DD
                elif len(eachrow[1]) == 6 and eachrow[1][1] == "/" and eachrow[1][3] == "/":
                    olddate = eachrow[1]
                    eachrow[1] = "20{}-0{}-0{}".format(olddate[-2:], olddate[0], olddate[2])
                    # print(eachrow[1]) # just to check
                # Convert m/dd/yy to YYYY-MM-DD
                elif len(eachrow[1]) == 7 and eachrow[1][1] == "/" and eachrow[1][4] == "/":
                    olddate = eachrow[1]
                    eachrow[1] = "20{}-0{}-{}".format(olddate[-2:], olddate[0], olddate[2:4])
                    # print(eachrow[1]) # just to check
                # Convert mm/d/yy to YYYY-MM-DD
                elif len(eachrow[1]) == 7 and eachrow[1][2] == "/" and eachrow[1][4] == "/":
                    olddate = eachrow[1]
                    eachrow[1] = "20{}-{}-0{}".format(olddate[-2:], olddate[0:2], olddate[3])
                    # print(eachrow[1])  # just to check
                # Convert m/dd/yyyy to YYYY-MM-DD
                elif len(eachrow[1]) == 9 and eachrow[1][1] == "/" and eachrow[1][4] == "/":
                    olddate = eachrow[1]
                    eachrow[1] = "{}-0{}-{}".format(olddate[-4:], olddate[0], olddate[2:4])
                    # print(eachrow[1])  # just to check
                else:
                    print("Error in date formatting:", eachrow)

                writer.writerow(eachrow)


def overwrite_oldfile(oldfilename,tempfilename):
    with open(tempfilename,"r") as tempfile:
        reader = csv.reader(tempfile)
        readerlist = list(reader)
        with open(oldfilename,"w") as oldfile:
            writer = csv.writer(oldfile)

            for eachrow in readerlist:
                writer.writerow(eachrow)


def is_number_tryexcept(any_string):
    # Returns True if string is a number.
    try:
        float(any_string)
        return True
    except ValueError:
        return False


def clean_price(oldfilename, tempfilename):
    with open(oldfilename,"r") as oldfile:
        reader = csv.reader(oldfile)
        readerlist = list(reader)
        with open(tempfilename,"w") as newfile:
            writer = csv.writer(newfile)

            for eachrow in readerlist:
                if is_number_tryexcept(eachrow[2]):
                    oldprice = float(eachrow[2])
                    eachrow[2] = "{:.4f}".format(oldprice)
                    # print(eachrow[2])
                else:
                    print("Error in results formatting:", eachrow)

                writer.writerow(eachrow)


## ---------------------------------------------
## ACTUAL DATA CLEANING PROGRAM
## ---------------------------------------------
# clean_stockid(oldfilename,tempfilename)
# clean_dates(oldfilename,tempfilename)
# overwrite_oldfile(oldfilename,tempfilename)
# clean_price(oldfilename,tempfilename)
# overwrite_oldfile(oldfilename,tempfilename)
# print("Data cleaning is done!")