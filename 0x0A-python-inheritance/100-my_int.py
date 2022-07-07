#!/usr/bin/python3
""" override the existing function with the opposite"""


class MyInt(int):
    """class that changes two operators == and !="""
    def __eq__(self, value):
        """return the opposite"""
        return self.real != value

    def __ne__(self, value):
        """ return the opposite"""
        return self.real == value
