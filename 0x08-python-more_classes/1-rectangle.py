#!/usr/bin/python3
"""
This is a module that defines a class named rectangle.
"""


class Rectangle:
    """
    A class representing a rectangle.
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def __str__(self):
        return (
            f"{{'_Rectangle__height': {self.__height}, "
            f"'_Rectangle__width': {self.__width}}}"
        )
