#!/usr/bin/python3
"""checks if an object is a subclass"""


def inherits_from(obj, a_class):
    """checks if an object inherits from anothe object"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
