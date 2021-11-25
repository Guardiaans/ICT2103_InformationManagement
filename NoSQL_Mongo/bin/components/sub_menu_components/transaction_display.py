from components.dbconnection import *
import inquirer as iq
import time as t
import components.utils as ut
import re
import numpy as np
import matplotlib.pyplot as plt
import calendar

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
    print("viewing transaction table")
    date = getDateInput()
    email=usremail
    query = {"email":email, "$expr": {"$eq":[{"$year": "$transaction_date"}, int(date.year)], "$eq": [{ "$month": "$transaction_date" }, int(date.month)] }}
    result = transactions.find(query).sort("transaction_date",1)
    transactionDisplay = []
    for x in result:    
        transactionDisplay.append(x)
    print("{:<13}{:<12}{:<12}{:<50}{:<50}{:<5}".format("date","debit", "credit", "description_1","description_2", "category"))
    print("_____________________________________________________________________________________________________________________________________________________________")
    for i in transactionDisplay:
        print("{:<13}{:<12}{:<12}{:<50}{:<50}{:<5}".format(str(i["transaction_date"]).replace("00:00:00",""), str(i["debit_amount"]), str(i["credit_amount"]),str(i["description_1"]), str(i["description_2"]), str(i["category"])))

    
    menuoption = iq.list_input(f"Select an option",
                              choices=['Back',
                              ])
    return menuoption

def overallSummary(email):
    option = iq.list_input("What would you like to view?",
                            choices=['Category Per Month', 'Debit vs Credit Per Year', 'Exit' ])
    if option == "Category Per Month":
        date = getDateInput()
        print("Displaying your graph!")
        labels = []
        sizes = []
        cleanLabels = []
        cleanSizes = []
        #aggregation is used to do multiple 'select' or condition statements together
        results = transactions.aggregate([
            {"$match": {"email":email,"$expr": {"$eq":[{"$year": "$transaction_date"}, int(date.year)], "$eq": [{ "$month": "$transaction_date" }, int(date.month) ] }} },
            {"$group": 
                {
                    "_id": "$category",
                    "Expenses": {"$sum": "$debit_amount"}
                }
            }
        ])
        
        # Store _id key (category) into labels and Expenses into sizes
        for x in results:
            labels.append(x["_id"])
            sizes.append(x["Expenses"])

        for i in range(0, len(sizes)):
            if (sizes[i] != 0):
                cleanLabels.append(labels[i])
                cleanSizes.append(sizes[i])

        fig1, ax1 = plt.subplots()
        ax1.pie(cleanSizes, labels=cleanLabels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        print("Displaying your graph!")

        return plt.show()

    elif option == "Debit vs Credit Per Year":
        year = iq.text(message="Enter a year (e.g. 2021)")
        print("Displaying your graph!")
        labels = []
        debit = []
        credit = []
        cleanLabels=[]
        cleanDebit=[]
        cleanCredit=[]
        results = transactions.aggregate([
            {"$match": {"email":email,"$expr": {"$eq":[{"$year": "$transaction_date"}, int(year)] }} },
            {"$group": 
                {
                    "_id": {"$month": "$transaction_date"},
                    "Expenses": {"$sum": "$debit_amount"},
                    "Income": {"$sum": "$credit_amount"}
                }
            },
            {
                "$sort": 
                {
                    "_id" :1
                }
            }
        ])
        for x in results:
            labels.append(x["_id"])
            debit.append(x["Expenses"])
            credit.append(x["Income"])

        for i in range(0, len(debit)):
            if (debit[i] != 0 or credit[i] != 0):
                cleanLabels.append(calendar.month_abbr[labels[i]])
                cleanDebit.append(debit[i])
                cleanCredit.append(credit[i])

        x = np.arange(len(cleanLabels))  # the label locations
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width/2, cleanDebit, width, label='Expense')
        rects2 = ax.bar(x + width/2, cleanCredit, width, label='Income')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Amount')
        ax.set_title('Income and Expense Per Year')
        ax.set_xticks(x, cleanLabels)
        ax.legend()

        ax.bar_label(rects1, padding=3)
        ax.bar_label(rects2, padding=3)

        fig.tight_layout()

        plt.show()

    return
