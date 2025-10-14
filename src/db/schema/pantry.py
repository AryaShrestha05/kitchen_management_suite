"""
File: pantry.py
File-Path: src/db/schema/pantry.py
Author: Rohan Plante
Date-Created: 10-14-2025

Description:
    SQLAlchemy ORM model for the Recipe entity ('Recipes' table).

Inputs:
    SQLAlchemy types/relationship helpers and the declarative Base
    and other ORM models (Household, User)

Outputs:
    The mapped `Recipe` class usable with SQLAlchemy sessions and __repr__ for debug
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.server import Base

class Pantry(Base):
    __tablename__ = "Pantries"

    PantryID = Column(Integer, primary_key = True, autoincrement=True)
    PantryName = Column(String(100))

    households = relationship("Household", secondary="Owns", back_populates="pantries")
    items = relationship("Items", secondary="Contains", back_populates="pantries")

    def __repr__(self):
        return f"""
        PANTRY NAME: {self.PantryName}
        """