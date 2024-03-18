#!/usr/bin/env python3
'''this module defines the Recommendation class'''

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Recommendation(BaseModel, Base):
    '''This class represents a recommendation'''
    __tablename__ = 'recommendations'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    user = relationship("User", back_populates="recommendations")
    item = relationship("Item", back_populates="recommendations")

    def __init__(self, *args, **kwargs):
        '''initializes a recommendation'''
        super().__init__(*args, **kwargs)

    def to_dict(self):
        '''returns a dictionary representation of a Recommendation instance'''
        return {
            'id': self.id,
            'user_id': self.user_id,
            'item_id': self.item_id
        }
