#!/usr/bin/python3

"""
This module defines a class named Student.
"""


class Student:
    """A class representing a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        student_dict = self.__dict__

        serialized_dict = {}

        for k, v in student_dict.items():
            if isinstance(v, (list, dict, str, int, bool)):
                serialized_dict[k] = v

        return serialized_dict
