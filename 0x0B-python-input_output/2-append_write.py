#!/usr/bin/python3

"""
This module defines a function that appends a string at the end of a text file

(UTF8) and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """Appends a string to a file and return the num of xters added."""

    with open(filename, 'a', encoding='utf-8') as a_file:
        a_file.write(text)
        return len(text)
