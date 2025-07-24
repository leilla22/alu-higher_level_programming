#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa."""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # DB connection setup
    username, password, db_name = argv[1], argv[2], argv[3]
    db_url = f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}'

    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying and displaying cities with their states
    results = session.query(City, State).join(State).order_by(City.id).all()

    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")
