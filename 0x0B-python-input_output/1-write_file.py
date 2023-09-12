#!/usr/bin/python3

"""
This module defines a function that writes a string to a text file (UTF8)

and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """Writes to a file and returns the number of xters written."""

    with open(filename, 'w', encoding='utf-8') as a_file:
        a_file.write(text)
        return len(text)
