#!/usr/bin/python3
"""Defines an inherited list of class MyList"""


class MyList(list):
    """impliments printing of sorted list class"""

    def print_sorted(self):
        """Prints a list in sorted(ascending) order"""
        print(sorted(self))
