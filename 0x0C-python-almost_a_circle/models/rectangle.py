#!/usr/bin/python3
"""A class rectangle that inherits from Base class"""
from models.base import Base


class Rectangle(Base):
    """ A class rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializing the rectangle """
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """retrieves the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """validates the value before setting"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ retrieves the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """validates the value of height bf setting"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ retrieves the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """validates the value of x before setting"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise TypeError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Retrives the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """ Validates the value of y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
