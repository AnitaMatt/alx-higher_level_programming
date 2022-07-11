#!/usr/bin/python3
"""function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """returns the number of characters appended"""
    with open(filename, 'a', encoding="utf-8") as fd:
        num_append = fd.write(text)
    return num_append
