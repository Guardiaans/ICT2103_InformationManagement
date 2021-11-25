import time
import pymongo
from pymongo import MongoClient
import inquirer as iq
from bson.objectid import ObjectId
from decimal import *
from sqlalchemy.sql.functions import user
import datetime
import pprint


class dateInput():
    def __init__(self,yr , mnth) -> None:
        self.year = yr
        self.month = mnth
def getDateInput():
    year = iq.text(message="Enter a year (e.g. 2021)")
    month = iq.text(message="Enter a month (e.g. 10)")
    d = dateInput(year, month)
    return d

start = time.perf_counter()

# Using SQLAlchemy reflection example
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
    

def deleteTransaction():
    u_email = "bo@gmail.com"
    date = getDateInput()

    result = db.transactions.find({"email":u_email, "$expr": {"$eq":[{"$year": "$transaction_date"}, int(date.year)], "$eq": [{ "$month": "$transaction_date" }, int(date.month)] }}).sort("transaction_date",1)
    transactionDisplay = []
    for x in result:    
        transactionDisplay.append(x)

    print("{:<30}{:<15}{:<12}{:<12}{:<50}{:<50}{:<5}".format("ID","date","debit", "credit", "description_1","description_2", "category"))
    print(200*"_")
    for i in transactionDisplay:
        print("{:<30}{:<15}{:<12}{:<12}{:<50}{:<50}{:<5}".format(str(i["_id"]), str(i["transaction_date"]).replace("00:00:00",""), str(i["debit_amount"]), str(i["credit_amount"]),str(i["description_1"]), str(i["description_2"]), str(i["category"])))

    delete = input("Please enter the transaction ID which you want to delete: ")

    try:
        result2 = db.transactions.find({"email" : u_email, "_id" : ObjectId(delete)})
        
        if result2:
            print("Transaction exist")
            result1 = db.transactions.find_one_and_delete({ "_id" : ObjectId(delete), "email" : u_email}, projection={"_Id" : 1, "transaction_date" : 1, "debit_amount" : 1, "credit_amount" : 1, "description_1" : 1, "description_2" : 1, "category" : 1})
            pprint.pprint(result1)
            print("Transaction successfully deleted")
        else:
            print("Transaction does not exist")
    except:
        print("Transaction does not exist")

deleteTransaction()


    
### GC's TEST CASE STATEMENTS ###

#verified_user = getUserProfile('kgc@gmail.com')
# print(verified_user.name)
#authenticate('Kwang Guan Cong', 'anyhow')
# getUserID('kgc@gmail.com')
#print(session.query(exists(user.c.name).where(user.c.name == 'notinDB')).scalar())
#register("Spongebob", 1234, "krustyKrab", "spongebob@gmail.com")

