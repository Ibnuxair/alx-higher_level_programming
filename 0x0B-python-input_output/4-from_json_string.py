#!/usr/bin/python3

"""
This module defines a function that returns an object (Python data structure)

represented by a JSON string.
"""


import json


def from_json_string(my_str):
    """Returns an obj representing by a json string."""

    data = json.loads(my_str)
    return data
