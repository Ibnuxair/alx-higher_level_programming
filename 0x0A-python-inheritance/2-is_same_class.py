#!/usr/bin/python3

"""
This module defines a function that returns True if the object is exactly

an instance of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """Cheks if an object is an instance of a class"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
