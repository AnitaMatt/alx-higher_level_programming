#!/usr/bin/python3
"""This is a class square"""


class Square:
    """Defining a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initiazies a square class"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """retieves size value"""
        return self.__size

    @property
    def position(self):
        """retrieves the position of a square"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position of a square"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or (value[0] < 0 and value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

    def my_print(self):
        """Printing a square using size"""
        sizes = self.__size
        yPos = self.__position[1]
        xPos = self.__position[0]
        if (sizes == 0):
            print("")
        else:
            [print("", end="\n") for i in range(yPos)]
            for i in range(sizes):
                [print(" ", end="") for i in range(xPos)]
                [print("#", end="") for i in range(sizes)]
                print()
