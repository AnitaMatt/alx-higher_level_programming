#!/usr/bin/python3
""" checks the type that it is exactly an instance"""


def is_same_class(obj, a_class):
    """returns true of false"""
    if type(obj) == a_class:
        return True
    return False
