#!/usr/bin/python3
"""This module defines the BaseModel class."""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """This Class represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialization of a new BaseModel.

        Args:
            *args (any): Not used.
            **kwargs (dict): The key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """This updates updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """This method returns the dictionary of the BaseModel instance.

        It includes the key/value pair __class__ representing
        the class name of the object.
        """
        r_dict = self.__dict__.copy()
        r_dict["created_at"] = self.created_at.isoformat()
        r_dict["updated_at"] = self.updated_at.isoformat()
        r_dict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
