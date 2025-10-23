"""
File: authors.py
File-Path: src/db/schema/authors.py
Author: Rohan Plante
Date-Created: 10-14-2025

Description:
    SQLAlchemy ORM model for the Author relationship ("Author" table).
    Junction table connecting Users to Recipes

Inputs:
    SQLAlchemy types/relationship helpers and the declarative Base
    and other ORM models (User, Recipe)

Outputs:
    The mapped `Author` class usable with SQLAlchemy sessions and __repr__ for debug
"""

from sqlalchemy import Column, Integer, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.server import Base

class Authors(Base):
    """class for the authors junction table for User-Household-Recipe relationship"""
    __tablename__ = "Authors"

    AuthorsID = Column(Integer, primary_key=True, autoincrement=True)
    UserID = Column(Integer, ForeignKey("Users.UserID"), nullable=False)
    HouseholdID = Column(Integer, ForeignKey("Households.HouseholdID"), nullable=False)
    RecipeID = Column(Integer, ForeignKey("Recipes.RecipeID"), nullable=False)
    DateAdded = Column(Date)
    IsCustom = Column(Boolean, default=False)  # true if recipe is custom to this household/user

    # relationships
    user = relationship("User", back_populates="authors")
    household = relationship("Household", back_populates="authors")
    recipe = relationship("Recipe", back_populates="authors")

    def __repr__(self):
        return f"AUTHORS: UserID {self.UserID} authored RecipeID {self.RecipeID} in HouseholdID {self.HouseholdID}"