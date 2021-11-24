import inquirer as iq
import components.utils as ut
import time as t
from components.utils import screen_clear
from components.dbconnection import user_data
from typing import Tuple
import os
import hashlib
import hmac
import datetime as dt



## CLIENT SIDE HASHING FOR MONGODB ##


def hash_new_password(password: str) -> Tuple[bytes, bytes]:
    """
    Hash the provided password with a randomly-generated salt and return the
    salt and hash to store in the database.
    """
    salt = os.urandom(16)
    pw_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt, pw_hash


def is_correct_password(salt: bytes, pw_hash: bytes, password: str) -> bool:
    """
    Given a previously-stored salt and hash, and a password provided by a user
    trying to log in, check whether the password is correct.
    """
    return hmac.compare_digest(
        pw_hash,
        hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    )

# launch authentication UI


def launchAuthenUI():
    screen_clear()
    print("""
            _________________________________________________________________________
            |                                                                       |
            |                  Welcome to OKFINANCE Management!                     |
            |_______________________________________________________________________|
    """)
    # only given two choice
    # inquirer import function
    option = iq.list_input("Login or Register?",
                           choices=['Login', 'Register', 'Exit', ])

    return option

## VERIFY THE LOGIN CREDENTIAL FUNCTION ##


def verifyCredentials(email_input, password_input):

    try:
        mydict = {}
        #### NOSQL MONGO Query ####
        myquery = {"Email": {'$exists': 'true', '$eq': email_input}}
        # Checking if document with such email exist
        usr_count = user_data.count_documents(myquery)

        # verifying password hashes.
        for x in user_data.find(myquery):
            mydict = x
        usr_pw_h = mydict["Password"]
        usr_salt = mydict["Salt"]
        pw = is_correct_password(usr_salt, usr_pw_h, password_input)

        if usr_count == 1 and pw == True:

            print(
                f"\n\t\t\t\t{'||' : <10}{ut.bcolors.OKGREEN}{'Logged In Successfully' : ^10}{ut.bcolors.ENDC}{'||' : >10}")

            return True

        else:
            # ut.screen_clear()
            print(
                f"\n\t\t\t\t{'||' : <10}{ut.bcolors.FAIL}Invalid Username or Password!{ut.bcolors.ENDC}{'||' : >10}")
            return False
    except:
        print("Unable to authenticate!")

    return False

## REGISTERING USER FUNCTION ##


def register(usrname, pw, bk, usremail):

    try:
        #### NOSQL QUERY ####
        myquery_email = {"Email": {'$exists': 'true', '$eq': usremail}}
        myquery_name = {"Name": {'$exists': 'true', '$eq': usrname}}
        # check if user name or email exist in database
        usr_count_email = user_data.count_documents(myquery_email)
        usr_count_name = user_data.count_documents(myquery_name)
        #print(f"is there an existing name?: {name}")

        t.sleep(1)
        # registering logic
        if usr_count_email or usr_count_name == 1:
            if usr_count_email == 1:
                print("\nExisting email in use!")
                t.sleep(1)
            else:
                print("\nUser name have been taken")
                t.sleep(1)

            return False

        else:
            ## MONGO QUERY ##
            today = dt.datetime.today()
            count = getCounter()
            salt, u_pw_h = hash_new_password(pw)
            newUser = {"Account_Id": count, 'Date_Registered': today,
                       'Name': usrname,
                       'Bank_Name': bk,
                       'Password': u_pw_h,
                       'Salt': salt,
                       'Email': usremail,
                       }
            # Inserting into the DB.
            user_data.insert_one(newUser)

            print('Successfully registered! Returning to main menu!\n')
            t.sleep(1)

            return True

    except:
        print("Error occurred while registering, please try again!\n")

    return 0
