#!/usr/bin/python3

"""
This module defines a class named TestSquare.
"""


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for the Square class."""

    def test_empty_constructor(self):
        """Test the constructor with no arguments."""

        with self.assertRaises(TypeError):
            square = Square()

    def test_constructor(self):
        """Test the constructor."""

        square = Square(5, 2, 3, 42)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 42)

    def test_size_property(self):
        """Test the size property."""

        square = Square(4)
        square.size = 7
        self.assertEqual(square.size, 7)
        self.assertEqual(square.width, 7)
        self.assertEqual(square.height, 7)

    def test_update_method(self):
        """Test the update method."""

        square = Square(5, 2, 3, 42)
        square.update(1, 10, 20, 30)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 20)
        self.assertEqual(square.y, 30)

    def test_str_method(self):
        """Test the __str__ method."""

        square = Square(3, 2, 4, 10)
        self.assertEqual(square.__str__(), "[Square] (10) 2/4 - 3")

    if __name__ == '__main__':
        unittest.main()
