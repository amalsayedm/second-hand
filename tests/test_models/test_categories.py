#!/usr/bin/python3
"""Test categories for expected behavior with a test_database"""
import sys
import unittest
import os

# Add the parent directory of the current script to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
parent_dir = os.path.dirname(parent_dir)
sys.path.append(parent_dir)

from models import storage
from models.categories import Category
from models.base_model import BaseModel


class TestCategory(unittest.TestCase):
    """this will test the Category class"""
    def test_Category_subclass(self):
        """Test that Category is a subclass of BaseModel"""
        self.assertTrue(issubclass(Category, BaseModel))

    def test_Category_attributes(self):
        """Test that Category has the required attributes"""
        category = Category()
        self.assertTrue(hasattr(category, 'name'))
        self.assertTrue(hasattr(category, 'picture'))
        self.assertTrue(hasattr(category, 'id'))
        self.assertFalse(hasattr(category, 'created_at'))
        self.assertFalse(hasattr(category, 'updated_at'))

    def test_Category_attributes_type(self):
        """Test that Category attributes are of the right type"""
        category = Category(
            name='item',
            picture='alaa.jpg')
        BaseModel.save(category)
        self.assertIsInstance(category.name, str)
        self.assertIsInstance(category.picture, str)

    def test_unique_name(self):
        """Test that name is unique"""
        category1 = Category(name='item', picture='alaa.jpg')
        BaseModel.save(category1)
        category2 = Category(name='item', picture='alaa.jpg')
        self.assertFalse(BaseModel.save(category2))

    def test_category_item_relationship(self):
        """Test that Category has a relationship with Item"""
        category = Category(name='item', picture='alaa.jpg')
        BaseModel.save(category)
        self.assertTrue(hasattr(category, 'items'))
        self.assertIsInstance(category.items, list)


if __name__ == '__main__':
    unittest.main()
