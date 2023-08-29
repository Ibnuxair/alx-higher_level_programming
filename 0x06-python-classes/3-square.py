#!/usr/bin/python3

"""
This is a module that defines a class named Square.
"""


class Square:
    """
    This class represents a square.
    """
    def __init__(self, size=0):
        """
        Initialize a square instance with a given size.

        Args:
            size: The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate the area of a square.

        Returns:
               int: The current square area.
        """
        return self.__size ** 2
