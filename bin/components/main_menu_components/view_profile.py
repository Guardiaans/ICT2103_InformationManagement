from components.dbconnection import user,session
from sqlalchemy import *
import inquirer as iq

def viewProfile(user_profile):
    
    print(f'''
    Hello {user_profile.name} here are your details!

    ACCOUNT ID      : {user_profile.id}
    DATE REGISTERED : {user_profile.registered}
    NAME            : {user_profile.name}
    BANK NAME       : {user_profile.bank}
    ACCOUNT BALANCE : {user_profile.balance}
    EMAIL           : {user_profile.email}

    ''')

    menuoption = iq.list_input(f"Select an option",
                              choices=['Back',
                              ])
    return menuoption


