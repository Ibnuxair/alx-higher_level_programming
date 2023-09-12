#!/usr/bin/python3

"""
This module defines a function that writes an Object to a text file,

using a JSON representation.
"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a file."""

    with open(filename, 'w', encoding='utf-8') as a_file:
        json_str = json.dumps(my_obj)
        a_file.write(json_str)
