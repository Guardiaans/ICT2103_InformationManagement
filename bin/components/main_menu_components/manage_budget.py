from components.dbconnection import category, budget, user, session
import inquirer as iq
import components.utils as ut
import sqlalchemy as sq

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
        budgetAmount = iq.text(message="Enter budget amount")
        monthInsert = iq.text(message="Enter month number")
        yearInsert = iq.text(message="Enter year")
        descInsert = iq.text(message="Enter description")
        categoryInsert = iq.text(message="Enter category name")
        stmt = sq.text("INSERT INTO budget VALUES(?, ?, ?, ?) "
                       ", b.actual_spent, c.category_name FROM budget b, user_detail u, category c "
                       "WHERE b.account_id = u.account_id AND c.category_id = b.category_id "
                       "AND u.email=:email")
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
