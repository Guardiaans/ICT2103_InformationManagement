from sqlalchemy.engine.interfaces import CreateEnginePlugin
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import *
from sqlalchemy.sql import select

def deleteCat(email):
    uEmail = email
    categoryDelete = input("Enter the category you wish to delete: ")

    stmt1 = text("SELECT category.category_name " +
                "FROM category " +
                "WHERE category.category_name=:whichCategory AND " +
                "category.account_id = (SELECT user_detail.account_id FROM user_detail WHERE user_detail.email=:userEmail)")
    stmt1 = stmt1.columns(category.c.category_name)
    stmt1 = stmt1.bindparams(whichCategory=categoryDelete, userEmail=uEmail)
    results = session.query(category.c.category_name).from_statement(stmt1).all()

    if results:
        # do something if there is data
        stmt = text("DELETE FROM category " + \
        "WHERE category.category_name=:whichCategory " + \
        "AND category.account_id=(SELECT user_detail.account_id FROM user_detail WHERE user_detail.email=:userEmail)")
        stmt = stmt.bindparams(whichCategory = categoryDelete, userEmail = uEmail)
        session.execute(stmt)
        session.commit()
        print("Category successfully deleted")
    else:
        print("Category does not exist")


# Using SQLAlchemy reflection example
engine = create_engine(
    'postgresql+psycopg2://bfcyvcjpoysvfm:2d577da4f1484cea46199f86a766e69fc14c6323e655828e032e2e1cdc8d5ed6@ec2-34-200-161-87.compute-1.amazonaws.com:5432/dcr1h5psuc7lvu')
metaData = MetaData(engine)
category = Table('category', metaData, autoload=True)
transaction = Table('transaction_data', metaData, autoload=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()

userEmail = 'aym@gmail.com'
deleteCat(userEmail)



# uEmail = 'aym@gmail.com'
# categoryDelete = input("Enter the category you wish to delete: ")

# stmt1 = text("SELECT category.category_name " +
#              "FROM category " +
#              "WHERE category.category_name=:whichCategory AND " +
#              "category.account_id = (SELECT user_detail.account_id FROM user_detail WHERE user_detail.email=:userEmail)")
# stmt1 = stmt1.columns(category.c.category_name)
# stmt1 = stmt1.bindparams(whichCategory=categoryDelete, userEmail=uEmail)
# results = session.query(category.c.category_name).from_statement(stmt1).all()

# if results:
#     # do something if there is data
#     stmt = text("DELETE FROM category " + \
#     "WHERE category.category_name=:whichCategory " + \
#     "AND category.account_id=(SELECT user_detail.account_id FROM user_detail WHERE user_detail.email=:userEmail)")
#     stmt = stmt.bindparams(whichCategory = categoryDelete, userEmail = uEmail)
#     session.execute(stmt)
#     session.commit()
#     print("Category successfully deleted")
# else:
#     print("Category does not exist")


