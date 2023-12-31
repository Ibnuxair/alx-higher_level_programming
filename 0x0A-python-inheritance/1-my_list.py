#!/usr/bin/python3

"""
This module defines a class named MyList that inherits from list.
"""


class MyList(list):
    """A class that inherits from a list class."""

    def print_sorted(self):
        """Prints my list in ascending sorted order."""

        if not self:
            print("The list is empty.")
        elif not all(isinstance(element, int) for element in self):
            print("All the elements shoud be integer!")

        else:
            sorted_list = sorted(self)
            print(sorted_list)
