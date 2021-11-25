from sqlalchemy.sql.operators import exists
from components.dbconnection import category, transactions, user_data
from components.utils import getList
import sqlalchemy as sq
import inquirer as iq
from decimal import *

def compareUserData(user_profile):
    #TODO: Implement method by using data from database
    #print("comparing user data")
    myquery = {'Email' : {'$exists' : 'true'}}
    options = getList(myquery,'Email',user_data)
    
    
    menuoption = iq.list_input(f"Select a user to compare with! ",
                              choices=options)

    cEmail = menuoption

    result = transactions.aggregate([{ "$match" : {"email" : user_profile.email, "debit_amount" : {"$gt":0}}}, {"$group": {"_id" : "$category",  "totalAmt" : {"$sum": "$debit_amount"}}}])

    #choose the user you want to compare with
    result2 = transactions.aggregate([{ "$match" : {"email" : cEmail, "debit_amount" : {"$gt":0}}}, {"$group": {"_id" : "$category",  "totalAmt" : {"$sum": "$debit_amount"}}}])

    resultDisplay = []
    for x in result:
        resultDisplay.append(x)

    resultDisplay2 = []
    for x in result2:
        resultDisplay2.append(x)

    getcontext().prec = 2
    print("Total amount spent for user: ", user_profile.email)
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