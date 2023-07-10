#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Applies geometry to the Rectangles"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """String"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)

    def area(self):
        """Define area of obj"""
        return self.__width * self.__height
