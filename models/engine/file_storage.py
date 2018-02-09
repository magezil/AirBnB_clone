#!/usr/bin/python3
import json
import sys

class FileStorage:
    """serializes and deserializes instances from json file"""

    def __init__(self):
        """initializes file path and objects"""
        self.__file_path = "storage.json"
        self.__objects = {}

    def all(self):
        """returns dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Args:
                obj: object
        """
        self.__objects["{}.{}".format(type(obj), obj.id)] = obj

    def save(self):
        """serializes __objects to __file_path"""
        with open(self.__file_path, 'w') as f:
            f.write(json.dump(self.__objects))

    def reload(self):
        """deserializes __objects from __file_path"""
        try:
            with open(self.__file_path) as f:
                json.loads(f.read())
        except FileNotFoundError:
            pass
