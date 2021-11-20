from components.dbconnection import *
import inquirer as iq

def transaction_table():
    print("viewing transaction table")
    year = iq.text(message="Enter a year <2021>")
    month = iq.text(message="Enter a month <10>")
    email="csy@gmail.com"
    stmt = text("SELECT t.transaction_id, t.transaction_date, t.debit_amount, " +
                "t.credit_amount, t.description_1, t.description_2, c.category_name " +
                " FROM transaction_data t, user_detail u, category c "+
                "WHERE t.account_id = u.account_id AND c.category_id = t.category_id " + 
                " AND u.email=:email AND CAST(t.transaction_date as character varying(50)) LIKE ':year-:month-%'") 
    stmt = stmt.columns(transaction.c.transaction_id, transaction.c.transaction_date, transaction.c.debit_amount, transaction.c.credit_amount, transaction.c.description_1, transaction.c.description_2, category.c.category_name)
    stmt = stmt.bindparams(year=int(year), month=int(month), email=email)
    results = session.query(transaction.c.transaction_id, transaction.c.transaction_date, transaction.c.debit_amount, transaction.c.credit_amount, transaction.c.description_1, transaction.c.description_2, category.c.category_name).from_statement(stmt).all()
    print("{:<5}{:<13}{:<12}{:<12}{:<40}{:<40}{:<5}".format("id","date","debit", "credit", "description_1","description_2", "category"))
    print("_________________________________________________________________________________________________________________________________________")
    for i in results:
        print("{:<5}{:<13}{:<12}{:<12}{:<40}{:<40}{:<5}".format(str(i.transaction_id), str(i.transaction_date), str(i.debit_amount), str(i.credit_amount), str(i.description_1), str(i.description_2), str(i.category_name)))
    return
