"""
File: user.py
File-Path: src/db/schema/user.py
Author: Thomas Bruce
Date-Created: 09-30-2025

Description:
    SQLAlchemy ORM model for the User entity ('Users' table).

Inputs:
    SQLAlchemy types/relationship helpers and the declarative Base
    and other ORM models (Household, Recipe, Member)

Outputs:
    The mapped `User` class usable with SQLAlchemy sessions and __repr__ for debug
"""

# TODO:
# - hash all user values
# - deal with UUIDv4 for UserID

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from db.server import Base

class User(Base):
    """class for the user table"""
    __tablename__ = 'Users'

    UserID = Column(Integer, primary_key=True, autoincrement=True)  # TODO: deal with UUIDv4
    Name = Column(String(100))
    Username = Column(String(50), unique=True)
    Email = Column(String(100), unique=True)
    DateOfBirth = Column(Date)
    Password = Column(String(255))

    # relationships
    user_recipes = relationship("UserRecipe", back_populates="user")
    memberships = relationship("Member", back_populates="user")

    recipes = relationship("Recipe", secondary="UserRecipes", viewonly=True)
    households = relationship("Household", secondary="Members", viewonly=True)

    def __repr__(self):
        return f"""
        USER: {self.Username}, NAME: {self.Name}, EMAIL: {self.Email}
        """
