#!/usr/bin/env python3
'''This module defines a class to manage db storage for second_hand'''

import models
import os
from models.base_model import BaseModel, Base
from models.user import User
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

classes = {
    'User': User
}


class DBStorage:
    '''This class manages storage of second_hand objects in a database'''
    __engine = None
    __session = None

    def __init__(self) -> None:
        '''This method creates a new instance of DBStorage'''
        SECOND_HAND_MYSQL_USER = os.getenv('second_hand_mysql_user')
        SECOND_HAND_MYSQL_PWD = os.getenv('second_hand_mysql_pwd')
        SECOND_HAND_MYSQL_HOST = os.getenv('second_hand_mysql_host')
        SECOND_HAND_MYSQL_DB = os.getenv('second_hand_mysql_db')
        SECOND_HAND_MYSQL_PORT = os.getenv('second_hand_mysql_port')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'
                                      .format(SECOND_HAND_MYSQL_USER,
                                              SECOND_HAND_MYSQL_PWD,
                                              SECOND_HAND_MYSQL_HOST,
                                              SECOND_HAND_MYSQL_PORT,
                                              SECOND_HAND_MYSQL_DB),
                                      pool_pre_ping=True)

    def new(self, obj) -> None:
        '''This method adds a new object to the current database session'''
        if obj:
            self.__session.add(obj)

    def save(self) -> None:
        '''This method commits all changes to the current database session'''
        self.__session.commit()

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
