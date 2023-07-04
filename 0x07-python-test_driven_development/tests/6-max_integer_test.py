#!/usr/bin/python3

"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests function max_integer."""
    def test_empty(self):
        """Checks if it is iterable and not empty."""
        self.assertTrue(len(list))

    def test_values(self):
        """Checks that the values in list are integers."""
        for i in list:
            self.assertIsInstance(i, int)
