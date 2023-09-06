#!/usr/bin/python3

"""
This module contains matrix_divided function that devides

each element of a matrix by the given number (div).
"""


def matrix_divided(matrix, div):
    """
    Divides each number from the matrix by div (number)
    """

    if (
            not isinstance(matrix, list)
            or not all(
                isinstance(row, list)
                and all(isinstance(element, (int, float))
                        for element in row)
                for row in matrix
            )
    ):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats'
        )

    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = [
        [round(element / div, 2) for element in row]
        for row in matrix
    ]

    return new_matrix
