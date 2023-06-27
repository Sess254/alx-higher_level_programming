#!/usr/bin/python3
"""Define a class square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a new square

        Args:
            size (int): size of the new square.
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns current square area"""
        return self.__size ** 2
