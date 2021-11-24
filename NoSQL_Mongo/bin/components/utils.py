import os
import time as t
from time import sleep
from sqlalchemy.sql.sqltypes import NullType
from components.dbconnection import user_data

# class User(Base):
#     __tablename__ = 'user_detail'

#     account_id = Column(Integer, primary_key=True)
#     date_registered = Column(Date)
#     name = Column(String(50))
#     bank_name = Column(String(50))
#     password = Column(String(20))
#     balance = Column(NullType)
#     email = Column(String(50))


class UserProfile:
    def __init__(self, usrid, name, reg_date, bk, bal, email):
        self.id = usrid
        self.name = name
        self.registered = reg_date
        self.bank = bk
        self.balance = bal
        self.email = email


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')


def getUserProfile(email_input):

    ## MONGODB QUERY ##
    profile = {}
    myquery = {"Email": {'$exists': 'true', '$eq': email_input}}
    cur = user_data.find(myquery)
    for x in cur:
        profile = x

    account_id = profile['Account_Id']
    account_registered_date = profile['Date_Registered']
    account_name = profile['Name']
    account_bank = profile['Bank_Name']
    account_balance = profile['Balance']
    account_email = email_input

    verified_usr = UserProfile(account_id, account_name, account_registered_date,
                               account_bank, account_balance, account_email)

    return verified_usr
