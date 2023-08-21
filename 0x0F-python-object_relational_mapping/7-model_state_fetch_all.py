#!/usr/bin/python3
'''fetching all datausing sqlalchemy'''


import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    i = 1
    for state in session.query(State).order_by(State.id):
        print(f"{i}: {state.name}")
        i = i + 1
    session.close()
