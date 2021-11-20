from sqlalchemy.engine.interfaces import CreateEnginePlugin
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import *
from sqlalchemy.sql import select

def insertCat(email):
    uEmail = email
    categoryInsert = input("Enter the new category name: ")
    # select statement to check for category name
    stmt1 = text("SELECT category.category_name " +
                "FROM category " +
                "WHERE category.category_name=:whichCategory AND " +
                "category.account_id = (SELECT user_detail.account_id FROM user_detail WHERE user_detail.email=:userEmail)")
    stmt1 = stmt1.columns(category.c.category_name)
    stmt1 = stmt1.bindparams(whichCategory=categoryInsert, userEmail=uEmail)
    results = session.query(category.c.category_name).from_statement(stmt1).all()

    #getting user ID
    stmt2 = text("SELECT user_detail.account_id FROM user_detail WHERE user_detail.email=:userEmail")
    stmt2 = stmt2.columns(userDetail.c.account_id)
    stmt2 = stmt2.bindparams(userEmail = uEmail)
    results2 = session.query(userDetail.c.account_id).from_statement(stmt2).all()
    for i in results2:
        uID = (str(i.account_id))

    #if category name exist --> then do something, else --> do something
    if results:
        # do something if there is data
        print("Category already exists")
    else:
        stmt3 = text("INSERT INTO category (category_name, account_id) VALUES (:categoryName, :userID)")
        stmt3 = stmt3.bindparams(categoryName = categoryInsert, userID = uID)
        session.execute(stmt3)
        session.commit()
        print("Category successfully added")



# Using SQLAlchemy reflection example
engine = create_engine(
    'postgresql+psycopg2://bfcyvcjpoysvfm:2d577da4f1484cea46199f86a766e69fc14c6323e655828e032e2e1cdc8d5ed6@ec2-34-200-161-87.compute-1.amazonaws.com:5432/dcr1h5psuc7lvu')
metaData = MetaData(engine)
category = Table('category', metaData, autoload=True)
transaction = Table('transaction_data', metaData, autoload=True)
userDetail = Table('user_detail', metaData, autoload=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()

userEmail = 'bo@gmail.com'
insertCat(userEmail)

# # select statement to check for category name
# stmt1 = text("SELECT category.category_name " +
#              "FROM category " +
#              "WHERE category.category_name=:whichCategory AND " +
#              "category.account_id = (SELECT user_detail.account_id FROM user_detail WHERE user_detail.email=:userEmail)")
# stmt1 = stmt1.columns(category.c.category_name)
# stmt1 = stmt1.bindparams(whichCategory=categoryInsert, userEmail=uEmail)
# results = session.query(category.c.category_name).from_statement(stmt1).all()

# #getting user ID
# stmt2 = text("SELECT user_detail.account_id FROM user_detail WHERE user_detail.email=:userEmail")
# stmt2 = stmt2.columns(userDetail.c.account_id)
# stmt2 = stmt2.bindparams(userEmail = uEmail)
# results2 = session.query(userDetail.c.account_id).from_statement(stmt2).all()
# for i in results2:
#     uID = (str(i.account_id))

# #if category name exist --> then do something, else --> do something
# if results:
#     # do something if there is data
#     print("Category already exists")
# else:
#     stmt3 = text("INSERT INTO category (category_name, account_id) VALUES (:categoryName, :userID)")
#     stmt3 = stmt3.bindparams(categoryName = categoryInsert, userID = uID)
#     session.execute(stmt3)
#     session.commit()
#     print("Category successfully added")
    