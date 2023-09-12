#!/usr/bin/python3

"""
This module defines a function that creates an Object from a "JSON file".
"""


import json


def load_from_json_file(filename):
    """Creates an object from json file"""

    with open(filename, 'r', encoding='utf-8') as a_file:
        json_content = a_file.read()
        data = json.loads(json_content)
        return data
