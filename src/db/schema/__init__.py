"""
File: __init__.py
Author: Rohan Plante
Date-Created: 10/16/2025
"""
# import all tables (models) so they get registered with Base.metadata
from .add import Add
from .author import Author
from .contain import Contain
from .hold import Hold
from .household import Household
from .item import Item
from .member import Member
from .own import Own
from .pantry import Pantry
from .recipe import Recipe
from .role import Role
from .user import User

# make tables (models) available when importing from schema package
__all__ = ['Add', 'Author', 'Contain','Hold', 'Household', 'Item', 'Member', 'Own', 'Pantry', 'Recipe', 'Role', 'User']