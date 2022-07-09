#!/usr/bin/python3
""" Unittest for max_integer([...])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Testing max_integer with diff methods"""

    def test_ordered_list(self):
        """A list that has the max at the end"""
        ordered = [2, 4, 6, 8]
        self.assertEqual(max_integer(ordered), 8)

    def test_unorderd_list(self):
        """ A list that has max in the middle"""
        unordered = [2, 4, 8, 6]
        self.assertEqual(max_integer(unordered), 8)

    def test_max_at_beginning(self):
        """ A list with max at the beginning"""
        max_at_begin = [10, 5, 2, 1]
        self.assertEqual(max_integer(max_at_begin), 10)

    def test_empty_list(self):
        """ An empty list"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_only_one_element(self):
        """only one element in the list"""
        only_one = [20]
        self.assertEqual(max_integer(only_one), 20)

    if __name__ == '__main__':
        unittest.main()
