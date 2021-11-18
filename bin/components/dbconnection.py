from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import psycopg2
import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import *
from sqlalchemy.sql import select


# Using SQLAlchemy reflection example
try:
    engine = create_engine('postgresql+psycopg2://bfcyvcjpoysvfm:2d577da4f1484cea46199f86a766e69fc14c6323e655828e032e2e1cdc8d5ed6@ec2-34-200-161-87.compute-1.amazonaws.com:5432/dcr1h5psuc7lvu')
    print("Connected to DB!")
except:
    print("Error connecting to DB")
    
metaData = MetaData(engine)
user = Table('user_detail', metaData, autoload=True)
category = Table('category', metaData, autoload=True)
transaction = Table('transaction_data', metaData, autoload=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()



#passing query statement in variable
# stmt = text('''
#     SELECT 
#     t.transaction_id, 
#     t.transaction_date, 
#     t.debit_amount, 
#     t.credit_amount, 
#     t.description_1, 
#     t.description_2, 
#     c.category_name 
#     FROM 
#     transaction_data t, 
#     user_detail u, 
#     category c
#     WHERE 
#     t.account_id = u.account_id AND c.category_id = t.category_id AND u.email='csy@gmail.com' 
#     ''')

# stmt = stmt.columns(transaction.c.transaction_id, transaction.c.transaction_date, transaction.c.debit_amount, transaction.c.credit_amount, transaction.c.description_1, transaction.c.description_2, category.c.category_name)

# results = session.query(transaction.c.transaction_id, transaction.c.transaction_date, transaction.c.debit_amount, transaction.c.credit_amount, transaction.c.description_1, transaction.c.description_2, category.c.category_name).from_statement(stmt).all()

# #printing the table
# print("{:<5}{:<13}{:<12}{:<12}{:<40}{:<40}{:<5}".format("id","date","debit", "credit", "description_1","description_2", "category"))
# print("_________________________________________________________________________________________________________________________________________")
# for i in results:
#     print("{:<5}{:<13}{:<12}{:<12}{:<40}{:<40}{:<5}".format(str(i.transaction_id), str(i.transaction_date), str(i.debit_amount), str(i.credit_amount), str(i.description_1), str(i.description_2), str(i.category_name)))


#TODO:
# implement getProfile - accountID Name, Date Registered, Bank used, bank balance, email

class UserProfile:
    def __init__(self, email):
        self.id
        self.name
        self.registered
        self.bank
        self.balance
        self.email = email

def authenticate(email, password):

    try:
        email = session.query(exists(user.c.email).where(user.c.email == email)).scalar()
        pw = session.query(exists(user.c.password).where(user.c.password == password)).scalar()

        if email == True and pw == True:
            return True
        else:
            return False
        #print(f"is user in database?: {usr}")
        #rint(f"is password in database?: {pw}")
    except:
        print("Unable to authenticate!")
    return False

def getUserID(email):

    stmt = text(f"SELECT ud.account_id, ud.name FROM user_detail ud WHERE ud.email = '{email}' ")
    data = stmt.columns(user.c.account_id, user.c.name)
    result = session.query(user.c.account_id, user.c.name).from_statement(data).all()

    account_id = [item[0] for item in result]
    name_list = [item[1] for item in result]
    
    userID = account_id[0]
    #name = name_list[0]
    return userID, name


#authenticate('Kwang Guan Cong', 'anyhow')
#getUserID('kgc@gmail.com')

#print(session.query(exists(user.c.name).where(user.c.name == 'notinDB')).scalar())

