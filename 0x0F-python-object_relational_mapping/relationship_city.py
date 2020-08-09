#!/usr/bin/python3
'''
Contains the class definition of a City
'''

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    '''Definition of the State class'''
    __tablename__ = 'cities'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer, ForeignKey(
        'states.id'), nullable=False)
