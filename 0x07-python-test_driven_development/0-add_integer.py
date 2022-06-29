#!/usr/bin/python3
"""  This module contains a add function"""


def add_integer(a, b=98):
    """This function takes two arguments, the second has
    a default value of 98"""
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    else:
        return int(a + b)
