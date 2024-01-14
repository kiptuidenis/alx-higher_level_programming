#!/usr/bin/python3
"""Contains class definition of a city"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """Defines a city

    Args:
        Base (class): declarative base class
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
