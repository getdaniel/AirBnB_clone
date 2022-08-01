#!/usr/bin/python3
""" Defines unitests for models/base_model.py."""
from models.base_model import BaseModel
import unittest
from datetime import datetime
from time import sleep


class TestBaseModel_instatiation(unittest.TestCase):
    """ Unittests for testing instatiation of the class."""

    def test_no_args_instantiations(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel(), id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

class testBaseModel_save(unittest.TestCase):
    """ Unittest for the save method of BaseModel. """

    def test_one_save(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

if __name__ == "__main__":
    unittest.main()
