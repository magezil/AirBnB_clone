#!/usr/bin/python3
"""
   reloads objects for class
"""
from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
