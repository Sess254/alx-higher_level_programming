#!/usr/bin/python3
"""Defines a square by inheriting from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Applies the geometry from rectangle to square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Area of the obj"""
        return self.__size * self.__size

    def __str__(self):
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
