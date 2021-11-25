from components.dbconnection import category, budget, user, session
import inquirer as iq
import components.utils as ut
import sqlalchemy as sq
from NoSQL_Mongo.bin.components.sub_menu_components.budget_management import createBudget

def manageBudget(user_profile):
    #TODO: 
    # Creating of sub menu for managing of budget
    # Implement create budget method
    # Implementing deleting of budget method
    
    # print("managing budget!")

    ut.screen_clear()
    #Menu options for user
    menuoption = iq.list_input("Managing Budget!",
                              choices=['Create budget', 
                              'Delete budget',
                              'Back',
                              ])

    if (menuoption == 'Create budget'):
        createBudget(user_profile)
        
    elif (menuoption == 'Delete budget'):
        #implement delete transaction method.
        print("delete budget method here")

    else:
        pass
        return None

    return None
