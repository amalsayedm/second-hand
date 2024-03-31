#!/usr/bin/env python3
''' This module contains the BaseModel class
    This class is the base class for all other classes in this project
'''
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models

Base = declarative_base()


class BaseModel:
    '''This class is the base class for all other classes in this project'''

    def __init__(self, *args, **kwargs):
        '''This method initializes a new instance of BaseModel'''
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def save(self):
        '''This method saves the instance to the database'''
        try:
            models.storage.new(self)
            models.storage.save()
            return True
        except:
            return False

    @classmethod
    def save_all(self, objects: list):
        '''This method saves the instance to the database'''
        for obj in objects:
            models.storage.new(obj)
        models.storage.save()

    def delete(self):
        '''This method deletes the instance from the database'''
        models.storage.delete(self)
        models.storage.save()
