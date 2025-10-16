"""
File: role.py
File-Path: src/db/schema/role.py
Author: Rohan Plante
Date-Created: 10-15-2025

Description:
    SQLAlchemy ORM model for the Role entity ("Role" table).
    Table contains RoleID & Role Name

Inputs:
    SQLAlchemy types/relationship helpers and the declarative Base

Outputs:
    The mapped `Role` class usable with SQLAlchemy sessions and __repr__ for debug
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.server import Base

class Role(Base):
    __tablename__ = "Roles"
    RoleID = Column(Integer, primary_key=True, autoincrement=True)
    RoleName = Column(String(30))

    # relationships
    members = relationship("Member", back_populates="roles")

    def __repr__(self):
        return f"""
        RoleID: {self.RoleID} RoleName: {self.RoleName}
        """