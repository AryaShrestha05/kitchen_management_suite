"""
File: recipe.py
File-Path: src/db/schema/recipes.py
Author: Rohan Plante, Thomas Bruce
Date-Created: 09-29-2025

Description:
    SQLAlchemy ORM model for the Recipe entity ('Recipes' table).

Inputs:
    SQLAlchemy types/relationship helpers and the declarative Base
    and other ORM models (Household, User)

Outputs:
    The mapped `Recipe` class usable with SQLAlchemy sessions and __repr__ for debug
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from db.server import Base

class Recipe(Base):
    """class for the recipe table"""
    __tablename__ = 'Recipes'

    RecipeID = Column(Integer, primary_key = True, autoincrement=True) # default to increment, change once ID format is decided
    RecipeBody = Column(JSONB)
    RecipeName = Column(String(40))

    users = relationship("User", secondary="Authors", back_populates="recipes")
    households = relationship("Household", secondary="HouseholdRecipes", back_populates="recipes")

    def __repr__(self):
        return f"""
        RECIPE NAME: {self.RecipeName}
        """
