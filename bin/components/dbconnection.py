import psycopg2
import sqlalchemy
from sqlalchemy import Column, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy import *
from sqlalchemy.sql import select
from sqlalchemy.sql.elements import Null
from sqlalchemy.sql.sqltypes import NullType


# Using SQLAlchemy reflection example
try:
    engine = create_engine(
        'postgresql+psycopg2://bfcyvcjpoysvfm:2d577da4f1484cea46199f86a766e69fc14c6323e655828e032e2e1cdc8d5ed6@ec2-34-200-161-87.compute-1.amazonaws.com:5432/dcr1h5psuc7lvu')
    print("Connected to DB!")
except:
    print("Error connecting to DB")

metaData = MetaData(engine)
user = Table('user_detail', metaData, autoload=True)
category = Table('category', metaData, autoload=True)
transaction = Table('transaction_data', metaData, autoload=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()

### GC's TEST CASE STATEMENTS ###

#verified_user = getUserProfile('kgc@gmail.com')
# print(verified_user.name)
#authenticate('Kwang Guan Cong', 'anyhow')
# getUserID('kgc@gmail.com')
#print(session.query(exists(user.c.name).where(user.c.name == 'notinDB')).scalar())
#register("Spongebob", 1234, "krustyKrab", "spongebob@gmail.com")
