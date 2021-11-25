from components.dbconnection import budget

# VIEW BUDGET FUNCTION
def viewBudget(user_profile):
    try:
        name = user_profile.name
        results = budget.find({ "name": name },
                              { "_id": 0, "budget_amount": 1, "description": 1, "actual_spent": 1, "month": 1, "year": 1 })
        print("\n{:<20}{:<20}{:<10}{:<10}{:<100}".format("budget_amount", "actual_spent", "month", "year", "description"))
        print(
            "____________________________________________________________________________________________________________________________________________")
        for i in results:
            print("${:<19}${:<19}{:<10}{:<10}{:<100}".format(i["budget_amount"], i["actual_spent"], i["month"], i["year"],
                                                             i["description"]))

    except:
        print("Error has occurred!")