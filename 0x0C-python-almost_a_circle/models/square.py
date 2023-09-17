#!/usr/bin/python3

"""
This module defines a class named Square.

The class inherits from Rectangle.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A class representing a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the attributes."""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of a Square instance."""

        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
