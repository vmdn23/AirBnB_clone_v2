#!/usr/bin/python3

'''
    All the test for the user model are implemented here.
'''

import sys
import unittest
from os import getenv, remove
from models.base_model import BaseModel
from models.user import User
from io import StringIO


class TestUser(unittest.TestCase):
    '''
        Testing User class
    '''

    @classmethod
    def setUpClass(cls):
        '''
            Unittest setup
        '''
        cls.new_usr = User()
        cls.new_usr.email = "betty@holberton.com"
        cls.new_usr.password = "ENIAC"
        cls.new_usr.first_name = "Betty"
        cls.new_usr.last_name = "Holberton"

    @classmethod
    def tearDownClass(cls):
        '''
            Tears down unittests
        '''
        del cls.new_usr
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_User_data_table(self):
        '''
            Check if the tablename is correct
        '''
        self.assertEqual(self.new_usr.__tablename__, "users")

    def test_User_inheritance(self):
        '''
            tests that the User class Inherits from BaseModel
        '''
        new_user = User()
        self.assertIsInstance(new_user, BaseModel)

    def test_User_inheritance_b(self):
        '''
            tests that the User class Inherits from Base
        '''
        new_user = User()
        self.assertIsInstance(new_user, BaseModel)

    def test_User_attributes(self):
        '''
            Test the user attributes exist
        '''

        new_user = User()
        self.assertTrue("email" in new_user.__dir__())
        self.assertTrue("first_name" in new_user.__dir__())
        self.assertTrue("last_name" in new_user.__dir__())
        self.assertTrue("password" in new_user.__dir__())

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db', "email")
    def test_type_email(self):
        '''
            Test the type of name
        '''
        new = User()
        name = getattr(new, "email")
        self.assertIsInstance(name, str)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db', "first_name")
    def test_type_first_name(self):
        '''
            Test the type of name
        '''
        new = User()
        name = getattr(new, "first_name")
        self.assertIsInstance(name, str)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db', "last_name")
    def test_type_last_name(self):
        '''
            Test the type of last_name
        '''
        new = User()
        name = getattr(new, "last_name")
        self.assertIsInstance(name, str)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db', "password")
    def test_type_password(self):
        '''
            Test the type of password
        '''
        new = User()
        name = getattr(new, "password")
        self.assertIsInstance(name, str)
