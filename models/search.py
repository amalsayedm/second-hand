#!/usr/bin/env python3
'''this module defines the Search class'''

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint, String
from sqlalchemy.orm import relationship


class Search(BaseModel, Base):
    '''This class represents a search'''
    __tablename__ = 'searches'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    user = relationship("User", back_populates="searches")

    __table_args__ = (
        UniqueConstraint('user_id', 'name', name='unique_user_query'),
    )

    def __init__(self, *args, **kwargs):
        '''initializes a search'''
        super().__init__(*args, **kwargs)

    def to_dict(self):
        '''returns a dictionary representation of a Search instance'''
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name
        }
