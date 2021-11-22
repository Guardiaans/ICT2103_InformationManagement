import psycopg2
import sqlalchemy
#import components.utils as ut
from sqlalchemy import Column, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy import *
from sqlalchemy.sql import select
from sqlalchemy.sql.elements import Null
from sqlalchemy.sql.sqltypes import NullType
import time
import concurrent.futures

start = time.perf_counter()

# Using SQLAlchemy reflection example
try:
    print(f"\t\t{'||' : <10} {'Establishing connection to Database...' : ^10} {'||' : >10}")
    engine = create_engine(
        'postgresql+psycopg2://bfcyvcjpoysvfm:2d577da4f1484cea46199f86a766e69fc14c6323e655828e032e2e1cdc8d5ed6@ec2-34-200-161-87.compute-1.amazonaws.com:5432/dcr1h5psuc7lvu')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        metaData = MetaData(engine)
        user = Table('user_detail', metaData, autoload=True)
        category = Table('category', metaData, autoload=True)
        transaction = Table('transaction_data', metaData, autoload=True)
        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        #### Testing threading to connect faster ####
        # t1 = executor.submit(MetaData, engine)
        # metaData = t1.result()
        # t2 = executor.submit(Table, 'user_detail', metaData, autoload=True)
        # user = t2.result()
        # t3 = executor.submit(Table, 'category', metaData, autoload=True)
        # category = t3.result()
        # t4 = executor.submit(Table, 'transaction_data', metaData, autoload=True)
        # transaction = t4.result()
        # t5 = executor.submit(sessionmaker, bind=engine)
        # DBSession = t5.result()
        # session = DBSession()

    #print("Connected to DB!")
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

