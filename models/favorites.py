#!/usr/bin/env python3
'''this module defines the Favourite class'''

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Favorite(BaseModel, Base):
    '''This class represents user favourites'''
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    item_id = Column(Integer, ForeignKey('items.id'))
    user = relationship("User", backref="favorites")
    item = relationship("Item", backref="favorites")

    def __init__(self, *args, **kwargs):
        '''initializes a favourite'''
        super().__init__(*args, **kwargs)

    def to_dict(self):
        '''returns a dictionary representation of a Favourite instance'''
        return {
            'id': self.id,
            'user_id': self.user_id,
            'item_id': self.item_id
        }
