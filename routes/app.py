"""
    app routes file: routes defined for primary service
"""

from fastapi import APIRouter, Request
import db

appRouter = APIRouter()

@appRouter.get("/get-all-customers")
def get_all_customers():
    """
        Returns all customers
    """
    return db.get_all_customers()


@appRouter.get("/get-customer/{customer_number}")
def get_customer(customer_number: int):
    """
        Returns the customer with the specified customer number
    """
    return db.get_customer(customer_number)


@appRouter.put("/update-customer/{customer_number}")
async def update_customer(customer_number: int, request: Request):
    """
        Updates customer record that matches specified customer number
    """
    body = await request.json()
    return db.update_customer(customer_number, body)

# For the reader: https://betterprogramming.pub/fastapi-best-practices-1f0deeba4fce
