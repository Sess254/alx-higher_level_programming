#!/usr/bin/python3
"""Defines same instance of class or inherited function"""


def inherits_from(obj, a_class):
    """Returns true if obj is an instance or inherited"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
