#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    """computes the square value of all integers of a matrix using map
    """

    new_matrix = list(map(lambda row: list(map(lambda x: x**2, row)), matrix))
    return new_matrix
