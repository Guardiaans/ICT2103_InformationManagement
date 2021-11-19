import inquirer as iq
import components.utils as ut

def manageTransaction():
    #TODO: 
    # Implement create / inserting transaction in database
    # Implementing deleting of transaction in database
    # Implementing creating of category in database
    
    #print("managing transaction!")

    ut.screen_clear()
    #Menu options for user
    menuoption = iq.list_input("Managing transactions!",
                              choices=['Create or Insert transaction', 
                              'Delete transaction',
                              'Create or Insert Category',
                              'Back',
                              ])

    if (menuoption == 'Create or Insert transaction'):
        #implement create transaction method.
        print("Create transaction method here")

    elif (menuoption == 'Delete transaction'):
        #implement delete transaction method.
        print("delete transaction method here")

    elif (menuoption == 'Create or Insert Category'):
        #implement create category method.
        print("create category method here")

    else:
        #exit or logout option implementation
        print("returning back to main menu")
        return None

    return None