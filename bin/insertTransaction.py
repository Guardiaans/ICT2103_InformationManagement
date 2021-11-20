from sqlalchemy.engine.interfaces import CreateEnginePlugin
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import *
from sqlalchemy.sql import select
from sqlalchemy.sql.functions import user

def insertTransaction(catName, user_Id):
    print("this is the insert transaction function")
    #getting category ID
    stmt2 = text("SELECT category.category_id FROM category WHERE category.category_name=:categoryName AND category.account_id=:userID")
    stmt2 = stmt2.columns(category.c.category_id)
    stmt2 = stmt2.bindparams(categoryName = catName, userID = user_Id)
    results2 = session.query(category.c.category_id).from_statement(stmt2).all()
    for i in results2:
        catID = (str(i.category_id))

    insertDebit = input("Please enter debit amount: ")
    insertCredit = input("Please enter credit amount: ")
    insertDesc1 = input("Please enter description if any: ")
    insertDesc2 = input("Please enter description if any: ")
    insertDate = input("Please enter date(yyyy-mm-dd): ")

    stmt4 = text("INSERT INTO transaction_data (transaction_date, debit_amount, credit_amount, description_1, description_2, category_id, account_id) " + \
    "VALUES (:tDate, :tDebit, :tCredit, :tDesc1, :tDesc2, :tCatID, :tAccID)")
    stmt4 = stmt4.bindparams(tDate = insertDate, tDebit = insertDebit, tCredit = insertCredit, tDesc1 = insertDesc1, tDesc2 = insertDesc2, tCatID = catID, tAccID = user_Id)
    session.execute(stmt4)
    session.commit()
    print("Transaction successfully added")


def checkCatAndName(email):
    uEmail = email
    insertCategory = input("Please enter category name: ")

    #getting user ID
    stmt = text("SELECT user_detail.account_id FROM user_detail WHERE user_detail.email=:userEmail")
    stmt = stmt.columns(userDetail.c.account_id)
    stmt = stmt.bindparams(userEmail = uEmail)
    results = session.query(userDetail.c.account_id).from_statement(stmt).all()
    for i in results:
        uID = (str(i.account_id))

    # select statement to check for category name
    stmt1 = text("SELECT category.category_name " +
                "FROM category " +
                "WHERE category.category_name=:whichCategory AND " +
                "category.account_id = (SELECT user_detail.account_id FROM user_detail WHERE user_detail.email=:userEmail)")
    stmt1 = stmt1.columns(category.c.category_name)
    stmt1 = stmt1.bindparams(whichCategory=insertCategory, userEmail=uEmail)
    results = session.query(category.c.category_name).from_statement(stmt1).all()

    #if category name exist --> then do something, else --> do something
    if results:
        # do something if there is data, in this case, if the category exists, continue with the inserting the transaction
        print("Category exists, proceeding to add transaction")
        insertTransaction(insertCategory, uID)
    else:
        #do something if there is no data, in this case, will help user to add the category
        stmt3 = text("INSERT INTO category (category_name, account_id) VALUES (:categoryName, :userID)")
        stmt3 = stmt3.bindparams(categoryName = insertCategory, userID = uID)
        session.execute(stmt3)
        session.commit()
        print("Category successfully added, proceeding to add transaction")
        insertTransaction(insertCategory, uID)

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
checkCatAndName(userEmail)