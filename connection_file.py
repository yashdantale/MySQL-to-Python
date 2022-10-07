import imports
from imports import *
try:
        print('Starting the Program')
        cnx = mysql.connector.connect(
                host= input('Enter Host: '),
                user= input('Enter User: '),
                password=getpass.getpass('Enter Password: '),
                port= input('Enter port: '),
                database = input('Enter Database: ')
        )
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
