import time
from inquirer.render.console.base import BaseConsoleRender
import pymongo
from pymongo import MongoClient
from typing import Tuple
import os
import hashlib
import hmac
import datetime as dt
from pprint import pprint

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

mydate = dt.datetime(2021,10,10)
mydate2 = dt.datetime(2021,10,1)

_id, account_id, balance, bank_name, category, category_created_by, credit_amount, date_registered, debit_amount,description_1,description_2, email, name, password, transaction_date = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[]

myquery = {'email' : 'kgc@gmail.com', 'transaction_date' : {'$lt':mydate, '$gt':mydate2}}

return_obj = transactions.find(myquery)
acc_id = [item['account_id'] for item in return_obj]
return_obj = transactions.find(myquery)
bal = [item['balance'] for item in return_obj]
return_obj = transactions.find(myquery)
bk_name = [item['bank_name'] for item in return_obj]
return_obj = transactions.find(myquery)
cat = [item['category'] for item in return_obj]
return_obj = transactions.find(myquery)
cr_amt = [item['credit_amount'] for item in return_obj]
return_obj = transactions.find(myquery)
db_amt = [item['debit_amount'] for item in return_obj]
return_obj = transactions.find(myquery)
dsc1 = [item['description_1'] for item in return_obj]
return_obj = transactions.find(myquery)
dsc2 = [item['description_2'] for item in return_obj]

#print(acc_id)

# for dicts in return_obj:
#     for key,val in dicts.items():
#         print(key, val)
        # _id.append(val)
        # account_id.append(val)
        # balance.append(val)
        # bank_name.append(val)
        # category.append(val)
        # category_created_by.append(val)
        # credit_amount.append(val)
        # date_registered.append(val)
        # debit_amount.append(val)
        # description_1.append(val)
        # description_2.append(val)
        # email.append(val)
        # name.append(val)
        # password.append(val)
        # transaction_date.append(val)



# total_debit = sum(debit_amount)
# print(total_debit)
