"""
File: author.py
File-Path: src/db/schema/author.py
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

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.server import Base

class Author(Base):
    """class for the author junction table for many to many User to Recipe"""
    __tablename__ = "Authors"

    UserID = Column(Integer, ForeignKey("Users.UserID"), primary_key=True)
    RecipeID = Column(Integer, ForeignKey("Recipes.RecipeID"), primary_key=True)

    users = relationship("User", back_populates="authors")
    recipes = relationship("Recipe", back_populates="authors")

    def __repr__(self):
        return f"""
        USER: {self.UserID} AUTHORED RECIPE: {self.RecipeID}
        """