#!/usr/bin/python3
"""Test locations or expected behavior with a test_database"""

import sys
import unittest
import os

# Add the parent directory of the current script to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
parent_dir = os.path.dirname(parent_dir)
sys.path.append(parent_dir)

from models import storage
from models.locations import Location
from models.base_model import BaseModel


class TestLocation(unittest.TestCase):
    """this will test the Location class"""
    def test_Location_subclass(self):
        """Test that Location is a subclass of BaseModel"""
        self.assertTrue(issubclass(Location, BaseModel))

    def test_Location_attributes(self):
        """Test that Location has the required attributes"""
        self.assertTrue(hasattr(Location, 'name'))
        self.assertFalse(hasattr(Location, 'latitude'))
        self.assertFalse(hasattr(Location, 'longitude'))
        self.assertFalse(hasattr(Location, 'item_id'))
        self.assertFalse(hasattr(Location, 'picture'))

    def test_Location_attributes_type(self):
        """Test that Location attributes are of the right type"""
        loc = Location(
            name='Cairo',
            )
        BaseModel.save(loc)
        self.assertIsInstance(loc.name, str)

    def test_location_item_relationship(self):
        """Test that Location has a relationship with Item"""
        loc = Location(
            name='Cairo',
            )
        BaseModel.save(loc)
        self.assertTrue(hasattr(loc, 'items'))
        self.assertIsInstance(loc.items, list)

    def test_unique_name(self):
        """Test that name is unique"""
        loc1 = Location(name='Cairo')
        BaseModel.save(loc1)
        loc2 = Location(name='Cairo')
        self.assertFalse(BaseModel.save(loc2))


if __name__ == '__main__':
    unittest.main()
