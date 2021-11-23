from datetime import datetime, timedelta
from sqlalchemy import *
from components.dbconnection import transaction, session, category
import inquirer as iq

def viewPrediction(user_profile):
    #TODO: Implement view prediction method()
    
    predictData(user_profile.email)

    menuoption = iq.list_input(f"Select an option",
                              choices=['Back',
                              ])
    return menuoption

def predictData(userEmail):

    N_DAYS_AGO = 90

    today = datetime.now()    
    n_days_ago = today - timedelta(days=N_DAYS_AGO)
    print(f'''

    PREDICTION START DATE    : {n_days_ago.date()}
    TODAY'S DATE             : {today.date()}
    DATA USED FOR PREDICTION : {N_DAYS_AGO}"

    ''')
   
    stmt = text("SELECT category.category_name, SUM(transaction_data.debit_amount)/3 AS prediction " + \
    "FROM transaction_data " + \
    "JOIN category " + \
    "ON category.category_id = transaction_data.category_id " + \
    "WHERE transaction_data.transaction_date <= :todayTime " + \
    "AND transaction_data.transaction_date >= :n_days_agoTime " + \
    "AND transaction_data.account_id = (SELECT user_detail.account_id FROM user_detail WHERE user_detail.email = :mainUser) " + \
    "GROUP BY category.category_name HAVING SUM(transaction_data.debit_amount)/3 > '0'")

    stmt = stmt.columns(category.c.category_name, transaction.c.debit_amount)
    stmt = stmt.bindparams(todayTime = today, n_days_agoTime = n_days_ago, mainUser = userEmail)
    results = session.query(category.c.category_name, transaction.c.debit_amount).from_statement(stmt).all()

    print("Your prediction for this month: ")
    print("{:<20}{:<12}".format("Category", "Amount"))
    print("______________________________________________________________________")
    for i in results:
        print("{:<20}: {:<12}".format(str(i.category_name), str(i.debit_amount)))
    print("\n")