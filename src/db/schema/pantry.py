"""
File: pantry.py
File-Path: src/db/schema/pantry.py
Author: Rohan Plante
Date-Created: 10-14-2025

Description:
    SQLAlchemy ORM model for the Pantry entity ('Pantries' table).
    Each household has exactly one pantry.

Inputs:
    SQLAlchemy types/relationship helpers and the declarative Base
    and other ORM models (Household, Item)

Outputs:
    The mapped `Pantry` class usable with SQLAlchemy sessions and __repr__ for debug
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.server import Base

class Pantry(Base):
    """class for the pantry table"""
    __tablename__ = "Pantries"

    PantryID = Column(Integer, primary_key=True, autoincrement=True)
    HouseholdID = Column(Integer, ForeignKey('Households.HouseholdID'), unique=True, nullable=False)
    PantryName = Column(String(100))

    # relationships
    household = relationship("Household", back_populates="pantry")
    adds = relationship("Adds", back_populates="pantry")
    
    items = relationship("Item", secondary="Adds", viewonly=True)

    def __repr__(self):
        return f"""
        PANTRY NAME: {self.PantryName} Belongs to HOUSEHOLD: {self.HouseholdID}
        """