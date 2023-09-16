#!/usr/bin/python3

"""
This module defines a function that reads a text file (UTF8)

and prints it to stdout.
"""


def read_file(filename=""):
    """Reads a file and prints it's content."""

    with open(filename, encoding="utf-8") as a_file:
        print(a_file.read(), end="")
