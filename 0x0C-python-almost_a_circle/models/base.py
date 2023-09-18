#!/usr/bin/python3

"""
This is a module that defines a class named Base
"""


import json


class Base:
    """A base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the attributes."""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps([obj.to_dictionary() for obj in list_dictionaries])

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""

        if list_objs is None or len(list_objs) == 0:
            list_objs = []

        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as a_file:
            json_str = cls.to_json_string(list_objs)
            a_file.write(json_str)
