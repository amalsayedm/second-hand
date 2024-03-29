#!/usr/bin/env python3
'''this module defines the Category class'''

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, LargeBinary
from sqlalchemy.orm import relationship


class Category(BaseModel, Base):
    '''This class represents a category'''
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False, unique=True)
    picture = Column(String(128), nullable=False)
    items = relationship(
        'Item', backref='category', cascade='all, delete-orphan')

    def __init__(self, *args, **kwargs):
        '''initializes a category'''
        super().__init__(*args, **kwargs)

    def to_dict(self):
        '''returns a dictionary representation of a Category instance'''
        return {
            'id': self.id,
            'name': self.name,
            'picture': self.picture,
        }
