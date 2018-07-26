#!/usr/bin/python3
'''
    Testing db_storage module
'''
import unittest
from models.engine.db_storage import DBStorage
from models.state import State
from models.user import User
from os import getenv


@unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db', "DB tests")
class testDBStorage(unittest.TestCase):
    '''
        DBStorage class testing
    '''
    def test_docstring(self):
        '''
        check that docstring exist
        '''
        self.assertTrue(len(DBStorage.__doc__) > 1)
        self.assertTrue(len(DBStorage.all.__doc__) > 1)
        self.assertTrue(len(DBStorage.new.__doc__) > 1)
        self.assertTrue(len(DBStorage.save.__doc__) > 1)
        self.assertTrue(len(DBStorage.reload.__doc__) > 1)

    def test_pep8(self):
        '''
        test pep8 comes back clean
        '''
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/db_storage'])
        self.assertEqual(result.total_errors, 0, "pep8")

    @classmethod
    def setUpClass(cls):
        '''
            Initialize class
        '''
        cls.storage = DBStorage()

    @classmethod
    def tearDownClass(cls):
        '''
            Deletes and resets class
        '''
        del cls.storage

    def test_new_DBStorage(self):
        '''
            Tests the new DB
        '''
        obj = State(name="Hawaii")
        self.assertEqual(obj.name, "Hawaii")

    def test_DBStorage_user_attr(self):
        '''
            Tests User attributes
        '''
        new_usr = User(email="betty@holberton.com", password="ENIAC")
        self.assertTrue(new_usr.email, "betty@holberton.com")
        self.assertTrue(hasattr(new_usr, "__tablename__"))
        self.assertTrue(hasattr(new_usr, "email"))
        self.assertTrue(hasattr(new_usr, "password"))
        self.assertTrue(hasattr(new_usr, "first_name"))
        self.assertTrue(hasattr(new_usr, "last_name"))
