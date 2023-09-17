#!/usr/bin/python3

"""
This module defines a class named TestBase.
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests Base class."""

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

    def test_to_json_string_valid_list(self):
        """Test to_json_string with a valid list of dictionaries."""

        dicts = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
        json_str = Base.to_json_string(dicts)
        expected = '[{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]'
        self.assertEqual(json_str, expected)


    if __name__ == '__main__':
        unittest.main()
