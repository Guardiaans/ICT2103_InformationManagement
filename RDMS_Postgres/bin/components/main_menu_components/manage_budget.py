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
        checkCatName(user_profile)

    elif (menuoption == 'Delete budget'):
        deleteBudget(user_profile)

    else:
        pass
        return None

    return None