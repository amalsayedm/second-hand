#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Recipe": Recipe, "category":Category, "Favorites":Favorites ,"User":User}

class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format('recipes_dev',
                                             'recipes_dev_pwd',
                                             'localhost',
                                             'recipes_dev_db'))
    
    def all(self, cls):
        """query on the current database session"""
        new_dict = {}
    
        objs = self.__session.query(cls).all()
        return (objs)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session
    
    def getItemsbycat(self,cat_id):
        results = self.__session.query(Items).filter(cat.type == cat_id).all()
        return (results)
    def getItemsbyuser(self,user_id):
        results = self.__session.query(Items).filter(user.id == user_id).all()
        return (results)
    
    def getuserfavorites(self,user_id):
        items = self.__session.query(Items).join(Favorites).filter(Favorites.user_id == user_id).all()
        return (items)
    
    def getuserfollowers(self,user_id):
        items = self.__session.query(Users).join(followers).filter(followers.followind_id == user_id).all()
        return (items)

    def get_userfollowings(self,user_id):
        items = self.__session.query(Users).join(followers).filter(followers.user_id == user_id).all()
        return (items)

    
    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        result = self.__session.query(cls).get(id)
        if(result):
            return result
        return None
