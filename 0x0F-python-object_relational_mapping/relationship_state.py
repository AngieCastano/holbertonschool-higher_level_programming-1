#!/usr/bin/python3
'''
contains the class definition of a State
and an instance Base = declarative_base()
Establishes a relationship between cities and states
'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship as rs

Base = declarative_base()


class State(Base):
    '''Definition of the State class'''
    __tablename__ = 'states'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(128), nullable=False)
    cities = rs("City", backref="state")
