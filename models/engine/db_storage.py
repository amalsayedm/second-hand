#!/usr/bin/env python3
'''This module defines a class to manage db storage for second_hand'''

import models
import os
from typing import List
from models.base_model import BaseModel, Base
from models.user import User
from models.categories import Category
from models.items import Item
from models.favorites import Favorite
from models.followers import Follower
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

classes = {
    'User': User,
    'Category': Category,
    'Item': Item,
    'Favorite': Favorite,
    'Follower': Follower
}


class DBStorage:
    '''This class manages storage of second_hand objects in a database'''
    __engine = None
    __session = None

    _mysql_user = 'second_hand'
    _mysql_pwd =  'Second_hand_pwd1'
    _mysql_host = 'localhost'
    _mysql_db = 'second_hand'
    _mysql_port = 3306

    def __init__(self) -> None:
        '''This method creates a new instance of DBStorage'''

        SECOND_HAND_MYSQL_USER = os.getenv('second_hand_mysql_user') or self._mysql_user
        SECOND_HAND_MYSQL_PWD = os.getenv('second_hand_mysql_pwd') or self._mysql_pwd
        SECOND_HAND_MYSQL_HOST = os.getenv('second_hand_mysql_host') or self._mysql_host
        SECOND_HAND_MYSQL_DB = os.getenv('second_hand_mysql_db') or self._mysql_db
        SECOND_HAND_MYSQL_PORT = os.getenv('second_hand_mysql_port') or self._mysql_port

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'
                                      .format(SECOND_HAND_MYSQL_USER,
                                              SECOND_HAND_MYSQL_PWD,
                                              SECOND_HAND_MYSQL_HOST,
                                              SECOND_HAND_MYSQL_PORT,
                                              SECOND_HAND_MYSQL_DB))

    def new(self, obj) -> None:
        '''This method adds a new object to the current database session'''
        if obj:
            self.__session.add(obj)

    def save(self) -> None:
        '''This method commits all changes to the current database session'''
        self.__session.commit()

    def all(self, cls=None) -> List[dict]:
        ''''This method queries the current database session
        based on the class name'''
        objects = []
        if not cls:
            print('cls required')
            return
        if type(cls) == str:
            cls = classes[cls]
        result = self.__session.query(cls).all()
        for obj in result:
            objects.append(obj.to_dict())
        return objects

    def get(self, cls, id) -> object:
        '''This method retrieves an object from the current database session'''
        if cls and id:
            return self.__session.query(cls).filter_by(id=id).first()
        return None

    def update(self, cls, id, **kwargs) -> None:
        '''This method updates an object from the current database session'''
        if cls and id:
            obj = self.__session.query(cls).filter_by(id=id).first()
            for key, value in kwargs.items():
                setattr(obj, key, value)
            self.save()

    def delete(self, obj=None) -> None:
        '''This method deletes an object from the current database session'''
        if obj:
            self.__session.delete(obj)

    def reload(self) -> None:
        '''This method creates all tables in the database'''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        '''This method closes the current session'''
        self.__session.remove()
<<<<<<< HEAD
    
    def getuser_bytoken(self,token) -> object:
=======

    def getuser_bytoken(self, token) -> object:
>>>>>>> database
        '''This method retrieves an object from the current database session'''
        if token:
            return self.__session.query(User).filter_by(token=token).first()
        return None
<<<<<<< HEAD
    
    # def getItemsbycat(self,cat_id):
    #     results = self.__session.query(Items).filter(cat.type == cat_id).all()
    #     return (results)
    
    # def getItemsbyuser(self,user_id):
    #     results = self.__session.query(Items).filter(user.id == user_id).all()
    #     return (results)
    
    # def getuserfavorites(self,user_id):
    #     items = self.__session.query(Items).join(Favorites).filter(Favorites.user_id == user_id).all()
    #     return (items)
    
    # def getuserfollowers(self,user_id):
    #     items = self.__session.query(Users).join(followers).filter(followers.followind_id == user_id).all()
    #     return (items)

    # def get_userfollowings(self,user_id):
    #     items = self.__session.query(Users).join(followers).filter(followers.user_id == user_id).all()
    #     return (items)
=======

    def search_items(self, name) -> List[dict]:
        '''This method retrieves an object from the current database session'''
        objects = []
        if name:
            result = self.__session.query(Item).filter(
                Item.name.like('%'+name+'%')).all()
            for obj in result:
                objects.append(obj.to_dict())
        return objects

    def get_user_favorites(self, user_id) -> List[dict]:
        '''This method retrieves an object from the current database session'''
        objects = []
        if user_id:
            result = self.__session.query(Favorite).filter_by(
                user_id=user_id).all()
            for obj in result:
                objects.append(self.get(cls=Item, id=obj.item_id).to_dict())
        return objects

    def get_user_following(self, user_id) -> List[dict]:
        '''This method retrieves an object from the current database session'''
        objects = []
        if user_id:
            result = self.__session.query(Follower).filter_by(
                follower_id=user_id).all()
            for obj in result:
                objects.append(self.get(
                    cls=User, id=obj.following_id).to_dict())
        return objects

    def get_user_followers(self, user_id) -> List[dict]:
        '''This method retrieves an object from the current database session'''
        objects = []
        if user_id:
            result = self.__session.query(Follower).filter_by(
                following_id=user_id).all()
            for obj in result:
                objects.append(self.get(
                    cls=User, id=obj.follower_id).to_dict())
        return objects

    def getuserfavorites(self,user_id):
        objects = []
        if user_id:
            items = self.__session.query(Item).join(Favorite).filter(Favorite.user_id == user_id).all()
            for item in items:
                objects.append(item.to_dict())
        return (objects)
    
>>>>>>> database
