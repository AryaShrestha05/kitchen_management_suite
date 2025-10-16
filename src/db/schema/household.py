"""
File: household.py
File-Path: src/db/schema/household.py
Author: Rohan Plante, Thomas Bruce
Date-Created: 09-30-2025

Description:
    SQLAlchemy ORM model for the Household entity ('Households' table).

Inputs:
    SQLAlchemy types/relationship helpers and the declarative Base
    and other ORM models (Recipe, User)

Outputs:
    The mapped `Household` class usable with SQLAlchemy sessions and __repr__ for debug
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.server import Base

class Household(Base):
    """class for the household table"""
    __tablename__ = 'Households'

    HouseholdID = Column(Integer, primary_key=True, autoincrement=True)  # TODO: deal with UUIDv4
    HouseholdName = Column(String(100))

    # relationships
    members = relationship("Member", back_populates="households")
    users = relationship("User", secondary="Members", viewonly=True)

    holds = relationship("Hold", back_populates="households")
    recipes = relationship("Recipe", secondary="Holds", viewonly=True)

    owns = relationship("Own", back_populates="household")
    pantries = relationship("Pantry", secondary="Owns", viewonly=True)
    
    def __repr__(self):
        return f"""
        HOUSEHOLD: {self.HouseholdName} (ID: {self.HouseholdID})
        """
