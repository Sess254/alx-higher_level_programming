#!/usr/bin/python3
"""Defines a from JSON string to object function"""
import json


def from_json_string(my_str):
    """Returns an object rep by a JSON string"""
    return json.loads(my_str)
