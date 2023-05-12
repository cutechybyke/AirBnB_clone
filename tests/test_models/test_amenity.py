#!/usr/bin/python3
"""for testing Amenity """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """to test for amenity """

    def __init__(self, *args, **kwargs):
        """for arguments"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """To test name """
        new = self.value()
        self.assertEqual(type(new.name), str)
