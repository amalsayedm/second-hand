#!/usr/bin/env python3
'''this module defines the Item class'''

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship


class Item(BaseModel, Base):
    '''This class represents an item'''
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    description = Column(String(128), nullable=False)
    price = Column(Integer, nullable=False)
    picture = Column(LargeBinary, nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        '''initializes an item'''
        super().__init__(*args, **kwargs)

    def to_dict(self):
        '''returns a dictionary representation of an Item instance'''
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'picture': self.picture,
            'user_id': self.user_id,
            'category_id': self.category_id
        }
