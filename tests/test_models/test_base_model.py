#!/usr/bin/python3
"""Test BaseModel for expected behavior with a test_database"""
import sys
import unittest
import os

# Add the parent directory of the current script to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
parent_dir = os.path.dirname(parent_dir)
sys.path.append(parent_dir)

from models import storage
from models.base_model import BaseModel
from models.user import User


class TestBaseModel(unittest.TestCase):
    """this will test the BaseModel class"""
    def test_base_model_init(self):
        """test the initialization of the base model class"""
        data = {
            'id': 1,
            'name': 'test',
            'email': 'test@example.com',
            'password': 'password',
            'phone_number': '1234567890',
            'picture': 'test.jpg',
            'token': 'token123',
            'salt': 'salt123'
        }
        model = BaseModel(**data)
        for key, value in data.items():
            self.assertEqual(getattr(model, key), value)

    def test_base_model_save(self):
        """test the save method of the base model class"""
        user1 = User(
            name='hamza',
            email='hamza@example.com',
            password='password5',
            phone_number='1234567890',
            token='2356',
            salt='salt123')
        self.assertTrue(BaseModel.save(user1))
        self.assertTrue(user1.id)

    def test_base_model_save_all(self):
        """test the save_all method of the base model class"""
        user1 = User(
            name='ham',
            email='ham@example.com',
            password='password5',
            phone_number='1234567890',
            token='235',
            salt='salt12')
        user2 = User(
            name='roka',
            email='roka@google.com',
            password='password5',
            phone_number='1234567890',
            token='256',
            salt='sa23')
        BaseModel.save_all([user1, user2])
        self.assertTrue(user1.id)
        self.assertTrue(user2.id)

    def test_base_model_delete(self):
        """test the delete method of the base model class"""
        user1 = storage.get(User, 1)
        BaseModel.delete(user1)
        self.assertIsNone(storage.get(User, 1))


if __name__ == '__main__':
    unittest.main()
