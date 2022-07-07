#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """Class that inherits from list"""
    def print_sorted(self):
        """pritns list in sorted ascending order"""
        print(sorted(self))
