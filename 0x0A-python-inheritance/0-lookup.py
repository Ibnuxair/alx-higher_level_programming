#!/usr/bin/python3

"""
This is a module that defines a function that returns

the list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    My lookup function.
    """
    attributes_and_methods = dir(obj)
    if attributes_and_methods:
        return attributes_and_methods
    else:
        return []
