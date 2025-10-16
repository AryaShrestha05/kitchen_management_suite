"""
File: add.py
File-Path: src/db/schema/add.py
Author: Rohan Plante
Date-Created: 10-15-2025

Description:
    SQLAlchemy ORM model for the Author relationship ("Author" table).
    Junction table connecting Users to Recipes

Inputs:
    SQLAlchemy types/relationship helpers and the declarative Base
    and other ORM models (User, Recipe)

Outputs:
    The mapped `Author` class usable with SQLAlchemy sessions and __repr__ for debug
"""

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.server import Base

class Add(Base):
    __tablename__ = "Adds"

    UserID = Column(Integer, ForeignKey("Users.UserID"), primary_key=True)
    ItemID = Column(Integer, ForeignKey("Items.ItemID"), primary_key=True)

    users = relationship("User", back_populates="adds")
    items = relationship("Item", back_populates="adds")

    def __repr__(self):
        return f"""
        Item ID: {self.ItemID} ADDED BY User ID: {self.UserID}
        """