#!/usr/bin/python3
"""This is a class square"""


class Square:
    """Defining a square"""
    def __init__(self, size=0):
        """Initiazing a square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
