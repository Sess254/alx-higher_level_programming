#!/usr/bin/python3
"""Defines a file from JSON file function"""
import json


def load_from_json_file(filename):
    """Creates an object from a json file"""
    with open(filename) as file:
        return json.load(file)
