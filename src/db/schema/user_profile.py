"""
File: user_profile.py
File-Path: src/db/schema/user_profile.py
Author: Rohan Plante
Date-Created: 10/23/2025

Description:
    SQLAlchemy ORM model for the UserProfile entity ('UserProfiles' table).
    Each user has exactly one profile with health and dietary information.

Inputs:
    SQLAlchemy types/relationship helpers and the declarative Base

Outputs:
    The mapped `UserProfile` class usable with SQLAlchemy sessions and __repr__ for debug
"""

from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from db.server import Base

class UserProfile(Base):
    """class for the user profile table"""
    __tablename__ = 'UserProfiles'

    ProfileID = Column(Integer, primary_key=True, autoincrement=True)
    UserID = Column(Integer, ForeignKey('Users.UserID'), unique=True, nullable=False)
    Height = Column(Float)  # in cm or inches
    Weight = Column(Float)  # in kg or lbs
    CalorieGoal = Column(Integer)
    DietaryPreferences = Column(String(255))  # e.g., "vegetarian, low-carb"
    Allergies = Column(String(255))  # e.g., "peanuts, shellfish"

    # relationship
    user = relationship("User", back_populates="profile")

    def __repr__(self):
        return f"PROFILE for UserID: {self.UserID}, CalorieGoal: {self.CalorieGoal}"