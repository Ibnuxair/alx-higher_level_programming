#!/usr/bin/python3

"""
This module defines a function that reads a text file (UTF8)

and prints it to stdout.
"""


def read_file(filename=""):
    """Reads a file"""

    with open(filename, encoding="utf-8") as a_file:
        content = a_file.read().rstrip()
        if not content:
            print("Empty file")
        else:
            print(content)
