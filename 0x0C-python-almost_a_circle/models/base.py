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

    @staticmethod
    def from_json_string(json_string):
        """converts json to python"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates a new instance from a dictionary"""
        if dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """return a list of instance after reading a json file"""
        filename = cls.__name__ + ".json"

        try:
            with open(filename, encoding="utf-8") as jfile:
                """this reads a json file and turns it to python"""
                list_dicts = Base.from_json_string(jfile.read())
                return [cls.create(**dicts) for dicts in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        """saving to a file"""
        filename = cls.__name__ + ".json"

        with open(filename, 'w', encoding='utf-8') as fd:
            if list_objs is None:
                fd.write("[]")
            else:
                dict_list = []
                for r in list_objs:
                    dict_list.append(r.to_dictionary())
                fd.write(cls.to_json_string(dict_list))
