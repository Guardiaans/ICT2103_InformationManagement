# from components.dbconnection import *
# import inquirer as iq
# import components.dbconnection as db
import inquirer as iq
import time as t
# import components.utils as ut
import matplotlib.pyplot as plt
import re


from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://shengyu98:PiJF4JXI@cluster0.zwj7f.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["expenseTracker"]
collection = db["expenseTracker"]

def transaction_table():
    print("viewing transaction table")
    year = iq.text(message="Enter a year <2021>")
    month = iq.text(message="Enter a month <10>")
    date = month+'/'+year
    print(type(date))
    email = 'csy@gmail.com'

    query = {"email":email,"transactions.category":{"$regex": "Food" }}
    query2 = {"account_id" : 1001}
    result = collection.find(query2)
    transactions = {}
    # print(result)
    for x in result:
        print(x)
        transactions = x['transactions']

    # print(transactions[0])
    print(len(transactions))
    # print("{:<13}{:<12}{:<12}{:<50}{:<50}{:<5}".format("date","debit", "credit", "description_1","description_2", "category"))
    # print("_________________________________________________________________________________________________________________________________________")
    # for i in transactions:
    #     print("{:<13}{:<12}{:<12}{:<50}{:<50}{:<5}".format(i["transaction_date"], i["debit_amount"], i["credit_amount"], i["description_1"], i["description_2"], i["category"]))



transaction_table()

# def transaction_table(usremail):
#     print("viewing transaction table")
#     year = iq.text(message="Enter a year <2021>")
#     month = iq.text(message="Enter a month <10>")
#     email=usremail
#     stmt = text("SELECT t.transaction_id, t.transaction_date, t.debit_amount, " +
#                 "t.credit_amount, t.description_1, t.description_2, c.category_name " +
#                 " FROM transaction_data t, user_detail u, category c "+
#                 "WHERE t.account_id = u.account_id AND c.category_id = t.category_id " + 
#                 " AND u.email=:email AND CAST(t.transaction_date as character varying(50)) LIKE ':year-%:month-%'") 
#     stmt = stmt.columns(transaction.c.transaction_id, transaction.c.transaction_date, transaction.c.debit_amount, transaction.c.credit_amount, transaction.c.description_1, transaction.c.description_2, category.c.category_name)
#     stmt = stmt.bindparams(year=int(year), month=int(month), email=email)
#     results = session.query(transaction.c.transaction_id, transaction.c.transaction_date, transaction.c.debit_amount, transaction.c.credit_amount, transaction.c.description_1, transaction.c.description_2, category.c.category_name).from_statement(stmt).all()
    # print("{:<5}{:<13}{:<12}{:<12}{:<40}{:<40}{:<5}".format("id","date","debit", "credit", "description_1","description_2", "category"))
    # print("_________________________________________________________________________________________________________________________________________")
    # for i in results:
    #     print("{:<5}{:<13}{:<12}{:<12}{:<40}{:<40}{:<5}".format(str(i.transaction_id), str(i.transaction_date), str(i.debit_amount), str(i.credit_amount), str(i.description_1), str(i.description_2), str(i.category_name)))
    
    
#     menuoption = iq.list_input(f"Select an option",
#                               choices=['Back',
#                               ])
#     return menuoption

# def overallSummary(email):
#     option = iq.list_input("What would you like to view?",
#                             choices=['By Category', 'Debit vs Credit', 'Exit' ])
#     year = iq.text(message="Enter a year (e.g. 2021)")
#     month = iq.text(message="Enter a month (e.g. 10)")
#     if option == "By Category":
#         emailReturned = "csy@gmail.com"
#         stmt = db.text("SELECT sum(t.debit_amount) as Expense, c.category_name FROM transaction_data t, category c, user_detail u " +
#                     "WHERE t.category_id=c.category_id AND u.account_id=t.account_id AND CAST(t.transaction_date as character varying(50)) LIKE ':year-%:month-%' AND u.email=:email " +
#                     "GROUP BY c.category_name")
#         stmt = stmt.columns(db.transaction.c.debit_amount, db.category.c.category_name)
#         stmt = stmt.bindparams(email=emailReturned, year=int(year), month=int(month))
#         results = db.session.query(db.transaction.c.debit_amount,
#                                 db.category.c.category_name).from_statement(stmt).all()
#         # print(results)
#         # Pie chart, where the slices will be ordered and plotted counter-clockwise:
#         labels = []
#         sizes = []
#         cleanLabels = []
#         cleanSizes = []
#         for i in results:
#             # print(type(i.debit_amount))
#             # print(i.debit_amount)
#             sizes.append(i.debit_amount[1:].replace(",", ""))
#             labels.append(i.category_name)

#         # print(labels)

#         for i in range(0, len(sizes)):
#             if (sizes[i] != '0.00'):
#                 cleanLabels.append(labels[i])
#                 cleanSizes.append(sizes[i])
#         print(cleanLabels)

#         # explode = (0, 0.1, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

#         fig1, ax1 = plt.subplots()
#         ax1.pie(cleanSizes, labels=cleanLabels, autopct='%1.1f%%',
#                 shadow=True, startangle=90)
#         ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

#         print("Displaying your graph!")

#         return plt.show()

#     elif option == "Debit vs Credit":

#         emailReturned = email
#         stmt = db.text("SELECT sum(t.debit_amount) as debit, sum(t.credit_amount) as credit " + 
#                     "FROM transaction_data t, user_detail u WHERE t.account_id=u.account_id " +  
#                     "AND CAST(t.transaction_date as character varying(50)) LIKE ':year-%:month-%' AND u.email=:email")
#         stmt = stmt.columns(db.transaction.c.debit_amount, db.transaction.c.credit_amount)
#         stmt = stmt.bindparams(email=emailReturned, year=int(year), month=int(month))
#         results = db.session.query(db.transaction.c.debit_amount, db.transaction.c.credit_amount).from_statement(stmt).all()
#         print(results)


