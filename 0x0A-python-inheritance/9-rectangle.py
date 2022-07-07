#!/usr/bin/python3
"""a class rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class based on 8-base_geometry.py"""
    def __init__(self, width, height):
        """instantiation with validated width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        word = "[{}] {:d}/{:d}".format(self.__class__.__name__,
                                       self.__width, self.__height)
        return word
