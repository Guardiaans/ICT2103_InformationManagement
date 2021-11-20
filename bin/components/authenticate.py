import inquirer as iq
import components.utils as ut
from components.utils import User
from components.dbconnection import session, user
from sqlalchemy import exists
from datetime import date

#launch authentication UI
def launchAuthenUI():
    print("""
            _________________________________________________________________________
            |                                                                       |
            |                  Welcome to OKFINANCE Management!                     |
            |_______________________________________________________________________|
    """)
    #only given two choice
    #inquirer import function
    option = iq.list_input("Login or Register?",
                              choices=['Login', 'Register', 'Exit',])

    return option

def verifyCredentials(email, password):

    try:
        #### RDMS query ####
        email = session.query(exists(user.c.email).where(user.c.email == email)).scalar()
        pw = session.query(exists(user.c.password).where(user.c.password == password)).scalar()

        if email == True and pw == True:
            
            print("\t\t\tLogin Successfully")
            
            return True

        else:
            #ut.screen_clear()
            print(f"\n\n\t\t\t\t{ut.bcolors.FAIL}Invalid Username or Password!{ut.bcolors.ENDC}")
            return False
    except:
        print("Unable to authenticate!")

    return False

def register(usrname, pw, bk, usremail):

    try:
        #### RDMS QUERY ####
        # check if user name or email exist in database
        email = session.query(exists(user.c.email).where(
            user.c.email == usremail)).scalar()
        #print(f"is there an existing email?: {email}")

        name = session.query(exists(user.c.name).where(
            user.c.name == usrname)).scalar()
        #print(f"is there an existing name?: {name}")

        # registering logic
        if email or name == True:
            if email == True:
                print("Existing email in use!")
            else:
                print("User name have been taken")
        else:
            today = date.today()

            #### RDMS QUERY ####
            newUser = User(date_registered=today, name=usrname,
                           bank_name=bk, password=pw, email=usremail)
            session.add(newUser)
            session.commit()

            print('Successfully registered! Returning to main menu!\n')

    except:
        print("Error occurred while registering, please try again!\n")





#authenticate()
#print(emailadd)