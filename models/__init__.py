#!/usr/bin/python3
"""
   reloads objects for class
"""
from models.engine import file_storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

cls_dict = {"BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review}


storage = file_storage.FileStorage()
storage.reload()
