from sqlalchemy.engine.interfaces import CreateEnginePlugin
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import psycopg2
import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import *
from sqlalchemy.sql import select

uEmail = 'aym@gmail.com'
cEmail = input("Enter the other party's email: ")

# Using SQLAlchemy reflection example
engine = create_engine('postgresql+psycopg2://bfcyvcjpoysvfm:2d577da4f1484cea46199f86a766e69fc14c6323e655828e032e2e1cdc8d5ed6@ec2-34-200-161-87.compute-1.amazonaws.com:5432/dcr1h5psuc7lvu')
metaData = MetaData(engine)
category = Table('category', metaData, autoload=True)
transaction = Table('transaction_data', metaData, autoload=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()

stmt = text("SELECT category.category_name, SUM(transaction_data.debit_amount) " + \
"FROM transaction_data " +\
"JOIN category " + \
"ON transaction_data.category_id = category.category_id " + \
"JOIN user_detail " + \
"ON transaction_data.account_id = user_detail.account_id " + \
"WHERE user_detail.email=:userEmail " + \
"GROUP BY category.category_name " + \
"HAVING SUM(transaction_data.debit_amount) > '0' " + \
"ORDER BY category.category_name ASC")
stmt = stmt.columns(category.c.category_name, transaction.c.debit_amount)
stmt = stmt.bindparams(userEmail = uEmail)
results = session.query(category.c.category_name, transaction.c.debit_amount).from_statement(stmt).all()
print("User: ", uEmail)
print("{:<20}{:<12}".format("Category", "Total Amount"))
print("______________________________________________________________________")
for i in results:
    print("{:<20}{:<12}".format(str(i.category_name), str(i.debit_amount)))
print("\n")



stmt2 = text("SELECT category.category_name, SUM(transaction_data.debit_amount) " + \
"FROM transaction_data " +\
"JOIN category " + \
"ON transaction_data.category_id = category.category_id " + \
"JOIN user_detail " + \
"ON transaction_data.account_id = user_detail.account_id " + \
"WHERE user_detail.email=:compareEmail " + \
"GROUP BY category.category_name " + \
"HAVING SUM(transaction_data.debit_amount) > '0' " + \
"ORDER BY category.category_name ASC")
stmt2 = stmt2.columns(category.c.category_name, transaction.c.debit_amount)
stmt2 = stmt2.bindparams(compareEmail = cEmail)
results = session.query(category.c.category_name, transaction.c.debit_amount).from_statement(stmt2).all()
print("Comparison: ", cEmail)
print("{:<20}{:<12}".format("Category", "Total Amount"))
print("______________________________________________________________________")
for i in results:
    print("{:<20}{:<12}".format(str(i.category_name), str(i.debit_amount)))