import time
import pymongo
from pymongo import MongoClient
from typing import Tuple
import os
import hashlib
import hmac
import datetime 

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
