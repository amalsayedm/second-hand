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
from models.search import Search
from models.locations import Location
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

classes = {
    'User': User,
    'Category': Category,
    'Item': Item,
    'Favorite': Favorite,
    'Follower': Follower,
    'Follower': Follower,
    'Search': Search,
    'Location': Location,
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

    def update(self, cls, class_id, ignore_items, **kwargs) -> object:
        '''This method updates an object from the current database session'''
        if cls and class_id:
            obj = self.__session.query(cls).filter_by(id=class_id).first()
            if(obj):
                for key, value in kwargs.items():
                    if key not in ignore_items:
                        if key == 'picture':
                            encoded_data = value.encode('utf-8')
                            setattr(obj, key, encoded_data)
                        else:
                            setattr(obj, key, value)
                self.save()
            return obj

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
        
    def count(self, cls: object) -> int:
        """
        count the number of objects in storage
        """
        count = len(models.storage.all(cls))
        return count

    def getuser_bytoken(self, token) -> object:

        '''This method retrieves an object from the current database session'''
        if token:
            return self.__session.query(User).filter_by(token=token).first()
        return None
    
    def finduser_byemail(self, uemail) -> object:

        '''This method retrieves an object from the current database session'''
        if uemail:
            return self.__session.query(User).filter(User.email==uemail).first()
        return None

    def getItemsbyuser(self,user_id):
        objects =[]
        results = self.__session.query(Item).filter(Item.user_id == user_id).all()
        for item in results:
                objects.append(item.to_dict())
        return (objects)
    
    def get_user_favorites(self, user_id) -> List[dict]:
        '''This method retrieves an object from the current database session'''
        objects = []
        if user_id:
            items = self.__session.query(Item).join(Favorite).filter(
                Favorite.user_id == user_id).all()
            for item in items:
                objects.append(item.to_dict())
        return (objects)

    def search_items(self, name) -> List[dict]:
        '''This method retrieves an object from the current database session'''
        objects = []
        if name:
            result = self.__session.query(Item).filter(
                Item.name.like('%'+name+'%')).all()
            for obj in result:
                objects.append(obj.to_dict())
        return objects

    def getuserfavorites(self,user_id) -> List[dict]:
        objects = []
        if user_id:
            items = self.__session.query(Item).join(Favorite).filter(Favorite.user_id == user_id).all()
            for item in items:
                objects.append(item.to_dict())
        return (objects)
    
    def get_items_by_location(self, loc_id) -> List[dict]:
        '''This method retrieves an object from the current database session'''
        objects = []
        if loc_id:
            result = self.__session.query(Item).join(Location).filter(
                Location.id == loc_id).all()
            for obj in result:
                objects.append(obj.to_dict())
        return objects

    def get_items_by_category(self, cat_id) -> List[dict]:
        '''This method retrieves an object from the current database session'''
        objects = []
        if cat_id:
            result = self.__session.query(Item).join(Category).filter(
                Category.id == cat_id ).all()
            for obj in result:
                objects.append(obj.to_dict())
        return objects
    
    def search_item_with_filters(self,location_id,cat_id,search_text) -> List[dict]:
        objects = []
        query = self.__session.query(Item)
        query = query.join(Location)
        query = query.join(Category)
        filters = []
        if location_id is not None:
            filters.append(Location.id == location_id)
        if cat_id is not None:
            filters.append(Category.id == cat_id)
        if search_text is not None:
            filters.append(Item.name.like('%'+search_text+'%'))
        if filters:
            result = query.filter(*filters).all()
            for obj in result:
                objects.append(obj.to_dict())
        return objects
    
    def delete_favourite(self,item_id, user_id) -> bool:
        '''This method retrieves an object from the current database session'''
        if item_id and user_id:
            obj = self.__session.query(Favorite).filter(Favorite.item_id ==item_id , Favorite.user_id == user_id ).first()
            if obj: 
                self.delete(obj=obj)
                return True
        return False
    
    def get_searches_by_user(self, user_id) -> List[dict]:
        '''This method retrieves an object from the current database session'''
        objects = []
        if user_id:
            searches = self.__session.query(Search).filter(
                Search.user_id == user_id).all()
            for search in searches:
                objects.append(search.to_dict()['name'])
        return objects

    def get_items(self, name, description) -> List[dict]:
        '''This method retrieves an object from the current database session'''
        objects = []
        if name and description:
            items = self.__session.query(Item).filter(Item.name == name, Item.description == description).all()
            for item in items:
                objects.append(item.to_dict())
        return objects
    
    def get_most_recent_items(self, page: int, per_page: int) -> List[dict]:
        '''This method retrieves an object from the current database session'''
        start = (page - 1) * per_page
        end = start + per_page
        objects = []
        result = self.__session.query(Item).order_by(Item.id.desc()).offset(start).limit(per_page).all()
        for obj in result:
            objects.append(obj.to_dict())
        return objects
