#!/usr/bin/python3
"""Creates a table named states with id and name as columns"""

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
database_url = 'mysql+mysqlconnector://denis:8904Jack@localhost:3306/hbtn_0e_6_usa'

class State(Base):
    """Defines a state

    Args:
        Base (class): declarative_base class
    """
    __tablename__ = "states"

    id = Column("id", Integer, default=11, primary_key=True, autoincrement=True, nullable=False)
    name = Column("name", String(128), nullable=False)

    def __init__(self, id, name):
        """Constructor to initialize name and id

        Args:
            id (int): id of the state
            name (str): name of the state
        """
        self.id = id
        self.name = name

engine = create_engine(database_url, echo=True)
