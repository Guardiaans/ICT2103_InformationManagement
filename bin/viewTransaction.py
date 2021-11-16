from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import psycopg2
import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import *
from sqlalchemy.sql import select



# Using SQLAlchemy reflection example
engine = create_engine('postgresql+psycopg2://bfcyvcjpoysvfm:2d577da4f1484cea46199f86a766e69fc14c6323e655828e032e2e1cdc8d5ed6@ec2-34-200-161-87.compute-1.amazonaws.com:5432/dcr1h5psuc7lvu')
metaData = MetaData(engine)
user = Table('user_detail', metaData, autoload=True)
category = Table('category', metaData, autoload=True)
transaction = Table('transaction_data', metaData, autoload=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()

stmt = text("SELECT t.transaction_id, t.transaction_date, t.debit_amount, t.credit_amount, t.description_1, t.description_2, c.category_name FROM transaction_data t, user_detail u, category c WHERE t.account_id = u.account_id AND c.category_id = t.category_id AND u.email='csy@gmail.com'")
stmt = stmt.columns(transaction.c.transaction_id, transaction.c.transaction_date, transaction.c.debit_amount, transaction.c.credit_amount, transaction.c.description_1, transaction.c.description_2, category.c.category_name)
results = session.query(transaction.c.transaction_id, transaction.c.transaction_date, transaction.c.debit_amount, transaction.c.credit_amount, transaction.c.description_1, transaction.c.description_2, category.c.category_name).from_statement(stmt).all()
print("{:<5}{:<13}{:<12}{:<12}{:<40}{:<40}{:<5}".format("id","date","debit", "credit", "description_1","description_2", "category"))
print("_________________________________________________________________________________________________________________________________________")
for i in results:
    print("{:<5}{:<13}{:<12}{:<12}{:<40}{:<40}{:<5}".format(str(i.transaction_id), str(i.transaction_date), str(i.debit_amount), str(i.credit_amount), str(i.description_1), str(i.description_2), str(i.category_name)))


# # Base = automap_base()
# Base = declarative_base()
# engine = create_engine('postgresql+psycopg2://bfcyvcjpoysvfm:2d577da4f1484cea46199f86a766e69fc14c6323e655828e032e2e1cdc8d5ed6@ec2-34-200-161-87.compute-1.amazonaws.com:5432/dcr1h5psuc7lvu', echo=True)
# # print(engine.table_names())
# Session = sessionmaker(bind=engine)
# session = Session()
# # Base.prepare(engine, reflect=True)
# conn = engine.connect()

# metadata_obj = MetaData()
# # Category = Table('category', metadata_obj,
# #     Column('category_id', Integer, primary_key=True),
# #     Column('category_name', String(50)),
# #     Column('account_id',Integer, ForeignKey("user_detail.account_id"))
# # )

# User = Table("user_detail", metadata_obj,
#     Column('account_id', Integer, primary_key=True),
#     Column('date_registered', Date),
#     Column('name', String(50), nullable=False),
#     Column('bank_name', String(50)),
#     Column('password', String(20), nullable=False),
#     Column('balance', Numeric),
#     Column('email', String(50), nullable=False)
# )
# Base.metadata_obj.create_all(engine)

# # s = select(User)
# # result = conn.execute(s)
# # for i in result:
# #     print(i.name)

# for t in metadata_obj.sorted_tables:
#     print(t.name)

# print(User.metadata)




# ## map python class to database table
# # User = Base.classes.user_detail
# # Transaction = Base.classes.transaction_data
# # Category = Base.classes.category

# # category = session.query(Category).first()
# # print(category.category_name)

# # u1 = session.query(User).first()
# # print(u1.name)
# # email = "aym@gmail.com"
# # password = "password123"
# # sql_query = session.query(User).from_statement(sqlalchemy.text("SELECT * FROM user_detail WHERE email =:n")).params(n=email)
# # print(sql_query.first().password)

# # sql = session.query(Transaction,Category).from_statement(sqlalchemy.text("SELECT t.transaction_id, c.category_name FROM transaction_data t JOIN category c ON t.category_id = c.category_id").columns(Transaction.transaction_id, Category.category_name)).first()
# # print(sql[Category].category_name)

# # stmt = sqlalchemy.text("SELECT t.transaction_id, c.account_id FROM transaction_data t JOIN user_detail c ON t.account_id=c.account_id").columns(Transaction.transaction_id, Category.category_name)
# # result = conn.execute(stmt)

# # for i in result:
# #     print(i.User.account_id)

# # email = 'csy@gmail.com'
# # sql_query = session.query(Transaction, Category, User).from_statement(sqlalchemy.text(
# "SELECT t.transaction_id, t.debit_amount, c.category_name FROM transaction_data t, user_detail u, category c WHERE t.account_id = u.account_id AND c.category_id = t.category_id AND u.email='csy@gmail.com'"))
# # print("id   trans_date   debit   credit   description_1                 description_2                     category_id  account_id")
# # for i in sql_query:
# #     print("{:<5}{:<13}{:<8}{:<16}{:<30}{:<34}{:<5}{:<5}".format(str(i.Transaction.transaction_id), str(i.Transaction.transaction_date), str(i.Transaction.debit_amount), str(i.Transaction.credit_amount), str(i.Transaction.description_1), str(i.Transaction.description_2), str(i.Transaction.category_id)))