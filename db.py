"""
    db file: operations related to DB
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.customer import Customer
import models.standard as structs
import utils.utils as utils

username, password, host, port = utils.get_credentials()

DB_URL = (
    "mysql+pymysql://"
    f"{username}:{password}"
    f"@{host}:{port}/classicmodels"
)


# create engine connection to the mysql DB
engine = create_engine(DB_URL)

#create a sessionmaker to manage database sessions
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_all_customers():
    """
    fetches all customers
    """

    with Session() as session:
        customers = session.query(Customer).all()

    return customers

def get_customer(customer_number: int):
    """
    fetches the customer with the specified customer number
    """

    with Session() as session:
        customer = session.query(Customer).filter_by(customerNumber=customer_number).first()

    return customer

def update_customer(customer_number: int, body: dict):
    """
    updates the customer record with the specified customer number
    """

    with Session() as session:
        customer = session.query(Customer).filter_by(customerNumber=customer_number).first()

        response = structs.Response()
        response.status = "failure"
        response.message = "Record not found"
        if customer is not None:
            customer.update(body)
            session.commit()
            response.status = "success"
            response.message = "Record updated"

    return response
