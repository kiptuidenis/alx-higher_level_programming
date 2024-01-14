#!/usr/bin/python3
"""Changes the name of state """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    database_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.\
        format(sys.argv[1], sys.argv[2], sys.argv[3])

    engine = create_engine(database_url)
    session = Session(engine)

    state_to_update = session.query(State).filter(State.id == 2).\
        first()

    state_to_update.name = 'New Mexico'
    session.commit()

    session.close()
