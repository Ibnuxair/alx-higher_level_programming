#!/usr/bin/python3

"""
This module contains the class definition of a State and an

instance Base = declarative_base()
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """A class that defines a state."""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
