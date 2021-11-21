import os
import time as t
from time import sleep
from sqlalchemy import *
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.sqltypes import NullType
from components.dbconnection import user, session


Base = declarative_base()


class User(Base):
    __tablename__ = 'user_detail'

    account_id = Column(Integer, primary_key=True)
    date_registered = Column(Date)
    name = Column(String(50))
    bank_name = Column(String(50))
    password = Column(String(20))
    balance = Column(NullType)
    email = Column(String(50))


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


def getUserProfile(email):

    stmt = text(
        f"SELECT ud.account_id, ud.date_registered, ud.name, ud.bank_name, ud.balance FROM user_detail ud WHERE ud.email = '{email}' ")
    data = stmt.columns(user.c.account_id, user.c.date_registered,
                        user.c.name, user.c.bank_name, user.c.balance)
    result = session.query(user.c.account_id, user.c.date_registered, user.c.name,
                           user.c.bank_name, user.c.balance).from_statement(data).all()

    account_id = [item[0] for item in result]
    account_registered_date = [item[1] for item in result]
    account_name = [item[2] for item in result]
    account_bank = [item[3] for item in result]
    account_balance = [item[4] for item in result]

    userID = account_id[0]
    acc_reg_date = account_registered_date[0]
    acc_name = account_name[0]
    acc_bank = account_bank[0]
    acc_bal = account_balance[0]
    acc_email = email

    verified_usr = UserProfile(userID, acc_name, acc_reg_date,
                               acc_bank, acc_bal, acc_email)

    return verified_usr
