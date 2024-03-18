#!/usr/bin/env python3
'''this module defines the followers table'''

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Follower(BaseModel, Base):
    '''This class represents a follower'''
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    follower_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    following_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        '''initializes a follower'''
        super().__init__(*args, **kwargs)

    def to_dict(self):
        '''returns a dictionary representation of a Follower instance'''
        return {
            'id': self.id,
            'user_id': self.user_id,
            'follower_id': self.follower_id
        }
