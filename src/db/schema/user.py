"""
File: user.py
File-Path: src/db/schema/user.py
Author: Thomas Bruce, Rohan Plante
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
    FirstName = Column(String(50))
    LastName = Column(String(50))
    Username = Column(String(50), unique=True)
    Email = Column(String(100), unique=True)
    DateOfBirth = Column(Date)
    Password = Column(String(255))

    # relationships
    authors = relationship("Author", back_populates="users")
    recipes = relationship("Recipe", secondary="Authors", viewonly=True)

    members = relationship("Member", back_populates="users")
    households = relationship("Household", secondary="Members", viewonly=True)
    
    adds = relationship("Add", back_populates="users")
    items = relationship("Item", secondary="Adds", back_populates=True)


    def __repr__(self):
        return f"""
        USER: {self.Username}, NAME: {self.Name}, EMAIL: {self.Email}
        """
