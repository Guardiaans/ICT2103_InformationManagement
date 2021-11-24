from components.dbconnection import category, budget, user, session
import inquirer as iq
import components.utils as ut
import sqlalchemy as sq
from components.sub_menu_components.budget_management import checkCatName, deleteBudget


def manageBudget(user_profile):
    ut.screen_clear()
    # Menu options for user
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

        checkCatName(user_profile)

    elif (menuoption == 'Delete budget'):
        deleteBudget(user_profile)

    else:
        pass
        return None

    return None