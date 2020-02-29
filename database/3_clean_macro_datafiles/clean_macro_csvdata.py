import csv
oldfilename = "macro_cleandata2000to2020.csv"
tempfilename = "macro_temp_cleandata.csv"


def clean_dates(oldfilename,tempfilename): # datetime format in mysql is YYYY-MM-DD
    with open(oldfilename,"r") as oldfile:
        reader = csv.reader(oldfile)
        readerlist = list(reader)
        with open(tempfilename,"w") as newfile:
            writer = csv.writer(newfile)

            for eachrow in readerlist:
                # Keep YYYY-MM-DD
                if len(eachrow[0]) == 10 and eachrow[0][4] == "-" and eachrow[0][7] == "-":
                    # print(eachrow) # just to check
                    None
                # Convert all mm/dd/yy to YYYY-MM-DD
                elif len(eachrow[0]) == 8 and eachrow[0][2] == "/" and eachrow[0][5] == "/":
                    olddate = eachrow[0]
                    eachrow[0] = "20{}-{}-{}".format(olddate[-2:], olddate[:2],olddate[3:5])
                    # print(eachrow) # just to check
                # Convert all other original formats to mm/dd/yy first then YYYY-MM-DD
                elif len(eachrow[0]) > 8:
                    olddate = eachrow[0]
                    newdate = olddate[0:8] # take the first 8 characters mm/dd/yy
                    eachrow[0] = "20{}-{}-{}".format(newdate[-2:],newdate[:2],newdate[3:5])
                    # print(eachrow) # just to check
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


def clean_time(oldfilename, tempfilename): # datetime format in mysql is hh:mm:ss
    with open(oldfilename,"r") as oldfile:
        reader = csv.reader(oldfile)
        readerlist = list(reader)
        with open(tempfilename,"w") as newfile:
            writer = csv.writer(newfile)

            for eachrow in readerlist:
                # Keep hh:mm:ss
                if len(eachrow[1]) == 8 and eachrow[1][2] == ":" and eachrow[1][5] == ":":
                    # print(eachrow) # just to check
                    None
                # Convert hh:mm to hh:mm:ss
                elif len(eachrow[1]) == 5 and eachrow[1][2] == ":":
                    oldtime = eachrow[1]
                    newtime = oldtime + ":00"
                    eachrow[1] = newtime
                    # print(eachrow) # just to check
                # Convert h:mm to hh:mm:ss
                elif len(eachrow[1]) == 4 and eachrow[1][1] == ":":
                    oldtime = eachrow[1]
                    newtime = "0" + oldtime + ":00"
                    eachrow[1] = newtime
                    # print(eachrow) # just to check
                # Keep blank values
                elif len(eachrow[1]) == 0:
                    # print(eachrow) # just to check
                    None
                else:
                    print("Error in time formatting:", eachrow)

                writer.writerow(eachrow)


def is_number_tryexcept(any_string):
    # Returns True if string is a number.
    try:
        float(any_string)
        return True
    except ValueError:
        return False


