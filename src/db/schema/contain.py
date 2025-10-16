"""
File: contain.py
File-Path:src/db/schema/contain.py
Author: Rohan Plante
Date-Created: 10-16-2025

Description:

Inputs:

Outputs:

"""
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.server import Base

class Contain(Base):
    __tablename__ = "Contains"

    PantryID = Column(Integer, ForeignKey("Pantries.PantryID"), primary_key=True)
    ItemID = Column(Integer, ForeignKey("Items.ItemID"), primary_key=True)

    pantries = relationship("Pantry", back_populates="contains")
    items = relationship("Item", back_populates="contains")

    def __repr__(self):
        return f"""
        Item ID: {self.ItemID} contained in Pantry ID: {self.PantryID}
        """