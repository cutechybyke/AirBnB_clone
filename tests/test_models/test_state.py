#!/usr/bin/python3
""" this is a module that tests file: state.py """

from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ For class that tests the state.py"""

    def __init__(self, *args, **kwargs):
        """ For the constructor for the test_state class """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ For more testing of state name"""
        new = self.value()
        self.assertNotEqual(type(new.name), str)
