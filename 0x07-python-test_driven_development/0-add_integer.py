#!/usr/bin/python3

"""Defines an integer addition function"""


def add_integer(a, b=98):
    """Returns addition of two integers a and b.

    Float arguments are changed to ints befor addition is done

    Raises:
        TypeError if a or b are not int integers of float integers
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
