#!/usr/bin/python3
"""Defines a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Reps a Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new square with
           x, y and id as args
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns str rep of a square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """Sets and gets the square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
