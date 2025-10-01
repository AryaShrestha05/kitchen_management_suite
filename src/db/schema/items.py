"""
File: items.py
File-Path: src/db/schema/items.py
Author: Noah Yurasko
Date-Created 10/1/2025

Description:
    ORM model for item entity (table holding all items currently in pantry)

Inputs:
    SQL Alchemy Declarative Base + .env + postgres connection

Outputs:
    Items class ready for use in SQL Alchemy ORM models
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.server import Base

class Items(Base):
    """ Items Class"""
    __tablename__ = "Items"

    ItemId = Column(Integer, autoincrement=True, primary_key = True)
    ItemName = Column(String(40))
    Owner = Column(String(40))
    Quantity = Column(String(40))
    ItemInDate = Column(String(40))

    household_items = relationship("HouseholdItems", back_propogate = "items")
    household = relationship("Household", secondary="HouseholdItems", viewonly=True)

    def __repr__(self):
        return(f"""
            ItemName: {self.ItemName} | Item Quantity {self.Quantity} | Owner{self.Owner}
              """)