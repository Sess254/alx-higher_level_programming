#!/usr/bin/python3
"""Defines a Basegeometry class"""


class BaseGeometry:
    """Reps base geometry class"""

    def area(self):
        """If not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a param as an int"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
