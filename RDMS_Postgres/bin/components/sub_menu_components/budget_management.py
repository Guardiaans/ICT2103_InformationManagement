from components.dbconnection import category, budget, user, session
import inquirer as iq
import components.utils as ut
import sqlalchemy
from sqlalchemy import *

# CREATE BUDGET FUNCTION
def createBudget(categoryInsert, user_profile):
    uID = user_profile.id
    print("Creating budget here: ")
    stmt2 = text("SELECT category.category_id "
                    "FROM category "
                    "WHERE category.category_name=:categoryName "
                    "AND category.account_id =:user_id")
    stmt2 = stmt2.bindparams(categoryName=categoryInsert, user_id=uID)
    results2 = session.query(
        category.c.category_id).from_statement(stmt2).all()
    for i in results2:
        catID = (str(i.category_id))

    budgetAmount = input("Enter budget amount: ")
    monthInsert = input("Enter month number: ")
    yearInsert = input("Enter year: ")
    descInsert = input("Enter description: ")

    stmt4 = text(
        "INSERT INTO budget (budget_amount, month, year, category_id, account_id, description, actual_spent) "
        "VALUES (:budget_amount, :month, :year, :categoryID, :userID, :description, :actual_spent)")
    stmt4 = stmt4.bindparams(budget_amount=budgetAmount, month=monthInsert, year=yearInsert,
                             categoryID=catID, userID=uID, description=descInsert, actual_spent=0)
    session.execute(stmt4)
    session.commit()
    print("Budget is successfully created")
    return None


# DELETE BUDGET FUNCTION
def deleteBudget(user_profile):
    uID = user_profile.id
    bID = input("Please enter the budget ID of budget that you wish to delete: ")
    stmt = text("SELECT budget_id "
                "FROM budget "
                "WHERE b.account_id=:accID AND budget_id=:budID")
    stmt = stmt.columns(budget.c.budget_id)
    stmt = stmt.bindparams(accID=uID, budID=bID)
    results = session.query(budget.c.budget_id).from_statement(stmt).all()
    if results:
        stmt1 = text("DELETE FROM budget "
                     "WHERE b.account_id=:accID AND budget_id=:bID")
        stmt1 = stmt1.bindparams(accID=uID, budID=bID)
        session.execute(stmt1)
        session.commit()
        print("Budget successfully deleted")
    else:
        print("Budget does not exist")
        return None
    return None


# CHECK CATEGORY NAME IF EXIST FUNCTION
def checkCatName(user_profile):
    uID = user_profile.id
    categoryInsert = input("Enter category name: ")
    # check if category exist
    stmt1 = text("SELECT category.category_name "
                 "FROM category "
                 "WHERE category.category_name=:categoryName "
                 "AND category.account_id=:user_id")
    stmt1 = stmt1.columns(category.c.category_name)
    stmt1 = stmt1.bindparams(categoryName=categoryInsert, user_id=uID)
    results = session.query(
        category.c.category_name).from_statement(stmt1).all()
    if results:
        createBudget(categoryInsert, user_profile)
    else:
        print("Category does not exists")
        return None