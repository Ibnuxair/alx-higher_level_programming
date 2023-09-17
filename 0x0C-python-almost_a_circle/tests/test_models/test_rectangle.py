#!/usr/bin/python3

"""
This module defines a class named TestRectangle.
"""


import unittest
import io
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests Rectangle class."""

    def test_empty_constructor(self):
        """Test the constructor with no arguments."""

        with self.assertRaises(TypeError):
            rect = Rectangle()

    def test_constructor(self):
        """Test the constructor."""

        rect = Rectangle(10, 20, 4, 7, 15)

        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 7)
        self.assertEqual(rect.id, 15)

    def test_setters(self):
        """Test with valid values."""

        rect = Rectangle(10, 20)

        rect.width = 30
        rect.height = 40
        rect.x = 5
        rect.y = 15
        rect.id = 42

        self.assertEqual(rect.width, 30)
        self.assertEqual(rect.height, 40)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 15)
        self.assertEqual(rect.id, 42)

    def test_invalid_setters(self):
        """Test invalid values."""

        rect = Rectangle(10, 20)

        with self.assertRaises(TypeError):
            rect.width = "invalid"

        with self.assertRaises(ValueError):
            rect.width = -5

        with self.assertRaises(TypeError):
            rect.height = "invalid"

        with self.assertRaises(ValueError):
            rect.height = 0

        with self.assertRaises(TypeError):
            rect.x = "invalid"

        with self.assertRaises(ValueError):
            rect.x = -1

        with self.assertRaises(TypeError):
            rect.y = "invalid"

        with self.assertRaises(ValueError):
            rect.y = -1

    def test_area(self):
        """Test the area of the rectangle."""

        rect = Rectangle(3, 2)
        self.assertEqual(rect.area(), 6)

        rect = Rectangle(2, 10)
        self.assertEqual(rect.area(), 20)

        rect = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(rect.area(), 56)

    def test_display(self):
        """Tests the display function."""

        rect = Rectangle(4, 6)
        output = "####\n####\n####\n####\n####\n####\n"

        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rect.display()
            self.assertEqual(mock_stdout.getvalue(), output)

            rect = Rectangle(2, 2)
            output = "##\n##\n"

        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rect.display()
            self.assertEqual(mock_stdout.getvalue(), output)

    def test_update(self):
        """Test the update method."""

        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(10, 20, 30, 40, 50)
        self.assertEqual(rect.__str__(), "[Rectangle] (10) 40/50 - 20/30")

        rect.update(100)
        self.assertEqual(rect.__str__(), "[Rectangle] (100) 40/50 - 20/30")

        rect.update(id=99, width=11, height=12, x=13, y=14)
        self.assertEqual(rect.__str__(), "[Rectangle] (99) 13/14 - 11/12")

        rect.update()
        self.assertEqual(rect.__str__(), "[Rectangle] (99) 13/14 - 11/12")

        rect.update(id=10, width=20, height=30, x=40, y=50, invalid=60)
        self.assertEqual(rect.__str__(), "[Rectangle] (10) 40/50 - 20/30")

    def test_to_dictionary(self):
        """Test the to_dictionary method."""

        rect = Rectangle(10, 20, 4, 7, 15)
        expected = {
            'id': 15,
            'width': 10,
            'height': 20,
            'x': 4,
            'y': 7
        }
        self.assertEqual(rect.to_dictionary(), expected)

    def test_str(self):
        """Test the __str__ method."""

        rect = Rectangle(10, 20, 4, 7, 15)
        output = "[Rectangle] (15) 4/7 - 10/20"
        self.assertEqual(rect.__str__(), output)

        rect = Rectangle(5, 5, 1, 1, 42)
        output = "[Rectangle] (42) 1/1 - 5/5"

        self.assertEqual(rect.__str__(), output)

    if __name__ == '__main__':
        unittest.main()
