#!/usr/bin/python3

"""
This is a module that contains add_integer function.

The module will be imported in to it's test file.
"""
def add_integer(a, b=98):
    """
    Adds two integer numbers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    return (a + b)
