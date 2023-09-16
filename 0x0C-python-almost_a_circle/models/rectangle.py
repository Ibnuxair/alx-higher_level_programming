#!/usr/bin/python3

"""
This is a module that defines a class named Rectangle.

It inherits from Base class.
"""

from models.base import Base


class Rectangle(Base):
    """A class representing a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes ojects' attributes."""

        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    @property
    def width(self):
        """Returns the width."""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width."""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height.."""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height."""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns the x."""

        return self.__x

    @x.setter
    def x(self, value):
        """Sets x."""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns the y."""

        return self.__y

    @y.setter
    def y(self, value):
        """Sets y."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def id(self):
        """Returns the id."""

        return self.__id

    @id.setter
    def id(self, value):
        """Sets the id."""

        self.__id = value

    def area(self):
        """Calculate and return the area of the rectangle."""

        return self.__width * self.__height