def clean_results(oldfilename, tempfilename, columnindex): # Actual [5], Prior [6], SurvM [7], SurvA [8]
    with open(oldfilename,"r") as oldfile:
        reader = csv.reader(oldfile)
        readerlist = list(reader)
        with open(tempfilename,"w") as newfile:
            writer = csv.writer(newfile)

            for eachrow in readerlist:
                # Keep blank values as ""
                if eachrow[columnindex] == "" or eachrow[columnindex] == "--":
                    eachrow[columnindex] = ""
                    # print("Blank", eachrow[columnindex]) # just to check
                # Numerics (e.g. 55.5, 0.4, -0.8, 58)
                elif is_number_tryexcept(eachrow[columnindex]):
                    oldresult = float(eachrow[columnindex])
                    newresult = "{:.2f}".format(oldresult)
                    eachrow[columnindex] = newresult
                    # print(eachrow[columnindex]) # just to check
                # Convert all percentages to 2dp, keep % sign (e.g. 2.60%, -1.10%)
                elif eachrow[columnindex][-1] == "%":
                    oldresult = float(eachrow[columnindex][0:-1])
                    newresult = "{:.2f}".format(oldresult)
                    eachrow[columnindex] = newresult + "%"
                    # print(eachrow[columnindex]) # just to check
                # Convert millions (m) to numbers
                elif eachrow[columnindex][-1] == "m":
                    newresult = int(float(eachrow[columnindex][0:-1])*1000000)
                    eachrow[columnindex] = newresult
                    # print(eachrow[columnindex]) # just to check
                # Convert thousands (k) to numbers
                elif eachrow[columnindex][-1] == "k":
                    newresult = int(float(eachrow[columnindex][0:-1]) * 1000)
                    eachrow[columnindex] = newresult
                    # print(eachrow[columnindex]) # just to check
                # Convert positive billions ($b) to numbers
                elif eachrow[columnindex][-1] == "b" and eachrow[columnindex][0] == "$":
                    newresult = int(float(eachrow[columnindex][1:-1]) * 1000000000)
                    eachrow[columnindex] = newresult
                    # print(eachrow[columnindex]) # just to check
                # Convert negative billions (-$b) to numbers
                elif eachrow[columnindex][-1] == "b" and eachrow[columnindex][1] == "$":
                    newresult = int(float(eachrow[columnindex][2:-1]) * 1000000000)
                    eachrow[columnindex] = -newresult
                    # print(eachrow[columnindex]) # just to check
                else:
                    print("Error in results formatting:", eachrow)

                writer.writerow(eachrow)


def clean_surprise(oldfilename,tempfilename):
    with open(oldfilename,"r") as oldfile:
        reader = csv.reader(oldfile)
        readerlist = list(reader)
        with open(tempfilename, "w") as newfile:
            writer = csv.writer(newfile)

            for eachrow in readerlist:
                # Convert all blanks to ""
                if eachrow[10] == "" or eachrow[10] == "--":
                    eachrow[10] = None
                    # print("Blank", eachrow[10]) # just to check
                # Convert all numerics to 2dp
                elif is_number_tryexcept(eachrow[10]):
                    oldresult = float(eachrow[10])
                    newresult = "{:.2f}".format(oldresult)
                    eachrow[10] = newresult
                    # print(eachrow[10]) # just to check
                else:
                    print("Error in surprise formatting:", eachrow)

                writer.writerow(eachrow)


def clean_stdev(oldfilename, tempfilename):
    with open(oldfilename,"r") as oldfile:
        reader = csv.reader(oldfile)
        readerlist = list(reader)
        with open(tempfilename,"w") as newfile:
            writer = csv.writer(newfile)

            for eachrow in readerlist:
                if eachrow[11] == "" or eachrow[11] == "--":
                    eachrow[11] = ""
                    # print("Blank",eachrow[11]) # just to check
                elif is_number_tryexcept(eachrow[11]):
                    oldresult = float(eachrow[11])
                    eachrow[11] = "{:.2f}".format(oldresult)
                    # print(eachrow[11]) # just to check
                else:
                    print("Error in stdev formatting:", eachrow)

                writer.writerow(eachrow)


## ---------------------------------------------
## ACTUAL DATA CLEANING PROGRAM
## ---------------------------------------------
clean_dates(oldfilename, tempfilename)
overwrite_oldfile(oldfilename, tempfilename)
clean_time(oldfilename,tempfilename)
overwrite_oldfile(oldfilename,tempfilename)
clean_results(oldfilename,tempfilename,5) # cleans Actual
overwrite_oldfile(oldfilename,tempfilename)
clean_results(oldfilename,tempfilename,6) # cleans Prior
overwrite_oldfile(oldfilename,tempfilename)
clean_results(oldfilename,tempfilename,7) # cleans SurvM
overwrite_oldfile(oldfilename,tempfilename)
clean_results(oldfilename,tempfilename,8) # cleans SurvA
overwrite_oldfile(oldfilename,tempfilename)
clean_surprise(oldfilename,tempfilename)
overwrite_oldfile(oldfilename,tempfilename)
clean_stdev(oldfilename,tempfilename)
overwrite_oldfile(oldfilename,tempfilename)
print("Data cleaning is done!")