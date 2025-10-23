"""
File: recipe.py
File-Path: src/db/schema/recipe.py
Author: Rohan Plante, Thomas Bruce
Date-Created: 09-29-2025

Description:
    SQLAlchemy ORM model for the Recipe entity ('Recipes' table).
    Recipes can be global (from Fathub dataset) or custom.

Inputs:
    SQLAlchemy types/relationship helpers and the declarative Base
    and other ORM models (Household, User)

Outputs:
    The mapped `Recipe` class usable with SQLAlchemy sessions and __repr__ for debug
"""
from sqlalchemy import Column, Integer, String, Boolean, JSON
from sqlalchemy.orm import relationship
from db.server import Base

class Recipe(Base):
    """class for the recipe table"""
    __tablename__ = 'Recipes'

    RecipeID = Column(Integer, primary_key=True, autoincrement=True)
    RecipeName = Column(String(100), nullable=False)
    RecipeBody = Column(JSON)  # JSON containing ingredients, instructions, etc.
    Source = Column(String(50))  # e.g., "fathub", "custom"
    IsGlobal = Column(Boolean, default=False)  # true if from Fathub dataset

    # relationships
    authors = relationship("Authors", back_populates="recipe")
    holds = relationship("Holds", back_populates="recipe")
    
    users = relationship("User", secondary="Authors", viewonly=True)
    households = relationship("Household", secondary="Holds", viewonly=True)

    def __repr__(self):
        return f"""
        RECIPE NAME: {self.RecipeName}
        """
