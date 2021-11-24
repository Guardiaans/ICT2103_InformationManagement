from datetime import datetime, timedelta
from sqlalchemy import *
from components.dbconnection import transaction, session
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
   
    # stmt = text("SELECT SUM(transaction_data.credit_amount)/3 AS prediction " + \
    # "FROM transaction_data " + \
    # "WHERE transaction_data.transaction_date <= :todayTime " + \
    # "AND transaction_data.transaction_date >= :n_days_agoTime " + \
    # "AND transaction_data.account_id = (SELECT user_detail.account_id FROM user_detail WHERE user_detail.email = :mainUser)")

    # stmt = stmt.columns(transaction.c.credit_amount)
    # stmt = stmt.bindparams(todayTime = today, n_days_agoTime = n_days_ago, mainUser = userEmail)
    # results = session.query(transaction.c.credit_amount).from_statement(stmt).all()
    # for i in results:
    #     print("\nYour current prediction of total spending for this month is: ", (str(i.credit_amount)), "\n\n")

    