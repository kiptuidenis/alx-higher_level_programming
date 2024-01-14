#!/usr/bin/python3
"""Prints all cities in the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    database_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.\
        format(sys.argv[1], sys.argv[2], sys.argv[3])
    
    engine = create_engine(database_url)
    session = Session(engine)

    cities = session.query(State, City).join(City).order_by(City.id).all()    
    for state, city in cities:
        print(f"{state.name}: ({city.id}) {city.name}")