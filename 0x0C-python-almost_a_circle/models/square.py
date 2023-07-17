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

    def update(self, *args, **kwargs):
        """Updates the square with arg 1-4 to rep
           id, size, x and y respectively
        """
        if args and len(args) != 0:
            c = 0
            for arg in args:
                if c == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif c == 1:
                    self.size = arg
                elif c == 2:
                    self.x = arg
                elif c == 3:
                    self.y = arg
                c += 1

        elif kwargs and len(kwargs) != 0:
            for k, a in kwargs.items():
                if k == "id":
                    if a is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = a
                elif k == "size":
                    self.size = a
                elif k == "x":
                    self.x = a
                elif k == "y":
                    self.y = a

    def to_dictionary(self):
        """Dictionary rep of a Square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
