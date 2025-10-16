"""
File: own.py
File-Path:src/db/schema/own.py
Author: Rohan Plante
Date-Created: 10-16-2025

Description:

Inputs:

Outputs:

"""
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.server import Base

class Own(Base):
    __tablename__ = "Owns"
    
    HouseholdID = Column(Integer, ForeignKey("Households.HouseholdID"), primary_key=True)
    PantryID = Column(Integer, ForeignKey("Pantries.PantryID"), primary_key=True)

    household = relationship("Household", back_populates="owns")
    pantry = relationship("Pantry", back_populates="owns")

    def __repr__(self):
        return f"""
        OWN: Household {self.HouseholdID} owns Pantry {self.PantryID}
        """
