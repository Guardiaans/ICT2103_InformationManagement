import inquirer as iq
import components.utils as ut

def manageBudget():
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
        #implement create transaction method.
        print("Create budget method here")

    elif (menuoption == 'Delete budget'):
        #implement delete transaction method.
        print("delete budget method here")

    else:
        #exit or logout option implementation
        print("returning back to main menu")
        return None

    return None
