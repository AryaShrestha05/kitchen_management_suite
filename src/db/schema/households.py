"""
File: households.py
File-Path: src/db/schema/households.py
Author: Rohan Plante
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

class Recipe(Base):
    """class for the household table"""
    __tablename__ = 'Households'

    HouseholdID = Column(Integer, primary_key = True, autoincrement=True) # default to increment, change once ID format is decided
    HouseholdName = Column(String(40))
    Members = Column(String) # use feed & .add in session to add members
                             # session.query(Households).all()/.get(1) to access

    household_recipes = relationship("HouseholdRecipe", back_populates="recipe")

    recipes = relationship("Recipe", secondary="HouseholdRecipes", viewonly=True)

def __repr__(self):
    return f"""
        HOUSEHOLD NAME: {self.HouseholdName}, MEMBERS: {self.Members}"""