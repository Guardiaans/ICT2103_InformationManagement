from components.dbconnection import category, transaction,user,session
import sqlalchemy as sq
import inquirer as iq
from decimal import *

def compareUserData(user_profile):
    #TODO: Implement method by using data from database
    #print("comparing user data")
    options = []
    stmt = sq.text("SELECT user_detail.email " + \
    "FROM user_detail ")
    stmt = stmt.columns(user.c.email)
    results = session.query(user.c.email).from_statement(stmt).all()
    for items in results:
        if items != user_profile.email:
            options.append(items[0])
    
    menuoption = iq.list_input(f"Select a user to compare with! ",
                              choices=options)

    cEmail = menuoption

    result = db.transactions.aggregate([{ "$match" : {"email" : user_profile, "debit_amount" : {"$gt":0}}}, {"$group": {"_id" : "$category",  "totalAmt" : {"$sum": "$debit_amount"}}}])

    #choose the user you want to compare with
    result2 = db.transactions.aggregate([{ "$match" : {"email" : cEmail, "debit_amount" : {"$gt":0}}}, {"$group": {"_id" : "$category",  "totalAmt" : {"$sum": "$debit_amount"}}}])

    resultDisplay = []
    for x in result:
        resultDisplay.append(x)

    resultDisplay2 = []
    for x in result2:
        resultDisplay2.append(x)

    getcontext().prec = 2
    print("Total amount spent for user: ", user_profile)
    print("{:<30}{:<15}".format("Category","Total Amount spent"))
    print(80*"_")
    for i in resultDisplay:
        print(f"{i['_id']:<30}", f"{(i['totalAmt']):<15.2f}")

    print("\n\n")
    print("Total amount spent for user: ", cEmail)
    print("{:<30}{:<15}".format("Category","Total Amount spent"))
    print(80*"_")
    for i in resultDisplay2:
        print(f"{i['_id']:<30}", f"{(i['totalAmt']):<15.2f}")

    menuoption = iq.list_input(f"Select an option",
                                choices=['Back',
                                ])

    return menuoption