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

    def save(self):
        '''This method saves the instance to the database'''
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        '''This method deletes the instance from the database'''
        models.storage.delete(self)
