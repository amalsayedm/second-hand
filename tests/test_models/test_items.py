#!/usr/bin/python3
"""Test Item for expected behavior with a test_database"""
import sys
import unittest
import os

# Add the parent directory of the current script to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
parent_dir = os.path.dirname(parent_dir)
sys.path.append(parent_dir)

from models import storage
from models.items import Item
from models.base_model import BaseModel


class TestItem(unittest.TestCase):
    """this will test the Item class"""
    def test_Item_subclass(self):
        """Test that Item is a subclass of BaseModel"""
        self.assertTrue(issubclass(Item, BaseModel))

    def test_Item_attributes(self):
        """Test that Item has the required attributes"""
        item = Item()
        self.assertTrue(hasattr(item, 'name'))
        self.assertTrue(hasattr(item, 'description'))
        self.assertTrue(hasattr(item, 'price'))
        self.assertTrue(hasattr(item, 'picture'))
        self.assertTrue(hasattr(item, 'category_id'))
        self.assertTrue(hasattr(item, 'location_id'))
        self.assertTrue(hasattr(item, 'user_id'))
        self.assertTrue(hasattr(item, 'id'))
        self.assertTrue(hasattr(item, 'size'))
        self.assertTrue(hasattr(item, 'favorites'))
        self.assertTrue(hasattr(item, 'category'))
        self.assertTrue(hasattr(item, 'location'))
        self.assertFalse(hasattr(item, 'created_at'))
        self.assertFalse(hasattr(item, 'updated_at'))
        self.assertFalse(hasattr(item, 'user'))
        self.assertFalse(hasattr(item, 'email'))

    def test_Item_attributes_type(self):
        """Test that Item attributes are of the right type"""
        item = Item(
            name='item',
            description='description',
            price=100,
            picture='alaa.jpg',
            category_id=1,
            location_id=1,
            user_id=1,
            size='small')
        BaseModel.save(item)
        self.assertIsInstance(item.name, str)
        self.assertIsInstance(item.description, str)
        self.assertIsInstance(item.price, int)
        self.assertIsInstance(item.picture, str)
        self.assertIsInstance(item.category_id, int)
        self.assertIsInstance(item.location_id, int)
        self.assertIsInstance(item.user_id, int)
        self.assertIsInstance(item.size, str)

    def test_nullable_false(self):
        """Test that nullable is False"""
        item = Item()
        self.assertFalse(item.name)
        self.assertFalse(item.description)
        self.assertFalse(item.price)
        self.assertFalse(item.picture)
        self.assertFalse(item.category_id)
        self.assertFalse(item.location_id)
        self.assertFalse(item.user_id)
        self.assertFalse(item.size)

    def test_item_category_relationship(self):
        """Test that Item has a relationship with Category"""
        item = Item(
            name='item',
            description='description',
            price=100,
            picture='alaa.jpg',
            category_id=1,
            location_id=1,
            user_id=1,
            size='small')
        BaseModel.save(item)
        self.assertTrue(hasattr(item, 'category'))
        self.assertIsInstance(item.category, object)

    def test_item_location_relationship(self):
        """Test that Item has a relationship with Location"""
        item = Item(
            name='item',
            description='description',
            price=100,
            picture='alaa.jpg',
            category_id=1,
            location_id=1,
            user_id=1,
            size='small')
        BaseModel.save(item)
        self.assertTrue(hasattr(item, 'location'))
        self.assertIsInstance(item.location, object)

    def test_item_user_relationship(self):
        """Test that Item has a relationship with User"""
        item = Item(
            name='item',
            description='description',
            price=100,
            picture='alaa.jpg',
            category_id=1,
            location_id=1,
            user_id=1,
            size='small')
        BaseModel.save(item)
        self.assertTrue(hasattr(item, 'user_id'))
        self.assertIsInstance(item.user_id, object)


if __name__ == '__main__':
    unittest.main()
