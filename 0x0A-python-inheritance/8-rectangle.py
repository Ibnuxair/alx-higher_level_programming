#!/usr/bin/python3

"""
This module defines a class Rectangle that inherits from

BaseGeometry (7-base_geometry.py).
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """
    A class representing rectangle.
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
