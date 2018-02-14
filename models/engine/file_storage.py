#!/usr/bin/python3
import json
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


class FileStorage:
    """serializes instances -> json file and deserializes
    json fle -> instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Args:
                obj: object
        """
        if obj:
            self.__objects["{}.{}".format(str(type(obj).__name__),
                                          obj.id)] = obj

    def save(self):
        """serializes __objects to __file_path"""
        obj_dict = {}
        for k in self.__objects:
            obj_dict[k] = self.__objects[k].to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """deserializes __objects from __file_path"""
        try:
            with open(self.__file_path, encoding="UTF-8") as f:
                obj = json.load(f)
            for obj_id in obj:
                self.__objects[obj_id] = cls_dict[obj[obj_id]
                                                  ['__class__']](**obj[obj_id])
        except FileNotFoundError:
            pass
