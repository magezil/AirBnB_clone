#!/usr/bin/python3
"""
   unittest suite for model/engine/file_storage.py
"""
import unittest
import sys
import os
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from datetime import datetime
from io import StringIO


class TestFileStorageClass(unittest.TestCase):
    """class TestFileStorageClass"""

    def test_save_file(self):
        """tests save method makes file"""
        m = BaseModel()
        m.save()
        self.assertEqual(True, os.path.isfile('storage.json'))

    def test_save_file_size(self):
        """tests save method makes non_empty file"""
        m = BaseModel()
        m.save()
        self.assertEqual(True, os.stat('storage.json').st_size != 0)

    def test_reload_file_dictionary(self):
        """tests reload method returns dictionary"""
        m = BaseModel()
        m.save()
        obj = storage.all()
        self.assertEqual(dict, type(obj))

    def test_reload_file_dictionary_objects(self):
        """tests reload method returns dictionary of objects"""
        m = BaseModel()
        m.save()
        all_objs = storage.all()
        for obj_key in all_objs.keys():
            obj = all_objs[obj_key]
            break
        self.assertEqual(True, issubclass(type(obj), type(BaseModel())))
