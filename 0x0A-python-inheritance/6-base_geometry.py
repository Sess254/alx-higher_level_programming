#!/usr/bin/python3
"""Defines a Basegeometry class"""


class BaseGeometry:
    """Reps base geometry class"""

    def area(self):
        """If not implemented"""
        raise Exception("area() is not implemented")
