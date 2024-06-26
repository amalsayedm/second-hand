#!/usr/bin/env python3
'''this module defines the Item class'''

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from models.favorites import Favorite
from models.user import User
from models.locations import Location


class Item(BaseModel, Base):
    '''This class represents an item'''
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    description = Column(String(128), nullable=False)
    price = Column(Integer, nullable=False)
    picture = Column(String(128), nullable=False)
    size = Column(String(128), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    location_id = Column(Integer, ForeignKey('locations.id'), nullable=False)
    favorites = relationship("Favorite", back_populates="item")

    def __init__(self, *args, **kwargs):
        '''initializes an item'''
        super().__init__(*args, **kwargs)

    def to_dict(self):
        '''returns a dictionary representation of an Item instance'''
        from models import storage
        user = storage.get(User, self.user_id)
        phone_number = user.phone_number if user else None
        location = storage.get(Location, self.location_id)
        location_name = location.name if location else None

        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'picture': self.picture,
            'size': self.size,
            'user_id': self.user_id,
            'category_id': self.category_id,
            'location_id': self.location_id,
            'contact': phone_number,
            'location_name': location_name
        }
