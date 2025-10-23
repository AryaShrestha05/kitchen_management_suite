"""
File: item.py
File-Path: src/db/schema/item.py
Author: Rohan Plante
Date-Created: 10-14-2025

Description:
    SQLAlchemy ORM model for the Item entity ('Items' table).
    Items can be global (from Open Food Facts) or custom.

Inputs:
    SQLAlchemy types/relationship helpers and the declarative Base
    and other ORM models (Pantry, User)

Outputs:
    The mapped `Item` class usable with SQLAlchemy sessions and __repr__ for debug
"""

from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy.orm import relationship
from db.server import Base

class Item(Base):
    """class for the item table"""
    __tablename__ = 'Items'

    ItemID = Column(Integer, primary_key=True, autoincrement=True)
    ItemName = Column(String(100), nullable=False)
    ItemBody = Column(Text)  # JSON or text description of the item
    Source = Column(String(50))  # e.g., "openfoodfacts", "custom"
    IsGlobal = Column(Boolean, default=False)  # true if from Open Food Facts

    # relationships
    adds = relationship("Adds", back_populates="item")
    
    users = relationship("User", secondary="Adds", viewonly=True)
    pantries = relationship("Pantry", secondary="Adds", viewonly=True)
    
    def __repr__(self):
        return f"""
        ITEM NAME: {self.ItemName}
        """