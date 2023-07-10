#!/usr/bin/python3
"""Defines an if the obj is excatly an instance of specified class"""


def is_same_class(obj, a_class):
    """Returns true if obj is of exact class otherwise false"""
    return type(obj) is a_class
