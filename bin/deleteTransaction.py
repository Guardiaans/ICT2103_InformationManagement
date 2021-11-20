from sqlalchemy.engine.interfaces import CreateEnginePlugin
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import *
from sqlalchemy.sql import select

#from bin.deleteCategory import deleteCat <-- to import other functions

def deleteTransaction(email):
    uEmail = email
    tID = input("Please enter the transaction ID that you wish to delete: ")

    stmt = text("SELECT transaction_data.transaction_id " +
            "FROM transaction_data " +
            "WHERE transaction_data.transaction_id=:whichTransaction AND " +
            "transaction_data.account_id = (SELECT user_detail.account_id FROM user_detail WHERE user_detail.email=:userEmail)") 
    stmt = stmt.columns(transaction.c.transaction_id)
    stmt = stmt.bindparams(whichTransaction = tID, userEmail = uEmail)   
    results = session.query(transaction.c.transaction_id).from_statement(stmt).all()

    if results:
        stmt1 = text("DELETE FROM transaction_data " + \
        "WHERE transaction_data.transaction_id=:transaction_ID " + \
        "AND transaction_data.account_id = (SELECT user_detail.account_id FROM user_detail WHERE user_detail.email=:userEmail)")
        stmt1 = stmt1.bindparams(transaction_ID = tID, userEmail = uEmail)
        session.execute(stmt1)
        session.commit()
        print("Transaction successfully deleted")
    else: 
        print("Transaction does not exist")




# Using SQLAlchemy reflection example
engine = create_engine(
    'postgresql+psycopg2://bfcyvcjpoysvfm:2d577da4f1484cea46199f86a766e69fc14c6323e655828e032e2e1cdc8d5ed6@ec2-34-200-161-87.compute-1.amazonaws.com:5432/dcr1h5psuc7lvu')
metaData = MetaData(engine)
category = Table('category', metaData, autoload=True)
transaction = Table('transaction_data', metaData, autoload=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()

userEmail = 'bo@gmail.com'
deleteTransaction(userEmail)