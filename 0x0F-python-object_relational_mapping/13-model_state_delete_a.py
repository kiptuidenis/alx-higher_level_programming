#!/usr/bin/python3
"""Deletes all states with name containing letter a"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    database_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.\
        format(sys.argv[1], sys.argv[2], sys.argv[3])

    engine = create_engine(database_url)
    session = Session(engine)

    query = session.query(State).filter(State.name.like('%a%'))
    rows = query.all()
    for row in rows:
        session.delete(row)
    session.commit()
