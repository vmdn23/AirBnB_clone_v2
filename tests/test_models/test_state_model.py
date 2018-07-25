#!/usr/bin/python3
'''
    Contain tests for the state module.
'''

from os import remove, getenv
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    '''
        Test the State class.
    '''

    @classmethod
    def setUpClass(cls):
        '''
            Sets up unittest
        '''
        cls.new_state = State()
        cls.new_state.name = "Hawaii"

    @classmethod
    def tearDownClass(cls):
        '''
            Tears down unittests
        '''
        del cls.new_state
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_State_inheritence(self):
        '''
            Test that State class inherits from BaseModel.
        '''
        new_state = State()
        self.assertIsInstance(new_state, BaseModel)

    def test_State_attributes(self):
        '''
            Test that State class contains the attribute `name`.
        '''
        new_state = State()
        self.assertTrue("name" in new_state.__dir__())

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db', "state attr")
    def test_State_attributes_type(self):
        '''
            Test that State class attribute name is class type str.
        '''
        new_state = State()
        name = getattr(new_state, "name")
        self.assertIsInstance(name, str)
