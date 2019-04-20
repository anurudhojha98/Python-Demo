
import csv
with open("employees.csv",'r') as f:
    """First Way to read csv files"""
    # reader=csv.reader(f)
    # for coloumn in reader:
    #     print(coloumn[0].ljust(10),coloumn[1].ljust(10),coloumn[2].ljust(10),coloumn[3])

    """Second way to read csv as dictionary"""
    reader=csv.DictReader(f)
    for column in reader:
        print(column['First name'].ljust(10),column['Last name'].ljust(10),column['Company'].ljust(10),column['Email'])

