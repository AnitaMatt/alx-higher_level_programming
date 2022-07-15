#!/usr/bin/python3
"""defining a class Square based on the rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class Square that inherits from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """call the super method and initiaize"""
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """updatess the square class"""
        if args is not None and len(args) != 0:
            list_args = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_args[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """returns the dictionary representation"""
        list_atr = ['id', 'size', 'x', 'y']
        ret_dict = {}

        for k in list_atr:
            ret_dict[k] = getattr(self, k)
        return ret_dict

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
