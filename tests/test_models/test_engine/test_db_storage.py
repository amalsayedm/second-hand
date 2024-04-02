#!/usr/bin/python3
"""Test db_storage behavior with a test_database"""

import sys
import unittest
import os

# Add the parent directory of the current script to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
parent_dir = os.path.dirname(parent_dir)
parent_dir = os.path.dirname(parent_dir)
sys.path.append(parent_dir)

from models import storage
from models.user import User
from models.items import Item
from models.base_model import BaseModel
from models.categories import Category
from models.locations import Location


class TestDBStorage(unittest.TestCase):
    """this will test the DBStorage class"""

    def test_new(self):
        """Test that new() adds an object to the database"""
        user = User(
            name='test',
            email='test@ex.com',
            password='password',
            phone_number='1234567890',
            picture='test.jpg',
            token='token',
            salt='salt'
            )
        self.assertTrue(storage.new(user))

    def test_save(self):
        """Test that save() adds an object to the database"""
        user = User(
            name='test2',
            email='test2@ex.com',
            password='password',
            phone_number='1234567890',
            picture='test.jpg',
            token='token2',
            salt='salt'
            )
        storage.new(user)
        self.assertTrue(storage.save())
        self.assertTrue(user.id)

    def test_all(self):
        """the test for all method"""
        user1 = User(
            name='test1',
            email='test1@ex.com',
            password='password',
            phone_number='1234567890',
            picture='test.jpg',
            token='token1',
            salt='salt1'
            )
        user2 = User(
            name='test2',
            email='test@ex2.com',
            password='password',
            phone_number='1234567890',
            picture='test.jpg',
            token='token22',
            salt='salt2'
            )
        BaseModel.save_all([user1, user2])
        all_users = storage.all(User)
        self.assertIsInstance(all_users, list)
        self.assertTrue(len(all_users) == 2)
        self.assertIsInstance(all_users[0], dict)

    def test_get(self):
        """Test the get method"""
        user = User(
            name='test3',
            email='test3@gmail.com',
            password='password',
            phone_number='1234567890',
            picture='test.jpg',
            token='token3',
            salt='salt3'
            )
        BaseModel.save(user)
        user_id = user.id
        self.assertIsInstance(storage.get(User, user_id), User)
        self.assertTrue(storage.get(User, user_id))
        self.assertIsNone(storage.get(User, 12))

    def test_count(self):
        """Test the count method"""
        user1 = User(
            name='test4',
            email='test4@gmail.com',
            password='password',
            phone_number='1234567890',
            picture='test.jpg',
            token='token4',
            salt='salt4'
            )
        user2 = User(
            name='test5',
            email='test5@gmail.com',
            password='password',
            phone_number='1234567890',
            picture='test.jpg',
            token='token5',
            salt='salt5'
            )
        BaseModel.save_all([user1, user2])
        self.assertTrue(storage.count(User) == 4)
        self.assertFalse(storage.count(User) == 3)

    def test_delete(self):
        """Test the delete method"""
        user = User(
            name='test6',
            email='tets6@gmail.com',
            password='password',
            phone_number='1234567890',
            picture='test.jpg',
            token='token6',
            salt='salt6'
            )
        BaseModel.save(user)
        user_id = user.id
        storage.delete(user)
        self.assertIsNone(storage.get(User, user_id))

    def test_update(self):
        """Test the update method"""
        user = User(
            name='test7',
            email='test7@email.com',
            password='password',
            phone_number='1234567890',
            picture='test.jpg',
            token='token7',
            salt='salt7'
            )
        BaseModel.save(user)
        user_id = user.id
        ignore = ['id', 'token']
        storage.update(User, user_id, ignore_items=ignore, name='test8')
        self.assertTrue(user.name == 'test8')

    def test_finduser_byemail(self):
        """Test the get_user_by_email method"""
        user = User(
            name='test9',
            email='test9@gmail.com',
            password='password',
            phone_number='1234567890',
            picture='test.jpg',
            token='token9',
            salt='salt9'
            )
        BaseModel.save(user)
        email = user.email
        self.assertIsInstance(storage.finduser_byemail(email), User)
        self.assertTrue(storage.finduser_byemail(email))
        self.assertEqual(storage.finduser_byemail(email), user)
        self.assertIsNone(storage.finduser_byemail('bata@bata.com'))

    def test_getuser_bytoken(self):
        """Test the get_user_by_token method"""
        user = User(
            name='test10',
            email='test10@test.com',
            password='password',
            phone_number='1234567890',
            picture='test.jpg',
            token='token10',
            salt='salt10'
            )
        BaseModel.save(user)
        token = user.token
        self.assertIsInstance(storage.getuser_bytoken(token), User)
        self.assertTrue(storage.getuser_bytoken(token))
        self.assertEqual(storage.getuser_bytoken(token), user)
        self.assertIsNone(storage.getuser_bytoken('token11111'))

    def test_getItemsbyuser(self):
        """Test the get_items_by_user method"""
        user = User(
            name='test11',
            email='tets11@test.com',
            password='password',
            phone_number='1234567890',
            picture='test.jpg',
            token='token11',
            salt='salt11'
            )
        BaseModel.save(user)
        category1 = Category(
            name='category1',
            picture='category1.jpg'
            )
        location1 = Location(
            name='location1',
            )
        BaseModel.save_all([category1, location1])

        item = Item(
            name='item1',
            description='item1 description',
            picture='item1.jpg',
            user_id=user.id,
            category_id=1,
            location_id=1,
            price=100
            )
        BaseModel.save(item)
        self.assertIsInstance(storage.getItemsbyuser(user.id, 1, 10), list)
        self.assertTrue(storage.getItemsbyuser(user.id, 1, 10))
        self.assertIsInstance(
            storage.getItemsbyuser(user.id, 1, 10)[0], object)


if __name__ == '__main__':
    unittest.main()
