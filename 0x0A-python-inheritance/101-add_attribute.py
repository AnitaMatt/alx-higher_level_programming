#!/usr/bin/python3
"""function that adds a new attribute if it is possible"""


def add_attribute(obj, attribute, value):
    """adds an atribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
