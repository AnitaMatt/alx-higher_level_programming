#!/usr/bin/python3
"""This is a class square"""


class Square:
    """Defining a square"""
    def __init__(self, size=0):
        """Initiazies a square class"""
        self.__size = size

    @property
    def size(self):
        """retieves size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting the size of a square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current size area"""
        return (self.__size * self.__size)
