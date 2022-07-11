#!/usr/bin/python3
"""function that returns the dictionary description with
    simple data structures(list, dictionary, string, integer and boolean)
    for JSON serialization of an object
"""


def class_to_json(obj):
    """return the dict representation"""
    return obj.__dict__
