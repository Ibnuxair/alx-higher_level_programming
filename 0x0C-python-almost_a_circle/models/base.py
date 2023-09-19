#!/usr/bin/python3

"""
This is a module that defines a class named Base
"""


import json
import os


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
        """Convert a list of dictionaries to a JSON string."""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        if all(isinstance(item, dict) for item in list_dictionaries):
            return json.dumps(list_dictionaries)

        # Convert objects to dictionaries and then to JSON
        dict_list = []
        for item in list_dictionaries:
            if hasattr(item, 'to_dictionary'):
                dict_list.append(item.to_dictionary())
            elif isinstance(item, dict):
                dict_list.append(item)

        return json.dumps(dict_list)

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries."""

        if json_string is None or json_string == "":
            return []

        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""

        if list_objs is None or len(list_objs) == 0:
            list_objs = []

        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as a_file:
            json_str = cls.to_json_string(list_objs)
            a_file.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes from a dictionary."""

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)  # Apply attributes from the dictionary
        return dummy

    def update(self, *args, **kwargs):
        """Update attributes using arguments or keyword arguments."""

        attributes = ["id", "width", "height", "x", "y"]

        if args:
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
        else:
            for k, v in kwargs.items():
                if k in attributes:
                    setattr(self, k, v)

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a JSON file."""

        filename = cls.__name__ + ".json"
        instances_list = []

        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                json_data = file.read()
                if json_data:
                    json_list = cls.from_json_string(json_data)
                    for item in json_list:
                        instance = cls.create(**item)
                        instances_list.append(instance)

        return instances_list
