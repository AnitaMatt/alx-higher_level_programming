#!/usr/bin/python3
""" function that reads a text file and prints to stdout"""


def read_file(filename=""):
    """use UTF8 encoding"""
    with open(filename, encoding="utf-8") as fd:
        for line in fd:
            print(line, end="")
