from components.dbconnection import budget
from bson.objectid import ObjectId

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
    print("\nDelete Budget here:")
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

# UPDATE ACTUAL SPENT IN BUDGET FUNCTION
def updateBudget(user_profile):
    print("\nUpdate actual spent of budget here:")
    name = user_profile.name
    results = budget.find({ "name": name },
                          { "_id": 1, "budget_amount": 1, "description": 1, "actual_spent": 1, "month": 1,
                            "year": 1 })
    print(
        "\n{:<30}{:<20}{:<20}{:<10}{:<10}{:<100}".format("id", "budget_amount", "actual_spent", "month", "year",
                                                        "description"))
    print(
        "____________________________________________________________________________________________________________________________________________")
    for i in results:
        print(
            "{:<30}${:<19}${:<19}{:<10}{:<10}{:<100}".format(str(i["_id"]), i["budget_amount"], i["actual_spent"], i["month"],
                                                            i["year"],
                                                            i["description"]))
    try:
        id = input("\n\nEnter the ID of budget you wish to update: ")
        actualSpent = int(input("Enter the new actual spent: "))
        budget.update_one({"_id":ObjectId(id)},{"$set":{"actual_spent":actualSpent}})
        print("Budget updated successfully")
    except:
        print("An Error has occurred!")
    return None