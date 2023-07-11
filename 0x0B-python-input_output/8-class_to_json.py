#!/usr/bin/python3
"""Defines function that returns dictionary descrption"""


def class_to_json(obj):
    """Module that returns and builds a dictionary"""
    return obj.__dict__
