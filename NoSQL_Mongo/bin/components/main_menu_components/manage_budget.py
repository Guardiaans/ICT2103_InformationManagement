import inquirer as iq
import components.utils as ut
from components.sub_menu_components.budget_management import createBudget, deleteBudget, updateBudget

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
                              'Delete budget','Update budget',
                              'Back',
                              ])

    if (menuoption == 'Create budget'):
        createBudget(user_profile)
        
    elif (menuoption == 'Delete budget'):
        deleteBudget(user_profile)

    elif (menuoption == 'Update budget'):
        updateBudget(user_profile)

    else:
        pass
        return None

    return None
