import time
import pymongo
from pymongo import MongoClient

start = time.perf_counter()

# Using SQLAlchemy reflection example
try:
    print(f"\t\t{'||' : <10} {'Establishing connection to Database...' : ^10} {'||' : >10}")
    cluster = MongoClient("mongodb+srv://shengyu98:PiJF4JXI@cluster0.zwj7f.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["expenseTracker"]
    collection = db["expenseTracker"]
    print(f"\t\t{'||' : <10} {'Database connected!' : ^10} {'||' : >29}")
    time.sleep(1)
    print(f"\t\t{'||' : <10} {'Redirecting......  ' : ^10} {'||' : >29}")
    time.sleep(2)
    
except:
    print("Error connecting to DB")


### GC's TEST CASE STATEMENTS ###

#verified_user = getUserProfile('kgc@gmail.com')
# print(verified_user.name)
#authenticate('Kwang Guan Cong', 'anyhow')
# getUserID('kgc@gmail.com')
#print(session.query(exists(user.c.name).where(user.c.name == 'notinDB')).scalar())
#register("Spongebob", 1234, "krustyKrab", "spongebob@gmail.com")

