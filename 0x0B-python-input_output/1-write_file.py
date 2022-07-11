#!/usr/bin/python3
""" function that writes to a string to a text file"""


def write_file(filename="", text=""):
    """ Return the number of charactes written"""
    with open(filename, 'w', encoding="utf-8") as fd:
        count = fd.write(text)
    return count
