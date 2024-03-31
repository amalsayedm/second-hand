#!/usr/bin/env python3
'''this module defines the locations table'''


from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Location(BaseModel, Base):
    '''This class represents a location'''
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False, unique=True)
    items = relationship(
        'Item', backref='location', cascade='all, delete-orphan')

    def __init__(self, *args, **kwargs):
        '''initializes a location'''
        super().__init__(*args, **kwargs)

    def to_dict(self):
        '''returns a dictionary representation of a Location instance'''
        return {
            'id': self.id,
            'name': self.name
        }
