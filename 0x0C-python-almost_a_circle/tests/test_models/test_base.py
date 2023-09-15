#!/usr/bin/python3

"""
This module defines a class named Test_base.
"""


import unittest
from models.base import Base


class Test_base(unittest.TestCase):
    """Tests Base class"""

    def test_id(self):
        """Tests the  id"""

        obj1 = Base(150)
        self.assertEqual(obj1.id, 150)

    def test_default_id(self):
        """Tests default id"""

        obj1 = Base()
        obj2 = Base()
        self.assertNotEqual(obj1.id, obj2.id)

    if __name__ == '__main__':
        unittest.main
