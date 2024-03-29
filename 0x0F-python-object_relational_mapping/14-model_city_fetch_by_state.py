#!/usr/bin/python3
'''fetching all datausing sqlalchemy'''


import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    joined = session.query(City, State).order_by(City.id).\
        join(State, City.state_id == State.id).all()
    for city, state in joined:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
