import sqlalchemy
import inquirer as iq
from sqlalchemy.engine.interfaces import CreateEnginePlugin
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import *
from sqlalchemy.sql import select
from components.dbconnection import session, category, user, transaction

#### INSERTING CATEGORY FUCNTION ####

def insertCat(u_email):
    uEmail = u_email
    categoryInsert = iq.text(message="Enter the new category name")
    # select statement to check for category name
    stmt1 = text("SELECT category.category_name " +
                 "FROM category " +
                 "WHERE category.category_name=:whichCategory AND " +
                 "category.account_id = (SELECT user_detail.account_id FROM user_detail WHERE user_detail.email=:userEmail)")
    stmt1 = stmt1.columns(category.c.category_name)
    stmt1 = stmt1.bindparams(whichCategory=categoryInsert, userEmail=uEmail)
    results = session.query(
        category.c.category_name).from_statement(stmt1).all()

    # getting user ID
    stmt2 = text(
        "SELECT user_detail.account_id FROM user_detail WHERE user_detail.email=:userEmail")
    stmt2 = stmt2.columns(user.c.account_id)
    stmt2 = stmt2.bindparams(userEmail=uEmail)
    results2 = session.query(user.c.account_id).from_statement(stmt2).all()
    for i in results2:
        uID = (str(i.account_id))

    # if category name exist --> then do something, else --> do something
    if results:
        # do something if there is data
        print("Category already exists")
    else:
        stmt3 = text(
            "INSERT INTO category (category_name, account_id) VALUES (:categoryName, :userID)")
        stmt3 = stmt3.bindparams(categoryName=categoryInsert, userID=uID)
        session.execute(stmt3)
        session.commit()
        print("Category successfully added")

    menuoption = iq.list_input(f"Select an option",
                              choices=['Back',
                              ])
    return menuoption

#### END INSERTING CATEGORY FUCNTION ####

#### START INSERT TRANSACTION FUNCTIONS ####

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
    insertDesc2 = input("Please enter remarks if any: ")
    insertDate = input("Please enter date(yyyy-mm-dd): ")

    stmt4 = text("INSERT INTO transaction_data (transaction_date, debit_amount, credit_amount, description_1, description_2, category_id, account_id) " + \
    "VALUES (:tDate, :tDebit, :tCredit, :tDesc1, :tDesc2, :tCatID, :tAccID)")
    stmt4 = stmt4.bindparams(tDate = insertDate, tDebit = insertDebit, tCredit = insertCredit, tDesc1 = insertDesc1, tDesc2 = insertDesc2, tCatID = catID, tAccID = user_Id)
    session.execute(stmt4)
    session.commit()
    print("Transaction successfully added")

def checkCatAndName(u_email,u_id):

    uEmail = u_email
    insertCategory = input("Please enter category name: ")

    #getting user ID
    # stmt = text("SELECT user_detail.account_id FROM user_detail WHERE user_detail.email=:userEmail")
    # stmt = stmt.columns(user.c.account_id)
    # stmt = stmt.bindparams(userEmail = uEmail)
    # results = session.query(user.c.account_id).from_statement(stmt).all()
    # for i in results:
    #     uID = (str(i.account_id))

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
        insertTransaction(insertCategory, u_id)
    else:
        #do something if there is no data, in this case, will help user to add the category
        stmt3 = text("INSERT INTO category (category_name, account_id) VALUES (:categoryName, :userID)")
        stmt3 = stmt3.bindparams(categoryName = insertCategory, userID = u_id)
        session.execute(stmt3)
        session.commit()
        print("Category successfully added, proceeding to add transaction")
        insertTransaction(insertCategory, u_id)

#### END INSERT TRANSACTION FUNCTIONS ####

#### START DELETE TRANSACTION FUNCTIONS ####

def deleteTransaction(u_email):
    uEmail = u_email
    print("viewing transaction table")
    year = iq.text(message="Enter a year <2021>")
    month = iq.text(message="Enter a month <10>")

    print("Transactions for user: ", u_email)
    
    stmt7 = text("SELECT t.transaction_id, t.transaction_date, t.debit_amount, t.credit_amount, t.description_1, t.description_2, c.category_name " + \
    "FROM transaction_data AS t " + \
    "JOIN category AS c " + \
    "ON t.category_id = c.category_id " + \
    "WHERE t.account_id = (SELECT user_detail.account_id FROM user_detail WHERE user_detail.email = :userEmail) " + \
    "AND CAST(t.transaction_date as character varying(50)) LIKE ':year-%:month-%' " + \
    "Order By t.transaction_id ASC")
    stmt7 = stmt7.columns(transaction.c.transaction_id, transaction.c.transaction_date, transaction.c.debit_amount, transaction.c.credit_amount, transaction.c.description_1, transaction.c.description_2, category.c.category_name)
    stmt7 = stmt7.bindparams(userEmail = u_email, year = int(year), month = int(month))

    results3 = session.query(transaction.c.transaction_id, transaction.c.transaction_date, transaction.c.debit_amount, transaction.c.credit_amount, transaction.c.description_1, transaction.c.description_2, category.c.category_name).from_statement(stmt7).all()
    print("{:<5}{:<13}{:<12}{:<12}{:<40}{:<40}{:<5}".format("id","date","debit", "credit", "description_1","description_2", "category"))
    print("_________________________________________________________________________________________________________________________________________")
    for i in results3:
        print("{:<5}{:<13}{:<12}{:<12}{:<40}{:<40}{:<5}".format(str(i.transaction_id), str(i.transaction_date), str(i.debit_amount), str(i.credit_amount), str(i.description_1), str(i.description_2), str(i.category_name)))

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

#### END DELETE TRANSACTION FUNCTIONS ####
