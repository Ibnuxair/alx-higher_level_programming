#!/usr/bin/python3

"""
This script prints all City objects from the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: python3 14-model_city_fetch_by_state.py "
            "<username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        f'mysql://{username}:{password}@localhost:3306/{db_name}')
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(State, City).join(
        City, State.id == City.state_id).order_by(City.id).all()

    for state, city in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
