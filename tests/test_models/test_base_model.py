#!/usr/bin/python3
"""
   unittest suite for model/base_model.py
"""
import unittest
from models.base_model import BaseModel


class TestBaseClass(unittest.TestCase):
    """class TestBaseClass"""

    def test_id(self):
        """id attr test"""
        model = BaseModel()
        self.assertEqual(str, type(model.id))
