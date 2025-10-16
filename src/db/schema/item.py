"""
File: item.py
File-Path: src/db/schema/.py
Author: Rohan Plante
Date-Created: 10-14-2025

Description:
    SQLAlchemy ORM model for the Item entity ('Items' table).

Inputs:
    SQLAlchemy types/relationship helpers and the declarative Base
    and other ORM models (Pantry, User)

Outputs:
    The mapped `Item` class usable with SQLAlchemy sessions and __repr__ for debug
"""

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from db.server import Base

class Item(Base):
    __tablename__ = 'Items'

    ItemID = Column(Integer, primary_key = True, autoincrement=True)
    ItemName = Column(String(100))
    Quantity = Column(Integer)
    ItemInDate = Column(Date)

    adds = relationship("Add", back_populates="items")
    users = relationship("User", secondary="Adds", viewonly=True)

    contains = relationship("Contain", back_populates="items")
    pantries = relationship("Pantry", secondary="Contains", viewonly=True)

    def __repr__(self):
        return f"""
        ITEM NAME: {self.ItemName}, QUANTITY: {self.Quantity}, DATE ADDED: {self.ItemInDate}
        """