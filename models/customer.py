"""
    Customer Model
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DECIMAL

Base = declarative_base()

class Customer(Base):
    """
        represents customer table in the DB
    """

    __tablename__ = "customers"

    customerNumber = Column(Integer, primary_key=True)
    customerName = Column(String(50), nullable=False)
    contactLastName = Column(String(50), nullable=False)
    contactFirstName = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    addressLine1 = Column(String(50), nullable=False)
    addressLine2 = Column(String(50), nullable=True)
    city = Column(String(50), nullable=False)
    state = Column(String(50), nullable=True)
    postalCode = Column(String(15), nullable=True)
    country = Column(String(50), nullable=False)
    salesRepEmployeeNumber = Column(Integer, nullable=True)
    creditLimit = Column(DECIMAL(10, 2), nullable=True)

    def update(self, body: dict):
        """
            update record in DB
        """
        for key, value in body.items():
            setattr(self, key, value)
