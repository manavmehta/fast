"""
    main file: entry point for the app
"""

from fastapi import FastAPI, Request
import db

app = FastAPI()


@app.get("/get-all-customers")
async def get_all_customers():
    """
        Returns all customers
    """
    return db.get_all_customers()


@app.get("/get-customer/{customer_number}")
async def get_customer(customer_number: int):
    """
        Returns the customer with the specified customer number
    """
    return db.get_customer(customer_number)


@app.put("/update-customer/{customer_number}")
async def update_customer(customer_number: int, request: Request):
    """
        Updates customer record that matches specified customer number
    """
    body = await request.json()
    return db.update_customer(customer_number, body)
