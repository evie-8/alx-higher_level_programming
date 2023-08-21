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
    state1 = session.query(State).filter(State.id == 1).first()
    if state1:
        print(f"1: {state1.name}")
    else:
        print("Nothing")
    session.close()
