from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pymysql
import models
import utils


username, password, host, port = utils.get_credentials()

DB_URL = "mysql+pymysql://{username}:{pwd}@{host}:{port}/classicmodels".format(username=username, pwd=password, host=host, port=port)

engine = create_engine(DB_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# connection = pymysql.connect(
#     host=host,
#     port=port,
#     user=username,
#     password=password,
#     db="classicmodels")

def get_customers():
    with Session() as session:
        customers = session.query(models.Customer).all()

    return customers