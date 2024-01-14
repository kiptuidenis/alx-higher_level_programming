#!/usr/bin/python3
"""Lists all objects with letter a from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    database_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.\
        format(sys.argv[1], sys.argv[2], sys.argv[3])

    # Create engine
    engine = create_engine(database_url)

    # Create session
    session = Session(engine)

    # Create a list of columns you want to query
    columns = [State.id, State.name]

    # Create a query
    stmt = session.query(*columns).filter(State.name.like('%a%'))

    # Execute query with condition that each state retrieved has letter 'a'
    rows = stmt.all()
    # Display results
    for row in rows:
        print("{}: {}".format(row.id, row.name))
