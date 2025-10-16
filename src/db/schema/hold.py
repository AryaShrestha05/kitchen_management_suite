"""
File: hold.py
File-Path:src/db/schema/hold.py
Author: Rohan Plante
Date-Created: 10-16-2025

Description:

Inputs:

Outputs:

"""
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.server import Base

class Hold(Base):
    __tablename__ = "Holds"

    HouseholdID = Column(Integer, ForeignKey("Households.HouseholdID"), primary_key=True)
    RecipeID = Column(Integer, ForeignKey("Recipes.RecipeID"), primary_key=True)

    households = relationship("Household", back_populates="holds")
    recipes = relationship("Recipe", back_populates="holds")

    def __repr__(self):
        return f"""
        Recipe ID: {self.RecipeID} HELD BY Household ID: {self.HouseholdID}
        """