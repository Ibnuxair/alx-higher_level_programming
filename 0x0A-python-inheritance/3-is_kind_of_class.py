#!/usr/bin/python3

"""
This module defines a function that returns True if the obj is an instance of

or if the object is an instance of a class that inherited from, the specified

class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """Checks the object."""

    return isinstance(obj, a_class)
