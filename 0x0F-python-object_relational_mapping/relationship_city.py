#!/usr/bin/python3
"""
This script defines a City class
to work with MySQLAlchemy ORM
"""

from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey

class City(Base):
    """
    City class

    Attributes:
        __tablename__: The table name of the class
        id: The id of the class
        name: The name of the class
        state_id: The state, the class belongs to
    """
    __tablename__ = 'cities'

    id = Column(Integer, primarykey=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
