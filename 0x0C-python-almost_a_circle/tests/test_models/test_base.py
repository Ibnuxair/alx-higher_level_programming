#!/usr/bin/python3

"""
This module defines a class named TestBase.
"""


import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests Base class."""

    def setUp(self):
        """Ensure the test files don't exist before running the tests"""

        if os.path.exists("Base.json"):
            os.remove("Base.json")
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def tearDown(self):
        """Clean up after each test."""

        if os.path.exists("Base.json"):
            os.remove("Base.json")
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_constructor_with_id(self):
        """Test the constructor."""

        base_obj = Base(42)
        self.assertEqual(base_obj.id, 42)

    def test_constructor_without_id(self):
        """Test the constructor."""

        base_obj = Base()
        self.assertTrue(hasattr(base_obj, 'id'))

    def test_to_json_string_empty_list(self):
        """Test to_json_string with an empty list."""

        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_none(self):
        """Test to_json_string with None."""

        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_save_to_file_empty_list(self):
        """Test saving an empty list of objects to a file."""

        Base.save_to_file([])
        self.assertTrue(os.path.exists("Base.json"))

    def test_to_json_string_empty_list(self):
        """Test to_json_string with an empty list."""

        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_none(self):
        """Test to_json_string with None."""

        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test__from_json_string_empty(self):
        """Test with an empty JSON string."""

        json_string = ""
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])

    def test_from_json_string_none(self):
        """Test with a None JSON string."""

        json_string = None
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])

    def test_from_json_string_valid(self):
        """Test with a valid JSON string."""

        json_string = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        expected_result = [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
        result = Base.from_json_string(json_string)
        self.assertEqual(result, expected_result)

    def test_create_with_empty_dictionary(self):
        """Test creating an instance with an empty dictionary."""

        obj = Base.create(**{})
        self.assertIsInstance(obj, Base)

    def test_create_with_rectangle_attributes(self):
        """Test creating a Rectangle instance with attributes."""

        rect_dict = {'width': 10, 'height': 5, 'x': 2, 'y': 3}
        obj = Rectangle.create(**rect_dict)
        self.assertIsInstance(obj, Rectangle)
        self.assertEqual(obj.width, 10)
        self.assertEqual(obj.height, 5)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 3)

    def test_create_with_square_attributes(self):
        """Test creating a Square instance with attributes."""

        square_dict = {'size': 5, 'x': 2, 'y': 3}
        obj = Square.create(**square_dict)
        self.assertIsInstance(obj, Square)
        self.assertEqual(obj.size, 5)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 3)

    def test_create_with_mixed_attributes(self):
        """Test creating an instance with mixed attributes."""

        mixed_dict = {'id': 1, 'size': 5, 'x': 2}
        obj = Square.create(**mixed_dict)

        if isinstance(obj, (Rectangle, Square)):
            if isinstance(obj, Rectangle):
                self.assertEqual(obj.width, 5)
                self.assertEqual(obj.height, 5)
            elif isinstance(obj, Square):
                self.assertEqual(obj.size, 5)
        else:
            self.fail(f"Unexpected object type: {type(obj).__name__}")

    def test_load_from_non_existing_file(self):
        """Test loading from a non-existing file."""

        result = Rectangle.load_from_file()
        self.assertEqual(result, [])

    def test_load_from_existing_file(self):
        """Test loading from an existing file."""

        rect = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([rect])
        result = Rectangle.load_from_file()
        self.assertEqual(result[0].to_dictionary(), rect.to_dictionary())

    if __name__ == '__main__':
        unittest.main()
