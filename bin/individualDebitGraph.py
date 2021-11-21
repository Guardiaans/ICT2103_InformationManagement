import matplotlib.pyplot as plt
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import psycopg2
import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import *
from sqlalchemy.sql import select

# Using SQLAlchemy reflection example
engine = create_engine('postgresql+psycopg2://bfcyvcjpoysvfm:2d577da4f1484cea46199f86a766e69fc14c6323e655828e032e2e1cdc8d5ed6@ec2-34-200-161-87.compute-1.amazonaws.com:5432/dcr1h5psuc7lvu')
metaData = MetaData(engine)
user = Table('user_detail', metaData, autoload=True)
category = Table('category', metaData, autoload=True)
transaction = Table('transaction_data', metaData, autoload=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()
emailReturned = "csy@gmail.com"
stmt = text("SELECT sum(t.debit_amount) as debit, sum(t.credit_amount) as credit " + 
            "FROM transaction_data t, user_detail u WHERE t.account_id=u.account_id " +  
            "AND t.transaction_date BETWEEN '2021-09-01' AND '2021-09-30' AND u.email=:email")
stmt = stmt.columns(transaction.c.debit_amount, transaction.c.credit_amount)
stmt = stmt.bindparams(email=emailReturned)
results = session.query(transaction.c.debit_amount, transaction.c.credit_amount).from_statement(stmt).all()
print(results)


labels = ["Income", "Expenses"]
sizes = [results[0].debit_amount[1:].replace("," ,""), results[0].credit_amount[1:].replace("," ,"")]

# Pie chart, where the slices will be ordered and plotted counter-clockwise:

# explode = (0, 0.1, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()