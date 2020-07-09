# What - we are trying to establish a connection and read data from the database in the python console
# In real time we see the output in the graphical user interface GUI
# pyodbc - just a python library helps you connect to database

# why - helping us to showcase data in the console which in real time, we would display

#import correct module
# find variables with login detaails (server,databse, username, password)
# connectionstring concatenated the variables
# troubleshoot
# with loop
# try for 5 seconds
import pyodbc

server = 'databases2.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

# Specifying the ODBC driver, server name, database, etc. directly
# cnxnString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE'+database+';UID='+username+';PWD='password

connectionString='DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password
try:
    with pyodbc.connect(connectionString, time=5) as connection:
        print("Connection did not time out")
except:
    print("Connection Time out")
else:
    pass
    # acquire a cursor from a connection-execute the code-through
    # the cursor-cursor.fetch-iterate through the results by using the raw objects that are returned by the cursor.fetch
    #
    cursor = connection.cursor()
