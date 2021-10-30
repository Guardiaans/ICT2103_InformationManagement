from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import psycopg2
import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker

Base = automap_base()
engine = create_engine('postgresql+psycopg2://bfcyvcjpoysvfm:2d577da4f1484cea46199f86a766e69fc14c6323e655828e032e2e1cdc8d5ed6@ec2-34-200-161-87.compute-1.amazonaws.com:5432/dcr1h5psuc7lvu')
# print(engine.table_names())
Session = sessionmaker(bind=engine)
session = Session()
Base.prepare(engine, reflect=True)

## map python class to database table
User = Base.classes.user_detail

u1 = session.query(User).first()
print(u1.name)
email = "aym@gmail.com"
password = "password123"
sql_query = session.query(User).from_statement(sqlalchemy.text("SELECT * FROM user_detail WHERE email =:n")).params(n=email)
print(sql_query.first().password)


