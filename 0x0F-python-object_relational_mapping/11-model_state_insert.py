#!/usr/bin/python3
"""Adds a row to the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    database_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.\
        format(sys.argv[1], sys.argv[2], sys.argv[3])

    engine = create_engine(database_url)
    session = Session(engine)

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    columns = [State.id]
    query = session.query(*columns).order_by(State.id.desc())
    rows = query.first()
    print(rows[0])
    session.close()
