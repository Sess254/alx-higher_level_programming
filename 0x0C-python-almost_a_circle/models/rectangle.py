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
