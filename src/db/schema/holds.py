"""
File: holds.py
File-Path: src/db/schema/holds.py
Author: Rohan Plante
Date-Created: 10-16-2025

Description:
    SQLAlchemy ORM model for the Holds relationship ("Holds" table).
    Junction table connecting Households with Recipes they use or save.
    Enables both global (shared) and custom recipes to appear in a household's collection.

Inputs:
    SQLAlchemy types/relationship helpers and the declarative Base
    and other ORM models (Household, Recipe)

Outputs:
    The mapped `Holds` class usable with SQLAlchemy sessions and __repr__ for debug
"""

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.server import Base

class Holds(Base):
    """class for the holds junction table for Household-Recipe relationship"""
    __tablename__ = "Holds"

    HoldsID = Column(Integer, primary_key=True, autoincrement=True)
    HouseholdID = Column(Integer, ForeignKey("Households.HouseholdID"), nullable=False)
    RecipeID = Column(Integer, ForeignKey("Recipes.RecipeID"), nullable=False)

    # relationships
    household = relationship("Household", back_populates="holds")
    recipe = relationship("Recipe", back_populates="holds")

    def __repr__(self):
        return f"""
        HOLDS: HouseholdID {self.HouseholdID} holds RecipeID {self.RecipeID}
        """