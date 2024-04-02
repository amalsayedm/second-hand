#!/usr/bin/python3
"""Test User for expected behavior with a test_database"""
import sys
import unittest
import os

# Add the parent directory of the current script to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
parent_dir = os.path.dirname(parent_dir)
sys.path.append(parent_dir)

from models import storage
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """this will test the User class"""
    def test_User_subclass(self):
        """Test that User is a subclass of BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_User_attributes(self):
        """Test that User has the required attributes"""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'name'))
        self.assertTrue(hasattr(user, 'phone_number'))
        self.assertTrue(hasattr(user, 'picture'))
        self.assertTrue(hasattr(user, 'token'))
        self.assertTrue(hasattr(user, 'salt'))
        self.assertTrue(hasattr(user, 'favorites'))
        self.assertTrue(hasattr(user, 'following'))
        self.assertTrue(hasattr(user, 'searches'))
        self.assertTrue(hasattr(user, 'id'))
        self.assertFalse(hasattr(user, 'created_at'))
        self.assertFalse(hasattr(user, 'updated_at'))

    def test_User_attributes_type(self):
        """Test that User attributes are of the right type"""
        user = User(
            name='Alaa',
            email='ala@gmail.com',
            password='password',
            phone_number='1234567890',
            picture='alaa.jpg',
            token='ouuyg',
            salt='89075')
        BaseModel.save(user)
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.name, str)
        self.assertIsInstance(user.phone_number, str)
        self.assertIsInstance(user.picture, str)
        self.assertIsInstance(user.token, str)
        self.assertIsInstance(user.salt, str)

    def test_unique_email(self):
        """Test that email is unique"""
        user1 = User(
            name='Alaa',
            email='alaa@gmail.com',
            password='password',
            phone_number='1234567890',
            picture='alaa.jpg',
            token='oujugiuytryugfb',
            salt='75')
        BaseModel.save(user1)
        user2 = User(
            name='Alaa',
            email='alaa@gmail.com',
            password='password',
            phone_number='1234567890',
            picture='alaa.jpg',
            token='oujuguyg',
            salt='-9489075')
        self.assertFalse(user2.save())

    def test_pic_can_be_null(self):
        """Test that picture can be null"""
        user2 = User(
            name='roka',
            email='roka@example.com',
            password='password4',
            phone_number='0987654321',
            token='1245',
            salt='lt123')
        user2.save()
        self.assertEqual(user2.picture, None)

    def test_follower(self):
        """Test that user can follow another user"""
        user1 = User(
            name='body',
            email='body@gmail.com',
            password='password',
            phone_number='1234567890',
            picture='body.jpg',
            token='oujugryugfb',
            salt='5')
        user2 = User(
            name='manal',
            email='manal@gmail.com',
            password='password',
            phone_number='1234567890',
            picture='manal.jpg',
            token='oujug',
            salt='7565')
        BaseModel.save_all([user1, user2])
        user1.following.append(user2)
        self.assertIn(user2, user1.following)
        self.assertIn(user1, user2.followers)

    def test_get_followers(self):
        """Test that user can get all followers"""
        user1 = storage.finduser_byemail('body@gmail.com')
        user2 = storage.finduser_byemail('manal@gmail.com')
        self.assertIn(user2, user1.following)

    def test_get_following(self):
        """Test that user can get all following"""
        user1 = storage.finduser_byemail('body@gmail.com')
        user2 = storage.finduser_byemail('manal@gmail.com')
        self.assertIn(user1, user2.followers)

    def test_unfollow(self):
        """Test that user can unfollow another user"""
        user1 = storage.finduser_byemail('body@gmail.com')
        user2 = storage.finduser_byemail('manal@gmail.com')
        user1.following.remove(user2)
        self.assertNotIn(user2, user1.following)
        self.assertNotIn(user1, user2.followers)


if __name__ == '__main__':
    unittest.main()
