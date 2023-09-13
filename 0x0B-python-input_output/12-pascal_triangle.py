#!/usr/bin/python3

"""
This module defines a function that returns a list of lists of integers

representing the Pascal's triangle of n.
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    result = []  # Initialize the result list
    first_row = [1]  # First row always starts with 1
    result.append(first_row)

    for i in range(1, n):
        prev_row = result[i - 1]
        new_row = [1]  # First element of each row is 1

        for j in range(1, i):
            new_element = prev_row[j - 1] + prev_row[j]
            new_row.append(new_element)

        new_row.append(1)  # Last element of each row is 1
        result.append(new_row)

    return result
