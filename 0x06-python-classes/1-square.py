#!/usr/bin/python3
""" Adding a private instance attribute"""


class Square:
    """ A square class"""
    def __init__(self, size):
        """Initialized a new square with size"""
        self.__size = size
