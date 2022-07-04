#!/usr/bin/python3
""" This module defines a rectangle with width and height"""


class Rectangle:
    """  This defines a rectangle based on 7-rectangle.py"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initializing with a width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                display += str(self.print_symbol)
            display += "\n"
        display = display[:-1]
        return display

    def __repr__(self):
        """returns the string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """deletes an instance  of the class"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """checks two instances of rectangle and the returns a
        a bigger or rect_1 if both are equal"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        a1 = rect_1.area()
        b2 = rect_2.area()

        if a1 >= b2:
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a square with width and height the same as size"""
        return cls(size, size)
