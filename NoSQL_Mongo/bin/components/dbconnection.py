import time
from inquirer.render.console.base import BaseConsoleRender
import pymongo
from pymongo import MongoClient
import datetime as dt

## MONGO CLIENT DATA CONNECTION ##
try:
    print(f"\t\t{'||' : <10} {'Establishing connection to Database...' : ^10} {'||' : >10}")
    cluster = MongoClient("mongodb+srv://shengyu98:PiJF4JXI@cluster0.zwj7f.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["expenseTracker"]
    transactions = db["transactions"]
    prediction = db["prediction"]
    budget = db["budget"]
    user_data = db["user_detail"]
    print(f"\t\t{'||' : <10} {'Database connected!' : ^10} {'||' : >29}")
    time.sleep(1)
    print(f"\t\t{'||' : <10} {'Redirecting......  ' : ^10} {'||' : >29}")
    time.sleep(1)
except:
    print("Error connecting to DB")


### LIST FUNCTION FOUND IN UTILS
def getList(query,fieldname):
    myquery = query
    return_obj = transactions.find(myquery)
    listname = [item[fieldname] for item in return_obj]
    return listname

### TABLE QUERY
mydate = dt.datetime(2021,10,10)
mydate2 = dt.datetime(2021,5,1)
myquery = {'email' : 'kgc@gmail.com', 'transaction_date' : {'$lt':mydate, '$gt':mydate2}}

### GENERATE ALL THE LIST FOR THE TABLE COLUMN
acc_id = getList(myquery,'account_id')
balance = getList(myquery,'balance')
bank_name = getList(myquery,'bank_name')
category = getList(myquery,'category')
credit_amount = getList(myquery,'credit_amount')
debit_amount = getList(myquery,'debit_amount')
description_1 = getList(myquery,'description_1')
description_2 = getList(myquery,'description_2')

### PRINTING TABLE
z = zip(acc_id, balance,bank_name,category,credit_amount,debit_amount,description_1,description_2)
alist = list(z)
print("{:<15}{:<19}{:<15}{:<15}{:<11}{:<11}{}".format('ACCOUNT_ID', 'ACCOUNT_BALANCE', 'BANK_NAME', 'CATEGORY', 'CREDIT', 'DEBIT', 'DESCRIPTION'))
print("---------------------------------------------------------------------------------------------------------------------------------------------")
for a_id , bal, bk_n, ct, cr_a, db_a, dsc1, dsc2 in alist:
    print("{:<14} {:<18} {:<14} {:<14} {:<10} {:<10} {:<35} {} ".format(a_id, bal, bk_n, ct, cr_a, db_a, dsc1, dsc2))





