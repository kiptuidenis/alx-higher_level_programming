#!/usr/bin/python3
"""This module contains a function that divides a matrix by a number
Matrix is a list of lists of integers or floats
Each row of the matrix should be of the same size
''div'' must be an integer or float and should not be zero
The results of the divison are rounded to 2 decimal places
"""


def matrix_divided(matrix, div):
    """Divides a all elements of matrix by ''div''
    Args: matrix - matrix to be divided
          div - number to be divided by
    Return: new matrix containing results of the division
    """
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(ints, (int, float))
                for row in matrix for ints in row)):
        raise TypeError("matrix must be a matrix(list of lists) "
                        "of integers/floats")

    same_length = all(len(row) == len(matrix[0]) for row in matrix)
    if not same_length:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = list(map(lambda row: list(map(lambda x:
                                               round(x/div, 2), row)), matrix))

    return new_matrix
