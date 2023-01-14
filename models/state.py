#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.city import City
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        # cities = relationship('City')
        cities = relationship('City', cascade="all, delete", backref='state')
        # user = relationship("User", back_populates="addresses")

    else:
        @property
        def cities(self):
            """
            returns the list of City instances with state_id
            equals the current State.id
            """
            from models import storage
            related_cities = []

            cities = storage.all(City)
            # gets the entire storage- a dictionary
            for key, value in cities.items():
                # cities.value returns list of the city objects
                if value.state_id == self.id:
                    # if the object.state_id == self.id
                    related_cities.append(value)
                    # append to the cities list
            return related_cities
        # state = relationship('State')
