#!/usr/bin/python3

"""
This module defines a class named Rectangle that inherits

from BaseGeometry (7-base_geometry.py).
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def print_info(self):
        print("[Rectangle] {}/{}".format(self.__width, self.__height))

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
