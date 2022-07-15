#!/usr/bin/python3
"""This file will contain a base class"""
import json


class Base:
    """This is the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initiazing an instance of the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return the JSON representation"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
