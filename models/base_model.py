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

        Args:
            *args (any): Not used
            **kwargs (dict): Key/value pairs of attributes
        """

        self.id = str(uuid.uuid4())  # To generate a unique ID
        self.created_at = datetime.now()  # To set creation timestamp
        self.updated_at = datetime.now()  # Initial update

        timefmt = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, timefmt)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """
        To print
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
        )

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
