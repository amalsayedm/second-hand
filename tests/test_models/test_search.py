#!/usr/bin/python3
"""Test searches or expected behavior with a test_database"""

import sys
import unittest
import os

# Add the parent directory of the current script to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
parent_dir = os.path.dirname(parent_dir)
sys.path.append(parent_dir)

from models import storage
from models.search import Search
from models.base_model import BaseModel


class TestSearch(unittest.TestCase):
    """this will test the Search class"""
    def test_Search_subclass(self):
        """Test that Search is a subclass of BaseModel"""
        self.assertTrue(issubclass(Search, BaseModel))

    def test_Search_attributes(self):
        """Test that Search has the required attributes"""
        self.assertTrue(hasattr(Search, 'user_id'))
        self.assertTrue(hasattr(Search, 'name'))
        self.assertTrue(hasattr(Search, 'id'))
        self.assertFalse(hasattr(Search, 'created_at'))
        self.assertFalse(hasattr(Search, 'updated_at'))

    def test_Search_attributes_type(self):
        """Test that Search attributes are of the right type"""
        search = Search(
            user_id=1,
            name='item',)
        BaseModel.save(search)
        self.assertIsInstance(search.user_id, int)
        self.assertIsInstance(search.name, str)

    def test_unique_name(self):
        """Test that name is unique"""
        search1 = Search(user_id=1, name='item')
        BaseModel.save(search1)
        search2 = Search(user_id=1, name='item')
        self.assertFalse(BaseModel.save(search2))

    def test_search_user_relationship(self):
        """test that Search has a relationship with User"""
        search = Search(user_id=1, name='item')
        BaseModel.save(search)
        self.assertTrue(hasattr(search, 'user'))
        self.assertIsInstance(search.user, object)


if __name__ == '__main__':
    unittest.main()
