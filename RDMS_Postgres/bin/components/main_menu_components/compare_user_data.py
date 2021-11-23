from components.dbconnection import category, transaction,user,session
import sqlalchemy as sq
import inquirer as iq

def compareUserData(user_profile):
    #TODO: Implement method by using data from database
    #print("comparing user data")
    options = []
    stmt = sq.text("SELECT user_detail.email " + \
    "FROM user_detail ")
    stmt = stmt.columns(user.c.email)
    results = session.query(user.c.email).from_statement(stmt).all()
    for items in results:
        if items != user_profile.email:
            options.append(items[0])
    
    menuoption = iq.list_input(f"Select a user to compare with! ",
                              choices=options)

    cEmail = menuoption

    stmt = sq.text("SELECT category.category_name, SUM(transaction_data.debit_amount) " + \
    "FROM transaction_data " +\
    "JOIN category " + \
    "ON transaction_data.category_id = category.category_id " + \
    "JOIN user_detail " + \
    "ON transaction_data.account_id = user_detail.account_id " + \
    "WHERE user_detail.email=:userEmail " + \
    "GROUP BY category.category_name " + \
    "HAVING SUM(transaction_data.debit_amount) > '0' " + \
    "ORDER BY category.category_name ASC")
    stmt = stmt.columns(category.c.category_name, transaction.c.debit_amount)
    stmt = stmt.bindparams(userEmail = user_profile.email)
    results = session.query(category.c.category_name, transaction.c.debit_amount).from_statement(stmt).all()

    #printing of result
    print("User: ", user_profile.email)
    print("{:<20}{:<12}".format("Category", "Total Amount"))
    print("______________________________________________________________________")
    for i in results:
        print("{:<20}{:<12}".format(str(i.category_name), str(i.debit_amount)))
    print("\n")

    stmt2 = sq.text("SELECT category.category_name, SUM(transaction_data.debit_amount) " + \
    "FROM transaction_data " +\
    "JOIN category " + \
    "ON transaction_data.category_id = category.category_id " + \
    "JOIN user_detail " + \
    "ON transaction_data.account_id = user_detail.account_id " + \
    "WHERE user_detail.email=:compareEmail " + \
    "GROUP BY category.category_name " + \
    "HAVING SUM(transaction_data.debit_amount) > '0' " + \
    "ORDER BY category.category_name ASC")
    stmt2 = stmt2.columns(category.c.category_name, transaction.c.debit_amount)
    stmt2 = stmt2.bindparams(compareEmail = cEmail)
    results = session.query(category.c.category_name, transaction.c.debit_amount).from_statement(stmt2).all()

    #printing of result
    print("Comparison: ", cEmail)
    print("{:<20}{:<12}".format("Category", "Total Amount"))
    print("______________________________________________________________________")
    for i in results:
        print("{:<20}{:<12}".format(str(i.category_name), str(i.debit_amount)))
    print("\n")

    menuoption = iq.list_input(f"Select an option",
                                choices=['Back',
                                ])

    return menuoption