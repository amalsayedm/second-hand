#!/usr/bin/env python3
'''this module defines the User class'''

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, LargeBinary
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    '''This class represents a user'''
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    phone_number = Column(String(128), nullable=False)
    picture = Column(LargeBinary, nullable=True)
    token = Column(String(128), nullable=True, unique=True)

    def __init__(self, *args, **kwargs):
        '''initializes a user'''
        super().__init__(*args, **kwargs)

    def to_dict(self):
        '''returns a dictionary representation of a User instance'''
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone_number': self.phone_number,
            'picture': self.picture,
            'token': self.token
        }
