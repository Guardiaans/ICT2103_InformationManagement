import sqlalchemy
import inquirer as iq
from sqlalchemy.engine.interfaces import CreateEnginePlugin
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import *
from sqlalchemy.sql import select
from components.dbconnection import session, category, user, transaction
import pprint
from bson.objectid import ObjectId
import datetime


class dateInput():
    def __init__(self,yr , mnth) -> None:
        self.year = yr
        self.month = mnth
def getDateInput():
    year = iq.text(message="Enter a year (e.g. 2021)")
    month = iq.text(message="Enter a month (e.g. 10)")
    d = dateInput(year, month)
    return d

#### INSERTING CATEGORY FUCNTION ####

def insertCat(u_email):
    
    insertName = ""
    insertAccID = ""

    result = db.transactions.find({"email": u_email})

    transactionDisplay = []
    for x in result:    
        transactionDisplay.append(x)

    for i in transactionDisplay:
        insertName = (str(i["name"]))
        insertAccID = (str(i["account_id"]))

    year = input("Enter a year (e.g. 2021): ")
    month = input("Enter a month (e.g. 10): ")
    day = input("Enter the day (e.g. 24): ")
    insertDebit = input("Enter debit amount: ")
    insertCredit = input("Enter credit amount: ")
    insertDesc1 = input("Enter description if any: ")
    insertDesc2 = input("Enter description if any: ")
    insertCategory = input("Enter the category: ")

    try:
        db.transactions.insert_one(
            {
            "transaction_date": datetime.datetime(int(year), int(month), int(day), 0, 0),
            "debit_amount" : int(insertDebit),
            "credit_amount" : int(insertCredit),
            "description_1" : insertDesc1,
            "description_2" : insertDesc2,
            "category" : insertCategory,
            "name" : insertName,
            "email" : u_email,
            "account_id" : insertAccID
            }
        ).inserted_id
        print("Transaction successfully added!")
    except:
        print("Transaction not added!")

    menuoption = iq.list_input(f"Select an option",
                              choices=['Back',
                              ])
    return menuoption

#### END INSERTING CATEGORY FUCNTION ####

#### START DELETING CATEGORY FUCNTION ####

def deleteCat(u_email):
    uEmail = u_email
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

#### END DELETING CATEGORY FUCNTION ####

#### START INSERT TRANSACTION FUNCTIONS ####

def insertTransaction(u_email):
    
    insertName = ""
    insertAccID = ""

    result = db.transactions.find({"email": u_email})

    transactionDisplay = []
    for x in result:    
        transactionDisplay.append(x)

    for i in transactionDisplay:
        insertName = (str(i["name"]))
        insertAccID = (str(i["account_id"]))

    year = input("Enter a year (e.g. 2021): ")
    month = input("Enter a month (e.g. 10): ")
    day = input("Enter the day (e.g. 24): ")
    insertDebit = input("Enter debit amount: ")
    insertCredit = input("Enter credit amount: ")
    insertDesc1 = input("Enter description if any: ")
    insertDesc2 = input("Enter description if any: ")
    insertCategory = input("Enter the category: ")

    try:
        db.transactions.insert_one(
            {
            "transaction_date": datetime.datetime(int(year), int(month), int(day), 0, 0),
            "debit_amount" : int(insertDebit),
            "credit_amount" : int(insertCredit),
            "description_1" : insertDesc1,
            "description_2" : insertDesc2,
            "category" : insertCategory,
            "name" : insertName,
            "email" : u_email,
            "account_id" : insertAccID
            }
        ).inserted_id
        print("Transaction successfully added!")
    except:
        print("Transaction not added!")

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
    date = getDateInput()

    result = db.transactions.find({"email":u_email, "$expr": {"$eq":[{"$year": "$transaction_date"}, int(date.year)], "$eq": [{ "$month": "$transaction_date" }, int(date.month)] }}).sort("transaction_date",1)
    transactionDisplay = []
    for x in result:    
        transactionDisplay.append(x)

    print("{:<30}{:<15}{:<12}{:<12}{:<50}{:<50}{:<5}".format("ID","date","debit", "credit", "description_1","description_2", "category"))
    print(200*"_")
    for i in transactionDisplay:
        print("{:<30}{:<15}{:<12}{:<12}{:<50}{:<50}{:<5}".format(str(i["_id"]), str(i["transaction_date"]).replace("00:00:00",""), str(i["debit_amount"]), str(i["credit_amount"]),str(i["description_1"]), str(i["description_2"]), str(i["category"])))

    delete = input("Please enter the transaction ID which you want to delete: ")

    try:
        result2 = db.transactions.find({"email" : u_email, "_id" : ObjectId(delete)})
        
        if result2:
            print("Transaction exist")
            result1 = db.transactions.find_one_and_delete({ "_id" : ObjectId(delete), "email" : u_email}, projection={"_Id" : 1, "transaction_date" : 1, "debit_amount" : 1, "credit_amount" : 1, "description_1" : 1, "description_2" : 1, "category" : 1})
            pprint.pprint(result1)
            print("Transaction successfully deleted")
        else:
            print("Transaction does not exist")
    except:
        print("Transaction does not exist")

#### END DELETE TRANSACTION FUNCTIONS ####
