#!/usr/bin/python3
"""Test favorits or expected behavior with a test_database"""

import sys
import unittest
import os

# Add the parent directory of the current script to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
parent_dir = os.path.dirname(parent_dir)
sys.path.append(parent_dir)

from models import storage
from models.favorites import Favorite
from models.base_model import BaseModel


class TestFavorite(unittest.TestCase):
    """this will test the Favorite class"""
    def test_Favorite_subclass(self):
        """Test that Favorite is a subclass of BaseModel"""
        self.assertTrue(issubclass(Favorite, BaseModel))

    def test_Favorite_attributes(self):
        """Test that Fvorite has the required attributes"""
        self.assertTrue(hasattr(Favorite, 'id'))
        self.assertTrue(hasattr(Favorite, 'user_id'))
        self.assertTrue(hasattr(Favorite, 'item_id'))
        self.assertFalse(hasattr(Favorite, 'name'))
        self.assertFalse(hasattr(Favorite, 'picture'))

    def test_Favotite_attributes_type(self):
        """Test that Category attributes are of the right type"""
        fav = Favorite(
            user_id=1,
            item_id=1)
        BaseModel.save(fav)
        self.assertIsInstance(fav.user_id, int)
        self.assertIsInstance(fav.item_id, int)

    def test_favorite_user_relationship(self):
        """Test that Favorite has a relationship with User"""
        fav = Favorite(user_id=1, item_id=1)
        BaseModel.save(fav)
        self.assertTrue(hasattr(fav, 'user'))
        self.assertIsInstance(fav.user, object)

    def test_favorite_item_relationship(self):
        """Test that Favorite has a relationship with Item"""
        fav = Favorite(user_id=1, item_id=1)
        BaseModel.save(fav)
        self.assertTrue(hasattr(fav, 'item'))
        self.assertIsInstance(fav.item, object)

    def test_unique_favorite(self):
        """Test that user can favorite an item more than one time"""
        fav = Favorite(user_id=1, item_id=1)
        BaseModel.save(fav)
        fav2 = Favorite(user_id=1, item_id=1)
        self.assertFalse(BaseModel.save(fav2))


if __name__ == '__main__':
    unittest.main()
