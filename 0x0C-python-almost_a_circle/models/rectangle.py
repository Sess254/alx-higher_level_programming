#!/usr/bin/python3
"""Defines a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Reps a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new Rectangle with width
           length, x, y, id as args
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Sets and gets the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Sets and gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Sets and gets the x coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """sets and gets the y coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle using #"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for he in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for wd in range(self.width)]
            print("")

    def __str__(self):
        """Returns the print and str rep of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
