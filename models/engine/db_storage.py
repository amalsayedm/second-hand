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
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

classes = {
    'User': User,
    'Category': Category,
    'Item': Item,
    'Favorite': Favorite
}


class DBStorage:
    '''This class manages storage of second_hand objects in a database'''
    __engine = None
    __session = None

    def __init__(self) -> None:
        '''This method creates a new instance of DBStorage'''
        SECOND_HAND_MYSQL_USER = os.getenv('second_hand_mysql_user') or 'second_hand'
        SECOND_HAND_MYSQL_PWD = os.getenv('second_hand_mysql_pwd') or 'Second_hand_pwd1'
        SECOND_HAND_MYSQL_HOST = os.getenv('second_hand_mysql_host') or 'localhost'
        SECOND_HAND_MYSQL_DB = os.getenv('second_hand_mysql_db') or 'second_hand'
        SECOND_HAND_MYSQL_PORT = os.getenv('second_hand_mysql_port') or 3306
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

    def getuser_bytoken(self, token) -> object:
        '''This method retrieves an object from the current database session'''
        if token:
            return self.__session.query(User).filter_by(token=token).first()
        return None

    def search_items(self, name) -> List[dict]:
        '''This method retrieves an object from the current database session'''
        objects = []
        if name:
            result = self.__session.query(Item).filter(
                Item.name.like('%'+name+'%')).all()
            for obj in result:
                objects.append(obj.to_dict())
        return objects

    def get_favorites(self, user_id) -> List[dict]:
        '''This method retrieves an object from the current database session'''
        objects = []
        if user_id:
            result = self.__session.query(Favorite).filter_by(user_id=user_id).all()
            for obj in result:
                objects.append(self.get(cls=Item, id=obj.item_id).to_dict())
        return objects
