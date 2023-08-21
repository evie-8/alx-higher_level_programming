#!/usr/bin/python3
'''a  python file that contains the class definition of a City
and an instance Base = declarative_base()'''


from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from model_state import Base, State


class City(Base):
    '''Class for states'''
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True,
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
