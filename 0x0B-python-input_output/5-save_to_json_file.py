#!/usr/bin/python3
"""Defines a save Object to file function"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an obj to a text file using JSON rep"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
