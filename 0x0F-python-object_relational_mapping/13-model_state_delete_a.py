#!/usr/bin/python3
"""
This script deletes State objects with a name containing the letter 'a'

from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: ./script.py [mysql_username] "
            "[mysql_password] [database_name]")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        f'mysql://{username}:{password}@localhost:3306/{db_name}')
    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = session.query(State).filter(
        State.name.ilike('%a%')).all()

    for state in states_to_delete:
        session.delete(state)
        session.commit()

    session.close()
