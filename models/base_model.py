#!/usr/bin/python3
"""
This conatins a class calle Basemodel
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    This is a class that defines all common attributes/methods
    for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization...
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue # To skip the class attribute
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
            if 'id' not in kwargs:
                # To generate a unique ID
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                # To set creation timestamp
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now() # Initial update
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        To print
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        """
        class_name = self.__class__.__name__
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = class_name
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
