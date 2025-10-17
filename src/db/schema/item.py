"""
File: item.py
File-Path: src/db/schema/items.py
Author: Noah Yurasko
Date-Created: 10-29-2025

Description:
    ORM declaration of Item Table

Inputs:
    SQLAlchemy types/relationship helpers and the declarative Base
    and other ORM models (User, Household)

Outputs:
       The mapped `Member` class usable with SQLAlchemy sessions and __repr__ for debug

"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.server import Base

class Item(Base):
    """class for the items table"""
    __tablename__ = 'item'

    ItemId = Column(Integer, primary_key = True, autoincrement=True) 
    ItemName = Column(String(40))
    ItemQuantity = Column(Integer)
    ItemInDate = Column(String(40)) #We need to decide on a standard for storing datetimes
    ItemOwner = String(Integer)#Contains User ID

    pantry_items = relationship("Pantry", back_populates="item")
    household = relationship("Household", secondary="Pantry", viewonly=True)

    #If we wanated we could also do a relation between owner and the item
    # owner = relationship("User", secondary="Household?", viewonly=True)

def __repr__(self):
    return f"""
        ITEM NAME: {self.ItemName}, ITEM OWNER: {self.ItmeOwner}"""