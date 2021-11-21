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
stmt = text("SELECT sum(t.credit_amount) as Expense, c.category_name FROM transaction_data t, category c, user_detail u " + \
        "WHERE t.category_id=c.category_id AND u.account_id=t.account_id AND t.transaction_date BETWEEN '2021-10-01' AND '2021-10-31' AND u.email=:email "+ \
        "GROUP BY c.category_name")
stmt = stmt.columns(transaction.c.credit_amount, category.c.category_name)
stmt = stmt.bindparams(email=emailReturned)
results = session.query(transaction.c.credit_amount, category.c.category_name).from_statement(stmt).all()
# print(results)
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = []
sizes = []
cleanLabels = []
cleanSizes = []
for i in results:
        # print(type(i.credit_amount))
        # print(i.credit_amount)
        sizes.append(i.credit_amount[1:].replace("," ,""))
        labels.append(i.category_name)

# print(labels)

for i in range(0,len(sizes)):
        if (sizes[i] != '0.00'):
                cleanLabels.append(labels[i])
                cleanSizes.append(sizes[i])
print(cleanLabels)

# explode = (0, 0.1, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(cleanSizes, labels=cleanLabels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()