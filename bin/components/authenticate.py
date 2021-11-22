import inquirer as iq
import components.utils as ut
import time as t
from components.utils import User, screen_clear
from components.dbconnection import session, user
from sqlalchemy import exists
from datetime import date


#launch authentication UI
def launchAuthenUI():
    screen_clear()
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
            
            print(f"\n\t\t\t\t{'||' : <10}{ut.bcolors.OKGREEN}{'Logged In Successfully' : ^10}{ut.bcolors.ENDC}{'||' : >10}")
            
            return True

        else:
            #ut.screen_clear()
            print(f"\n\t\t\t\t{'||' : <10}{ut.bcolors.FAIL}Invalid Username or Password!{ut.bcolors.ENDC}{'||' : >10}")
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
        print(f"is there an existing email?: {email}")

        name = session.query(exists(user.c.name).where(
            user.c.name == usrname)).scalar()
        print(f"is there an existing name?: {name}")
        
        t.sleep(1)
        # registering logic
        if email or name == True:
            if email == True:
                print("Existing email in use!")
                t.sleep(1)
            else:
                print("User name have been taken")
                t.sleep(1)
            
            return False

        else:
            today = date.today()

            #### RDMS QUERY ####
            newUser = User(date_registered=today, name=usrname,
                           bank_name=bk, password=pw, email=usremail)
            session.add(newUser)
            session.commit()

            print('Successfully registered! Returning to main menu!\n')
            t.sleep(1)

            return True

    except:
        print("Error occurred while registering, please try again!\n")
    
    return 0





#authenticate()
#print(emailadd)