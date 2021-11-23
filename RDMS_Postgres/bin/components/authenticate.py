import inquirer as iq
import components.utils as ut
import time as t
from sqlalchemy import *
from components.utils import User, screen_clear
from components.dbconnection import session, user
from sqlalchemy import exists
from datetime import date
from components.dbconnection import user

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
        usr_email = session.query(exists(user.c.email).where(user.c.email == email)).scalar()

        stmt1 = text(f"SELECT user_detail.password = crypt('{password}',user_detail.password) " +
                "FROM user_detail " +
                "WHERE user_detail.email=:userEmail")
        stmt1 = stmt1.columns(user.c.password)
        stmt1 = stmt1.bindparams(userEmail=email)
        results = session.query(user.c.password).from_statement(stmt1).all()
        
        x = [item[0] for item in results]
        usr_pw = x[0]

        #select (password = crypt('water',password)) from user_detail where email = 'spongehe';
        #pw = session.query(exists(user.c.password).where(user.c.password == password)).scalar()

        if usr_email == True and usr_pw == True:
            
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
        #print(f"is there an existing email?: {email}")

        name = session.query(exists(user.c.name).where(
            user.c.name == usrname)).scalar()
        #print(f"is there an existing name?: {name}")
        
        t.sleep(1)
        # registering logic
        if email or name == True:
            if email == True:
                print("\nExisting email in use!")
                t.sleep(1)
            else:
                print("\nUser name have been taken")
                t.sleep(1)
            
            return False

        else:
            today = date.today()

            #### RDMS QUERY ####
            # newUser = User(date_registered=today, name=usrname,
            #                bank_name=bk, password=pw, email=usremail)

            newUser = text(
            "INSERT INTO user_detail (date_registered, name, bank_name, password, email) " + 
            "VALUES (:date_registered, :name, :bank_name, crypt(:password,gen_salt('md5')), :email)")
            newUser = newUser.bindparams(date_registered=today, name=usrname,
                                        bank_name=bk, password=pw, email=usremail)

            session.execute(newUser)
            session.commit()

            print('Successfully registered! Returning to main menu!\n')
            t.sleep(1)

            return True

    except:
        print("Error occurred while registering, please try again!\n")
    
    return 0





#authenticate()
#print(emailadd)