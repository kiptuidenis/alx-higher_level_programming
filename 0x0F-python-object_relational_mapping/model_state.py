#!/usr/bin/python3
"""Creates a table named states with id and name as columns"""

from sqlalchemy import Column, String, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base


mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)
database_url = 'mysql+mysqlconnector://denis:8904Jack@localhost:3306/hbtn_0e_6_usa'

class State(Base):
    """Defines a state

    Args:
        Base (class): declarative_base class
    """
    __tablename__ = "states"

    id = Column(Integer, default=11, primary_key=True, unique=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, id, name):
        """Constructor to initialize name and id

        Args:
            id (int): id of the state
            name (str): name of the state
        """
        self.id = id
        self.name = name

