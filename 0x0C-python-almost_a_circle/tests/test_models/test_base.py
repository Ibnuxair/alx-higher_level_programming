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

    if __name__ == '__main__':
        unittest.main()
