from components.dbconnection import budget

# CREATE BUDGET FUNCTION
def createBudget(user_profile):
    print("\nCreate Budget here:")
    try:
        id = user_profile.id
        name = user_profile.name
        budgetAmount = int(input("Enter budget amount: "))
        month = int(input("Enter month number: "))
        year = int(input("Enter year in YYYY: "))
        catName = input("Enter category name: ")
        desc = input("Enter description: ")
        actualSpent = int(input("Enter actual spent: "))
        bankName = user_profile.bank
        email = user_profile.email
        date = user_profile.registered
        mydict = {"budget_amount":budgetAmount,"month":month,"year":year,"category_name":catName,"description":desc,
                  "actual_spent":actualSpent,"date_registered":date,"name":name,
                  "bank_name":bankName,"email":email,"category_created_by":name,"account_id":id}
        budget.insert_one(mydict)
        print("Budget successfully inserted")
    except:
        print("Budget unsuccessfully inserted")
    return None


# DELETE BUDGET FUNCTION
def deleteBudget(user_profile):
    try:
        budgetAmount = int(input("\nEnter budget amount: "))
        month = int(input("Enter month number: "))
        year = int(input("Enter year in YYYY: "))
        catName = input("Enter category name: ")
        desc = input("Enter description: ")
        accountID = user_profile.id
        mydict = { "budget_amount": budgetAmount, "month": month, "year": year, "category_name": catName,
                   "description": desc,
                   "account_id": accountID }
        budget.delete_one(mydict)
        print("Budget successfully deleted")
    except:
        print("Budget unsuccessfully deleted")
    return None