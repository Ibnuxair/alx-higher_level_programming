#!/usr/bin/python3

"""
This is a module that defines a class named Square.
"""


class Square:
    """
    This class represents a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a square instance with a given size.

        Args:
            size: The size of the square.
            position: The position.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Getter to get the size of the square. """
        return self.__size

    @property
    def position(self):
        """ Getter to get the position. """
        return self.__position

    @size.setter
    def size(self, size):
        """ Setter to set new size. """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @position.setter
    def position(self, value):
        """ Setter to set the position."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not all(isinstance(val, int) and val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of a square.

        Returns:
               int: The current square area.
        """
        return self.size ** 2

    def my_print(self):
        """ Prints in stdout the square with the character #."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print("_" * self.__position[0] + "#" * self.__size)
