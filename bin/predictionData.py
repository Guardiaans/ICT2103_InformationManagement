from sqlalchemy.engine.interfaces import CreateEnginePlugin
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import psycopg2
import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import *
from sqlalchemy.sql import select
from datetime import datetime, timedelta

def predictData(userEmail):

    N_DAYS_AGO = 90

    today = datetime.now()    
    n_days_ago = today - timedelta(days=N_DAYS_AGO)
    print("Today's date: ", today.date())
    print("That day: ", n_days_ago.date())
    
    stmt = text("SELECT SUM(transaction_data.credit_amount)/3 AS prediction " + \
    "FROM transaction_data " + \
    "WHERE transaction_data.transaction_date <= :todayTime " + \
    "AND transaction_data.transaction_date >= :n_days_agoTime " + \
    "AND transaction_data.account_id = (SELECT user_detail.account_id FROM user_detail WHERE user_detail.email = :mainUser)")

    stmt = stmt.columns(transaction.c.credit_amount)
    stmt = stmt.bindparams(todayTime = today, n_days_agoTime = n_days_ago, mainUser = userEmail)
    results = session.query(transaction.c.credit_amount).from_statement(stmt).all()
    for i in results:
        print("Your current prediction spending for this month is: ", (str(i.credit_amount)))


# Using SQLAlchemy reflection example
engine = create_engine('postgresql+psycopg2://bfcyvcjpoysvfm:2d577da4f1484cea46199f86a766e69fc14c6323e655828e032e2e1cdc8d5ed6@ec2-34-200-161-87.compute-1.amazonaws.com:5432/dcr1h5psuc7lvu')
metaData = MetaData(engine)
category = Table('category', metaData, autoload=True)
transaction = Table('transaction_data', metaData, autoload=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()

user = 'aym@gmail.com'
predictData(user)