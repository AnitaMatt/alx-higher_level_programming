#!/usr/bin/python3
"""defines a class student"""


class Student:
    """ A class with one public method and
        three public instance attributes
    """
    def __init__(self, first_name, last_name, age):
        """initializing with three attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of
           Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            j = {}
            for i in attrs:
                if hasattr(self, i):
                    j.update({i: getattr(self, i)})
            return j
