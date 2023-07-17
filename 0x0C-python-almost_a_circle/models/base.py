#!/usr/bin/python3
"""Defines a base model class"""
import json
import csv


class Base:
    """Represnts a base model for all classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new base with id as args"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the json string rep of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Return the JSON string rep of list_obj to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(list_dict))
