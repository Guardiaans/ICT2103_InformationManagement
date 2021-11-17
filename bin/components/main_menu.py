import inquirer as iq
import time as t
import components.utils as ut
from components.main_menu_components.compare_user_data import compareUserData
from components.main_menu_components.manage_budget import manageBudget
from components.main_menu_components.manage_transaction import manageTransaction
from components.main_menu_components.upload_data import uploadData
from components.main_menu_components.view_budget import viewBudget
from components.main_menu_components.view_prediction import viewPrediction
from components.main_menu_components.view_transaction_summary import viewTransactionSummary

menu = True

def mainMenu():
    ut.screen_clear()
    #Menu options for user
    menuoption = iq.list_input("Welcome to the Main Menu! What would you like to do today?",
                              choices=['Upload Data', 
                              'View Transaction Summary',
                              'View Budget',
                              'View Prediction',
                              'Compare User data',
                              'Manage Transactions',
                              'Manage Budget',
                              'Exit'
                              ])

    if (menuoption == 'Upload Data'):
        uploadData()
    elif (menuoption == 'View Transaction Summary'):
        viewTransactionSummary()
    elif (menuoption == 'View Budget'):
        viewBudget()
    elif (menuoption == 'View Prediction'):
        viewPrediction()
    elif (menuoption == 'Compare User data'):
        compareUserData()
    elif (menuoption == 'Manage Transactions'):
        manageTransaction()
    elif (menuoption == 'Manage Budget'):
        manageBudget()
    else:
        #exit or logout option implementation
        print("See you again!")
        menu = False
        return menu

    t.sleep(1)

    return True
