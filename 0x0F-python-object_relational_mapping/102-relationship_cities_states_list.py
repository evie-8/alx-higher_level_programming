#!/usr/bin/python3
"""Start link class to table in database
"""


import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    for city, state in session.query(City, State).\
            filter(City.state_id == State.id).order_by(City.id).all():
        print(f"{city.id}: {city.name} -> {state.name}")
    session.close()
