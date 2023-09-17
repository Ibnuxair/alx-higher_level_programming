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

    @property
    def size(self):
        """Getter size."""

        return self.width

    @size.setter
    def size(self, value):
        """Setter for size."""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns arguments to attributes."""

        attributes = ['id', 'size', 'x', 'y']

        if args:
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        else:
            for k, v in kwargs.items():
                if k in attributes:
                    setattr(self, k, v)

    def to_dictionary(self):
        """Return a dictionary representation of the Square."""

        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Return a string representation of a Square instance."""

        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
