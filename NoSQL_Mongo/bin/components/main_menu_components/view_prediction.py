from datetime import datetime, timedelta
from sqlalchemy import *
from components.dbconnection import transactions, user_data
from components.utils import getList, removeDup
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
    end_date = datetime.now()    
    start_date = end_date - timedelta(days=N_DAYS_AGO)

    #making query statement
    myquery = {'email' : userEmail, 'transaction_date' : {'$lt':end_date, '$gt':start_date}}

    print(f'''

    PREDICTION START DATE    : {start_date.date()}
    TODAY'S DATE             : {end_date.date()}
    DATA USED FOR PREDICTION : {N_DAYS_AGO}"

    ''')
    #Using a function the get a list from the query table based on the document field.
    category = getList(myquery,'category')
    #removing duplicates from the list of category to iterate a table.
    catlist = removeDup(category)
    
    #printing out the table for the prediction.
    print("Your spending prediction for this month")
    print("{:<16}{}".format("Category", "Prediction Amount"))
    print('---------------------------------')
    for cate in catlist:
        if getCatPredict('kgc@gmail.com',start_date,end_date,cate) != '0':
            print("{:<16}{}".format(cate, "$"+getCatPredict(userEmail,start_date,end_date,cate)))

#Function to calculate all the figures in the selected category and return a Sum.
def getCatPredict(user_email: str, startdate: str, enddate: str, category:str) -> str:
    query2 = {'email' : user_email, 'transaction_date' : {'$lt':enddate, '$gt':startdate}, 'category':category, 'debit_amount':{'$gt':0}}
    db_a = []
    for x in transactions.find(query2):
        db_a.append(x['debit_amount'])
    predicted_debit_aggregate = int(sum(db_a)/3)
    return str(predicted_debit_aggregate)

