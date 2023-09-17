#!/usr/bin/python3
"""a python file that contains the class definition of
   a State and an instance Base = declarative_base()
"""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """ Class with id and name attributes of states
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
