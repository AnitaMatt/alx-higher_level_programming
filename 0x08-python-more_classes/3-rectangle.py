#!/usr/bin/python3
""" This module defines a rectangle with width and height"""


class Rectangle:
    """  This defines a rectangle based on 2-rectangle.py"""
    def __init__(self, width=0, height=0):
        """ initializing with a width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ retieves the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrives the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """prints the rectangle with the character #"""
        display = ""
        if self.__height == 0 or self.__width == 0:
            return display
        for i in range(self.__height):
            for j in range(self.__width):
                display += "#"
            display += "\n"
        return display
