#!/usr/bin/python3
"""This module has a function that prints a square with a character #"""


def print_square(size):
    """ printing a square"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
