#!/usr/bin/python3
"""Prints the first State object from the database"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session

if __name__ == "__main__":
    # Define the database URL
    database_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.\
    format(sys.argv[1], sys.argv[2], sys.argv[3])

    #create engine
    engine = create_engine(database_url, pool_pre_ping=True)
    
    #create session
    session = Session(engine)

    #Execute query and fetch the results
    rows = session.query(State).first()
    print(type(rows))
    #Display the results
    if rows is None:
        print("Nothing")
    else:
        print("{}: {}".format(rows.id, rows.name))
    session.close()
