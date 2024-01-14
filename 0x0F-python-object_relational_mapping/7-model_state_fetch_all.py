#!/usr/bin/python3
"""This script lists all state objects from the database"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

if __name__== "__main__":
    # Define the database URL
    database_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format\
                           (sys.argv[1], sys.argv[2], sys.argv[3])
    # create an engine
    engine = create_engine(database_url, pool_pre_ping=True)

    # create a session
    session = Session(engine)

    # specify columns you want to retrieve
    columns = [State.id, State.name]

    # build a select statement
    query = select(*columns)

    # Execute the query and fetch the results
    rows = session.execute(query).fetchall()

    # Display the results
    for row in rows:
        print("{}: {}".format(row.id, row.name))
