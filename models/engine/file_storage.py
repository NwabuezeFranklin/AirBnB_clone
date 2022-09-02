#!/usr/bin/python3
"""Importing the necessary"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """A json storage unit
    some private class attributes initialized
    __file_path (str): file to save objects to.
    __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new = FileStorage.__objects
        objectdict = {obj: new[obj].to_dict() for obj in new.keys()}
        with open(FileStorage.__file_path, "w") as doc:
            json.dump(objectdict, doc)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file exists"""
        try:
            with open(File.__file_path) as doc:
                objectdict = json.load(doc)
                for o in objectdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