#         labels = ["Income", "Expenses"]
#         sizes = [results[0].debit_amount[1:].replace("," ,""), results[0].credit_amount[1:].replace("," ,"")]

#         # Pie chart, where the slices will be ordered and plotted counter-clockwise:

#         # explode = (0, 0.1, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

#         fig1, ax1 = plt.subplots()
#         ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
#                 shadow=True, startangle=90)
#         ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

#         print("Displaying your graph!")

#         return plt.show()

#     return
class dateInput():
    def __init__(self,yr , mnth) -> None:
        self.year = yr
        self.month = mnth

def getDateInput():
    year = iq.text(message="Enter a year (e.g. 2021)")
    month = iq.text(message="Enter a month (e.g. 10)")
    d = dateInput(year, month)
    return d

def transaction_table(usremail):

    year = iq.text(message="Enter a year <2021>")
    month = iq.text(message="Enter a month <10>")
    email=usremail
    
    print("\n\n")
    stmt = text("SELECT t.transaction_id, t.transaction_date, t.debit_amount, " +
                "t.credit_amount, t.description_1, t.description_2, c.category_name " +
                " FROM transaction_data t, user_detail u, category c "+
                "WHERE t.account_id = u.account_id AND c.category_id = t.category_id " + 
                " AND u.email=:email AND CAST(t.transaction_date as character varying(50)) LIKE ':year-%:month-%'" + 
                " ORDER BY t.transaction_date ASC") 
    stmt = stmt.columns(transaction.c.transaction_id, transaction.c.transaction_date, transaction.c.debit_amount, transaction.c.credit_amount, transaction.c.description_1, transaction.c.description_2, category.c.category_name)
    stmt = stmt.bindparams(year=int(year), month=int(month), email=email)
    results = session.query(transaction.c.transaction_id, transaction.c.transaction_date, transaction.c.debit_amount, transaction.c.credit_amount, transaction.c.description_1, transaction.c.description_2, category.c.category_name).from_statement(stmt).all()
    print("{:<5}{:<13}{:<12}{:<12}{:<40}{:<40}{:<5}".format("id","date","debit", "credit", "description_1","description_2", "category"))
    print("_________________________________________________________________________________________________________________________________________")
    for i in results:
        print("{:<5}{:<13}{:<12}{:<12}{:<40}{:<40}{:<5}".format(str(i.transaction_id), str(i.transaction_date), str(i.debit_amount), str(i.credit_amount), str(i.description_1), str(i.description_2), str(i.category_name)))
    print("\n\n")
    
    menuoption = iq.list_input(f"Select an option",
                              choices=['Back',
                              ])
    return menuoption

def overallSummary(email):

    option = iq.list_input("What would you like to view?",
                            choices=['By Category', 'Debit vs Credit', 'Exit' ])
    
    if option == "By Category":
        emailReturned = email
        
        my_date = getDateInput()

        stmt = db.text("SELECT sum(t.debit_amount) as Expense, c.category_name FROM transaction_data t, category c, user_detail u " +
                    "WHERE t.category_id=c.category_id AND u.account_id=t.account_id AND CAST(t.transaction_date as character varying(50)) LIKE ':year-%:month-%' AND u.email=:email " +
                    "GROUP BY c.category_name")
        stmt = stmt.columns(db.transaction.c.debit_amount, db.category.c.category_name)
        stmt = stmt.bindparams(email=emailReturned, year=int(my_date.year), month=int(my_date.month))
        results = db.session.query(db.transaction.c.debit_amount,
                                db.category.c.category_name).from_statement(stmt).all()
        # print(results)
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = []
        sizes = []
        cleanLabels = []
        cleanSizes = []
        for i in results:
            # print(type(i.debit_amount))
            # print(i.debit_amount)
            sizes.append(i.debit_amount[1:].replace(",", ""))
            labels.append(i.category_name)

        # print(labels)

        for i in range(0, len(sizes)):
            if (sizes[i] != '0.00'):
                cleanLabels.append(labels[i])
                cleanSizes.append(sizes[i])
        print(cleanLabels)

        # explode = (0, 0.1, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

        fig1, ax1 = plt.subplots()
        ax1.pie(cleanSizes, labels=cleanLabels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        print("Displaying your graph!")

        return plt.show()

    elif option == "Debit vs Credit":
        
        my_date = getDateInput()

        emailReturned = email
        stmt = db.text("SELECT sum(t.debit_amount) as debit, sum(t.credit_amount) as credit " + 
                    "FROM transaction_data t, user_detail u WHERE t.account_id=u.account_id " +  
                    "AND CAST(t.transaction_date as character varying(50)) LIKE ':year-%:month-%' AND u.email=:email")
        stmt = stmt.columns(db.transaction.c.debit_amount, db.transaction.c.credit_amount)
        stmt = stmt.bindparams(email=emailReturned, year=int(my_date.year), month=int(my_date.month))
        results = db.session.query(db.transaction.c.debit_amount, db.transaction.c.credit_amount).from_statement(stmt).all()
        print(results)


        labels = ["Income", "Expenses"]
        sizes = [results[0].debit_amount[1:].replace("," ,""), results[0].credit_amount[1:].replace("," ,"")]

        # Pie chart, where the slices will be ordered and plotted counter-clockwise:

        # explode = (0, 0.1, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        print("Displaying your graph!")

        return plt.show()
    
    else:
        pass

    return 
