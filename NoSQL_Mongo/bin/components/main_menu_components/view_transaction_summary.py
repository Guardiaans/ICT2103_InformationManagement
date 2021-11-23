from components.sub_menu_components.transaction_display import transaction_table, overallSummary
from components.dbconnection import *
import inquirer as iq
import time as t
import components.utils as ut

def viewTransactionSummary(user_profile):
    #TODO: 
    # Add in Overall Summary Method
    # Add in Transaction table Method
    usremail = user_profile.email
    ut.screen_clear()
    # #Menu options for user
    menuoption = iq.list_input("Welcome to the Transaction Menu! What would you like to do today?",
                              choices=['View Overall Summary', 'View Transaction Table',
                              'Back'
                              ])
    
    if (menuoption == "View Transaction Table"):
        transaction_table(usremail)
    elif (menuoption == "View Overall Summary"):
        overallSummary(usremail)
    else:
        return
    
    return