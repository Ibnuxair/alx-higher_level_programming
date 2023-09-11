#!/usr/bin/python3

"""
This module defines a  function that returns True if the obj is an instance of

a class that inherited (directly or indirectly) from the specified class;

otherwise False.
"""


def inherits_from(obj, a_class):

    """Checks the object."""

    if type(obj) == a_class:
        return False

    base_classes = obj.__class__.__bases__
    for base_class in base_classes:
        if base_class == a_class or inherits_from(base_class, a_class):
            return True

    return False
