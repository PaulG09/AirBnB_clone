#!/usr/bin/python3
"""Defines class FileStorage[serializes/deserializes JSON file to instances]"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """class FileStorage that serializes instances to a JSON file and
    deserializes JSON file to instances

    Attributes:
        __file_path (str): string - path to the JSON file
        __objects (dict): dictionary - empty but will store
        all objects by <class name>.id
    """

    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """Sets in __objects the 'obj' with <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def all(self):
        """returns the dictionary __objects containing all stored objects"""
        return self.__objects

    def save(self):
        """serializes __objects to the JSON file(path: __filepath)"""
        sterObj = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(sterObj, file)

    def reload(self):
        """deserializes the JSON file to __objects
        (if the JSON file (__file_path) exists
        """
        try:
            with open(FileStorage.__file_path) as f:
                sterObj = json.load(f)
                for value in sterObj.values():
                    class_name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(class_name)(**value))
        except FileNotFoundError:
            return
