"""
File: member.py
File-Path: src/db/schema/member.py
Author: Thomas Bruce, Rohan Plante
Date-Created: 09-30-2025

Description:
    SQLAlchemy ORM model for the Member relationship ('Members' table).
    Junction table connecting Users to Households with role information.

Inputs:
    SQLAlchemy types/relationship helpers and the declarative Base
    and other ORM models (User, Household)

Outputs:
    The mapped `Member` class usable with SQLAlchemy sessions and __repr__ for debug
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.server import Base

class Member(Base):
    """class for the member junction table"""
    __tablename__ = 'Members'

    Member_ID = Column(Integer, primary_key=True, autoincrement=True)
    UserID = Column(Integer, ForeignKey('Users.UserID'))
    HouseholdID = Column(Integer, ForeignKey('Households.HouseholdID'))
    RoleID = Column(Integer, ForeignKey("Roles.RoleID"))

    # relationships
    users = relationship("User", back_populates="members")
    households = relationship("Household", back_populates="members")
    roles = relationship("Role", back_populates="members")

    def __repr__(self):
        return f"""
        MEMBER: UserID {self.UserID} in HouseholdID {self.HouseholdID}, ROLE: {self.RoleID}
        """
