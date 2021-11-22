import components.dbconnection as db
from numpy import genfromtxt
from datetime import datetime
import os
import numpy as numpy
import inquirer as iq

def uploadData():
#TODO: Implementing uploadData method
    try: 
        print("uploading data..")
        searchPath = iq.text(message="Enter a search path directory of your file")
        fileName = iq.text(message="Enter the file name")
        file = findFile(fileName, searchPath)
        data = genfromtxt(file, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
        for i in data:
            strD = numpy.str(i[0])[1:].replace('\'', '')
            csvDate = datetime.strptime(strD, '%Y-%m-%d')
            # print(type(strD))
            stmt = db.text("INSERT INTO transaction_data (transaction_date, debit_amount, credit_amount, description_1, description_2, category_id, account_id) " +
                        "VALUES (:date, :debit, :credit, :d1, :d2, :catId, :accId)")
            stmt = stmt.bindparams(date=csvDate, debit=i[1], credit=i[2], d1=i[3], d2=i[4], catId=i[5], accId=i[6])
            db.session.execute(stmt)
            print(i)
        db.session.commit()
        print('Upload Success!')
    except:
        db.session.rollback()
        print('Upload Failed! Please check your filename, directory or ur data formating in the excel')
    return
    

def findFile(fileName, searchPath):
    for root, dirs, files in os.walk(searchPath):
        if fileName in files:
            return os.path.join(root, fileName)



# uploadData('uploadT.csv', 'C:\\')
# uploadData('uploadT.csv', 'C:\\Users\\sheng\\OneDrive - Singapore Institute Of Technology\\Desktop\\SE - Y2_TRI_1\\ICT 2103')