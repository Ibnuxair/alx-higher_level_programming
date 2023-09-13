#!/usr/bin/python3

"""
Defines a function that returns the dictionary description with simple data

structure for JSON serialization of an object:
"""


def class_to_json(obj):
    """Returns the dictionary description."""

    obj_dict = obj.__dict__

    serialized_dict = {}

    for k, v in obj_dict.items():
        if isinstance(v, (list, dict, str, int, bool)):
            serialized_dict[k] = v

    return serialized_dict
