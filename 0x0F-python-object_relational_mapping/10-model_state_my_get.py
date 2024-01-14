#!/usr/bin/python3
"""Prints the id of a serched state"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    database_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.\
        format(sys.argv[1], sys.argv[2], sys.argv[3])

    engine = create_engine(database_url)
    session = Session(engine)

    columns = [State.id]
    name_to_search = sys.argv[4]
    query = session.query(*columns).filter(State.name == name_to_search)

    rows = query.all()
    if len(rows) == 0:
        print("Not found")
    else:
        print(rows[0][0])
