#!/usr/bin/python3
'''
    Implementation of the State class
'''

from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship(City, backref="state", cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            '''
             FileStorage to return City instances with state_id == current State.id
            '''
            from models import storage
            list_cities = []
            for city_inst in storage.all(City).values():
                if city_inst.state_id == self.id:
                    list_cities.append(city_inst)
            return list_cities
