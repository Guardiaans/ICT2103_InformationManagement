import inquirer as iq
import time as t
import components.utils as ut
from components.utils import getUserProfile
from components.main_menu_components.view_profile import viewProfile
from components.main_menu_components.compare_user_data import compareUserData
from components.main_menu_components.manage_budget import manageBudget
from components.main_menu_components.manage_transaction import manageTransaction
from components.main_menu_components.upload_data import uploadData
from components.main_menu_components.view_budget import viewBudget
from components.main_menu_components.view_prediction import viewPrediction
from components.main_menu_components.view_transaction_summary import viewTransactionSummary

def mainMenu(email):
    ut.screen_clear()
    user_profile = getUserProfile(email)
    #Menu options for user
    menuoption = iq.list_input(f"Welcome to the Main Menu <{user_profile.name}>! What would you like to do today?",
                              choices=['View Profile', 'Upload Data', 
                              'View Transaction Summary',
                              'View Budget',
                              'View Prediction',
                              'Compare User data',
                              'Manage Transactions',
                              'Manage Budget',
                              'Logout',
                              'Exit'
                              ])
    if (menuoption) == 'View Profile':
        viewProfile(user_profile)
    elif (menuoption == 'Upload Data'):
        uploadData()
    elif (menuoption == 'View Transaction Summary'):
        viewTransactionSummary()
    elif (menuoption == 'View Budget'):
        viewBudget()
    elif (menuoption == 'View Prediction'):
        viewPrediction()
    elif (menuoption == 'Compare User data'):
        compareUserData(user_profile)
    elif (menuoption == 'Manage Transactions'):
        manageTransaction()
    elif (menuoption == 'Manage Budget'):
        manageBudget()
    elif (menuoption == 'Logout'):
        print(f"\n\t\t\t\t{'||' : <10}{ut.bcolors.OKBLUE}{'Logging you out!' : ^10}{ut.bcolors.ENDC}{'||' : >10}")
        t.sleep(1.5)
        return 'Logout'
    else:
        #exit or logout option implementation
        print("See you again!")
        return False

    t.sleep(1)

    return True

