#!/usr/bin/python3
""" function that returns true if the object is exactly an instance
 of the class"""


def is_kind_of_class(obj, a_class):
    """ returns true or false"""
    if not isinstance(obj, a_class):
        return False
    return True
