#!/usr/bin/python3
"""defining a class Square based on the rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class Square that inherits from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """call the super method and initiaize"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns the size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size and validates, inherits validation from rectangle"""
        self.width = value
        self.height = value

    def __str__(self):
        """returns a str representation of square"""
        return "[{}] ({}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__,
            self.id, self.x, self.y,
            self.size)
