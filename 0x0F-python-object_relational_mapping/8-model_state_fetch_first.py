#!/usr/bin/python3
"""Prints the first State object from the database"""

import sys
from sqlalchemy import create_engine, select
from model_state import Base, State
from sqlalchemy.orm import Session

if __name__ == "__main__":
    # Define the database URL
    database_url = 'mysql+mysqldb://{}:{}@localhost/{}'.\
    format(sys.argv[1], sys.argv[2], sys.argv[3])

    #create engine
    engine = create_engine(database_url, pool_pre_ping=True)

    #create session
    session = Session(engine)

    #specify columns you want to select
    columns = [State.id, State.name]

    #build a select statement
    query = select(*columns).where(State.id == 1)

    #Execute query and fetch the results
    rows = session.execute(query).fetchall()
    if len(rows) == 0:
        print("")
    #Display the results
    for row in rows:
        print("{}: {}".format(row.id, row.name))