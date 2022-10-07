from imports import *
from connection_file import *
from extract import *


# converting to csv
ans = input('Do you want to convert to csv? Enter Y/N: ')
if ans ==  'Y':
    data = resultstore
    dfcsv = pd.DataFrame(data)

    print(dfcsv)
    dfcsv.to_csv('file1.csv',index = False)
    cnx.close()
    print('CSV Generated')
else:
    print('Done Executing without generating CSV')
