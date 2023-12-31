#!/usr/bin/python3
"""This module generates the Pascal's Triangle
"""


def pascal_triangle(n):
    """that returns a list of lists of integers
    representing the Pascal’s triangle of n:
    Args:
        n (integer):
    """
    triangle = []

    if n <= 0:
        return triangle

    else:
        triangle = [[1]]
        i = 0
        j = 1
        prev = triangle[i]
        new_row = [1]

        while (j < n):
            for k in range(len(prev)):
                if k == len(prev) - 1:
                    elem = prev[k]
                else:
                    elem = prev[k] + prev[k + 1]
                new_row.append(elem)
            triangle.append(new_row)
            new_row = [1]
            i += 1
            j += 1
            prev = triangle[i]
    return triangle
