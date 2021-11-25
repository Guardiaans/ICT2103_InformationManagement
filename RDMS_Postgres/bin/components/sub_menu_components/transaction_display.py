from components.dbconnection import *
import inquirer as iq
import time as t
import components.utils as ut
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
    my_date = getDateInput()
    
    email=usremail
    
    print("\n\n")
    stmt = text("SELECT t.transaction_id, t.transaction_date, t.debit_amount, " +
                "t.credit_amount, t.description_1, t.description_2, c.category_name " +
                " FROM transaction_data t, user_detail u, category c "+
                "WHERE t.account_id = u.account_id AND c.category_id = t.category_id " + 
                " AND u.email=:email AND CAST(t.transaction_date as character varying(50)) LIKE ':year-%:month-%'" + 
                " ORDER BY t.transaction_date ASC") 
    stmt = stmt.columns(transaction.c.transaction_id, transaction.c.transaction_date, transaction.c.debit_amount, transaction.c.credit_amount, transaction.c.description_1, transaction.c.description_2, category.c.category_name)
    stmt = stmt.bindparams(year=int(my_date.year), month=int(my_date.month), email=email)
    results = session.query(transaction.c.transaction_id, transaction.c.transaction_date, transaction.c.debit_amount, transaction.c.credit_amount, transaction.c.description_1, transaction.c.description_2, category.c.category_name).from_statement(stmt).all()
    print("{:<5}{:<13}{:<12}{:<12}{:<50}{:<50}{:<5}".format("id","date","debit", "credit", "description_1","description_2", "category"))
    print("_____________________________________________________________________________________________________________________________________________________________")
    for i in results:
        print("{:<5}{:<13}{:<12}{:<12}{:<50}{:<50}{:<5}".format(str(i.transaction_id), str(i.transaction_date), str(i.debit_amount), str(i.credit_amount), str(i.description_1), str(i.description_2), str(i.category_name)))
    print("\n\n")
    
    menuoption = iq.list_input(f"Select an option",
                              choices=['Back',
                              ])
    return menuoption

def overallSummary(email):

    option = iq.list_input("What would you like to view?",
                            choices=['Category Per Month', 'Debit vs Credit Per Year', 'Exit' ])
    
    if option == "Category Per Month":
        emailReturned = email
        
        my_date = getDateInput()

        stmt = text("SELECT sum(t.debit_amount) as Expense, c.category_name FROM transaction_data t, category c, user_detail u " +
                    "WHERE t.category_id=c.category_id AND u.account_id=t.account_id AND CAST(t.transaction_date as character varying(50)) LIKE ':year-%:month-%' AND u.email=:email " +
                    "GROUP BY c.category_name")
        stmt = stmt.columns(transaction.c.debit_amount, category.c.category_name)
        stmt = stmt.bindparams(email=emailReturned, year=int(my_date.year), month=int(my_date.month))
        results = session.query(transaction.c.debit_amount,
                                category.c.category_name).from_statement(stmt).all()
        labels = []
        sizes = []
        cleanLabels = []
        cleanSizes = []
        for i in results:
            sizes.append(i.debit_amount[1:].replace(",", ""))
            labels.append(i.category_name)

        for i in range(0, len(sizes)):
            if (sizes[i] != '0.00'):
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
        emailReturned = email
        stmt = text("SELECT sum(t.debit_amount), sum(t.credit_amount), date_part('month', t.transaction_date) as month "+
                        "FROM transaction_data t, user_detail u WHERE t.account_id=u.account_id AND u.email=:email "+
                        "AND date_part('year', t.transaction_date)=:year GROUP BY month ORDER BY month ASC")
        stmt = stmt.columns(transaction.c.debit_amount, transaction.c.credit_amount, transaction.c.transaction_date)
        stmt = stmt.bindparams(email=emailReturned, year=int(year))
        results = session.query(transaction.c.debit_amount, transaction.c.credit_amount, transaction.c.transaction_date).from_statement(stmt).all()

        labels = []
        debit = []
        credit = []
        cleanLabels=[]
        cleanDebit=[]
        cleanCredit=[]
        for index in range(len(results)):
            labels.append(results[index][2])
            debit.append(results[index][0])
            credit.append(results[index][1])

        for i in range(0, len(debit)):
            if (debit[i] != '0.00' or credit[i] != '0.00'):
                cleanLabels.append(calendar.month_abbr[int(labels[i])])
                cleanDebit.append(float(debit[i][1:].replace(",", "")))
                cleanCredit.append(float(credit[i][1:].replace(",", "")))


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
    
    else:
        pass

    return 

