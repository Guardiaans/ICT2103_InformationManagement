from components.dbconnection import category, budget, user, session
import inquirer as iq
import components.utils as ut
import sqlalchemy as sq
def viewBudget(user_profile):
    email=user_profile.email
    #TODO: Implement view budget Method()
    stmt = sq.text("SELECT b.budget_id, b.budget_amount, b.month, b.year, b.description "
                   ", b.actual_spent, c.category_name FROM budget b, user_detail u, category c "
                   "WHERE b.account_id = u.account_id AND c.category_id = b.category_id "
                   "AND u.email=:email")
    stmt = stmt.columns(budget.c.budget_id, budget.c.budget_amount, budget.c.month,
                        budget.c.year, budget.c.description, budget.c.actual_spent, category.c.category_name)
    stmt = stmt.bindparams(email=str(email))
    results = session.query(budget.c.budget_id, budget.c.budget_amount, budget.c.month,
                            budget.c.year, budget.c.description, budget.c.actual_spent
                            , category.c.category_name).from_statement(stmt).all()
    print("{:<5}{:<13}{:<12}{:<12}{:<40}{:<40}{:<5}".format("id", "amount", "month", "year", "description",
                                                            "actual spent", "category"))
    print("_________________________________________________________________________________________________________________________________________")
    for i in results:
        print("{:<5}{:<13}{:<12}{:<12}{:<40}{:<40}{:<5}".format(str(i.budget_id), str(i.budget_amount),
                                                                str(i.month), str(i.year),
                                                                str(i.description), str(i.actual_spent),
                                                                str(i.category_name)))
    menuoption = iq.list_input(f"Select an option",
                              choices=['Back',
                              ])
    return menuoption