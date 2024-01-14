#!/usr/bin/python3
"""Creates a table named states with id and name as columns"""

from sqlalchemy import Column, String, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base


mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)

class State(Base):
    """Defines a state

    Args:
        Base (class): declarative_base class
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
