#!/usr/bin/python3
"""Defines a class MyInt, inherits from int"""


class MyInt(int):
    """Inverts oprs == and !="""

    def __eq__(self, value):
        """Overides == with !="""
        return self.real != value

    def __ne__(self, value):
        """Overides != with =="""
        return self.real == value
