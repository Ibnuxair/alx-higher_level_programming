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
        """
        Initialize a Rectangle object with width and height.
        """

        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """
        Calculate and return the area of the rectangle.
        """
        return self.__width * self.__height

    def __print__(self):
        """
        Print the rectangle description.
        """
        print("[Rectangle] {}/{}".format(self.__width, self.__height))

    def __str__(self):
        """
        Return a string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
