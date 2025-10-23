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
    and other ORM models (User, Household, Role)

Outputs:
    The mapped `Member` class usable with SQLAlchemy sessions and __repr__ for debug
"""

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.server import Base

class Member(Base):
    """class for the member junction table"""
    __tablename__ = 'Members'

    MemberID = Column(Integer, primary_key=True, autoincrement=True)
    UserID = Column(Integer, ForeignKey('Users.UserID'), nullable=False)
    HouseholdID = Column(Integer, ForeignKey('Households.HouseholdID'), nullable=False)
    RoleID = Column(Integer, ForeignKey("Roles.RoleID"), nullable=False)

    # relationships
    user = relationship("User", back_populates="members")
    household = relationship("Household", back_populates="members")
    role = relationship("Role", back_populates="members")

    def __repr__(self):
        return f"""
        MEMBER: UserID {self.UserID} in HouseholdID {self.HouseholdID}, RoleID: {self.RoleID}
        """