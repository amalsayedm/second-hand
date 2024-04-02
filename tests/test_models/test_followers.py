#!/usr/bin/python3
"""Test followers or expected behavior with a test_database"""

import sys
import unittest
import os

# Add the parent directory of the current script to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
parent_dir = os.path.dirname(parent_dir)
sys.path.append(parent_dir)

from models import storage
from models.followers import Follower
from models.base_model import BaseModel
from models.user import User


class TestFollower(unittest.TestCase):
    """this will test the Follower class"""
    def test_Follower_subclass(self):
        """Test that Follower is a subclass of BaseModel"""
        self.assertTrue(issubclass(Follower, BaseModel))

    def test_Follower_attributes(self):
        """Test that Follower has the required attributes"""
        self.assertTrue(hasattr(Follower, 'follower_id'))
        self.assertTrue(hasattr(Follower, 'following_id'))
        self.assertFalse(hasattr(Follower, 'item_id'))
        self.assertFalse(hasattr(Follower, 'name'))
        self.assertFalse(hasattr(Follower, 'picture'))

    def test_UniqueConstraint(self):
        """test that same user can't follow a user more than one time"""
        user = User(
            name='Ayman',
            email='ayman@gmail.com',
            password='password',
            phone_number='1234567890',
            picture='ayman.jpg',
            token='oujugwrt4',
            salt='75g65'
        )

        user2 = User(
            name='Doda',
            email='doda@gmail.com',
            password='password',
            phone_number='1234567890',
            picture='doda.jpg',
            token='ugwrt4',
            salt='65'
        )

        BaseModel.save_all([user, user2])
        user_id = user.id
        user2_id = user2.id
        follower1 = Follower(follower_id=user_id, following_id=user2_id)
        self.assertTrue(BaseModel.save(follower1))
        follower2 = Follower(follower_id=user_id, following_id=user2_id)
        self.assertFalse(BaseModel.save(follower2))


if __name__ == '__main__':
    unittest.main()
