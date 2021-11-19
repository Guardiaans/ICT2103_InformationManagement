# import components.dbconnection as db
# import inquirer as iq
# import time as t
# import components.utils as ut
# import matplotlib.pyplot as plt

def overallSummary():
    # option = iq.list_input("What would you like to view?",
    #                         choices=['By Category', 'Debit vs Credit', 'Exit', ])
    # if option == "By Category":
    #     emailReturned = "csy@gmail.com"
    #     stmt = db.text("SELECT sum(t.credit_amount) as Expense, c.category_name FROM transaction_data t, category c, user_detail u " +
    #                 "WHERE t.category_id=c.category_id AND u.account_id=t.account_id AND t.transaction_date BETWEEN '2021-10-01' AND '2021-10-31' AND u.email=:email " +
    #                 "GROUP BY c.category_name")
    #     stmt = stmt.columns(db.transaction.c.credit_amount, db.category.c.category_name)
    #     stmt = stmt.bindparams(email=emailReturned)
    #     results = db.session.query(db.transaction.c.credit_amount,
    #                             db.category.c.category_name).from_statement(stmt).all()
    #     # print(results)
    #     # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    #     labels = []
    #     sizes = []
    #     cleanLabels = []
    #     cleanSizes = []
    #     for i in results:
    #         # print(type(i.credit_amount))
    #         # print(i.credit_amount)
    #         sizes.append(i.credit_amount[1:].replace(",", ""))
    #         labels.append(i.category_name)

    #     # print(labels)

    #     for i in range(0, len(sizes)):
    #         if (sizes[i] != '0.00'):
    #             cleanLabels.append(labels[i])
    #             cleanSizes.append(sizes[i])
    #     print(cleanLabels)

    #     # explode = (0, 0.1, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    #     fig1, ax1 = plt.subplots()
    #     ax1.pie(cleanSizes, labels=cleanLabels, autopct='%1.1f%%',
    #             shadow=True, startangle=90)
    #     ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    #     plt.show()
    # elif option == "Debit vs Credit":
    #     emailReturned = "csy@gmail.com"
    #     stmt = db.text("SELECT sum(t.debit_amount) as debit, sum(t.credit_amount) as credit " + 
    #                 "FROM transaction_data t, user_detail u WHERE t.account_id=u.account_id " +  
    #                 "AND t.transaction_date BETWEEN '2021-09-01' AND '2021-09-30' AND u.email=:email")
    #     stmt = stmt.columns(db.transaction.c.debit_amount, db.transaction.c.credit_amount)
    #     stmt = stmt.bindparams(email=emailReturned)
    #     results = db.session.query(db.transaction.c.debit_amount, db.transaction.c.credit_amount).from_statement(stmt).all()
    #     print(results)


    #     labels = ["Income", "Expenses"]
    #     sizes = [results[0].debit_amount[1:].replace("," ,""), results[0].credit_amount[1:].replace("," ,"")]

    #     # Pie chart, where the slices will be ordered and plotted counter-clockwise:

    #     # explode = (0, 0.1, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    #     fig1, ax1 = plt.subplots()
    #     ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
    #             shadow=True, startangle=90)
    #     ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    #     plt.show()