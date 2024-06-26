#!/usr/bin/env python3
'''this module defines the User class'''

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, LargeBinary
from sqlalchemy.orm import relationship
from models.favorites import Favorite
from models.followers import Follower
from models.search import Search


class User(BaseModel, Base):
    '''This class represents a user'''
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    phone_number = Column(String(128), nullable=False)
    picture = Column(String(128), nullable=True)
    token = Column(String(128), nullable=False, unique=True)
    salt = Column(String(128), nullable=False)
    favorites = relationship("Favorite", back_populates="user")
    following = relationship(
        "User", secondary='followers',
        primaryjoin=id == Follower.follower_id,
        secondaryjoin=id == Follower.following_id,
        backref="followers")
    searches = relationship("Search", back_populates="user")

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
            'token': self.token,

        }

    def get_user_following(self):
        '''This method retrieves the users following the current user'''
        return [user.to_dict() for user in self.following]

    def get_user_followers(self):
        '''This method retrieves the users following the current user'''
        return [user.to_dict() for user in self.followers]
