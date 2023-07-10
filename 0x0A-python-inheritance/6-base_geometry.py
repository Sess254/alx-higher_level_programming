#!/usr/bin/python3
"""Defines a Basegeometry class"""


class BaseGeometry:
    """Impliments area with exception if not implemented"""
    def area(self):
        raise Exception("area () is not implemented")
