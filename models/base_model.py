#!/usr/bin/python3
""" Defines all common attributes/methods."""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ Represents the BaseModel of the AirBnB project. """

    def __init__(self):
        """ Initialize a new BaseModel. """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """ Return the print/str representation the BaseModel instance. """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime.
        """
        self.update_at = datetime.today()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of
        __dict__ of the instance.
        """
        rdict = self.__dict__.copy()
        rdict["__class__"] = self.__class__.__name__
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()

        return rdict
