
from imports import *
from connection_file import *


try:
  uploadfilepath = input('Enter path to SQL File: ')
  assert os.path.isfile(uploadfilepath)
  file = open(uploadfilepath)
  sql = file.read()


  cursor = cnx.cursor()
  database = cnx.database
  for result in cursor.execute(sql, multi=True):
    if result.with_rows:
      print("Rows produced by query '{}':".format(
        result.statement))
      resultstore = result.fetchall()
      print(resultstore)
    else:
      print("Number of rows affected by query '{}': {}".format(
        result.statement, result.rowcount))

  print('------------------------------------------------')

  print (resultstore)
except ValueError:
  print('Wrong Path')

