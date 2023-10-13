#!/usr/bin/python3
"""
This file contains class
"""
import json


class FileStorage:
    """
    class that serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of all objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in obejts the obj with key
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file.
        """
        serialized_objects = {}
        for key, value in FileStorage.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        """
        from models.base_model import BaseModel
        from models.user import User

        classes = {'BaseModel': BaseModel, 'User': User}

        try:
            data = {}

            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, val in data.items():
                    self.all()[key] = classes[val['__class__']](**val)

        except FileNotFoundError:
            pass
