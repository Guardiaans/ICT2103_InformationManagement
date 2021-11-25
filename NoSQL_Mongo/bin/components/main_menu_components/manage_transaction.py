import inquirer as iq
import components.utils as ut
import components.sub_menu_components.transaction_management as tm

def manageTransaction(user_profile):
    
    ut.screen_clear()

    #getting profile information
    usr_id = user_profile.id
    usr_email = user_profile.email

    #Menu options for user
    menuoption = iq.list_input("Managing transactions!",
                              choices=['Create or Insert transaction', 
                              'Delete transaction',
                              'Back',
                              ])

    if (menuoption == 'Create or Insert transaction'):
        #adding transaction
        tm.insertTransaction(usr_email)
    elif (menuoption == 'Delete transaction'):
        #adding transaction
        tm.deleteTransaction(usr_email)
    else:
        
        print("returning back to main menu")
        return None

    return None