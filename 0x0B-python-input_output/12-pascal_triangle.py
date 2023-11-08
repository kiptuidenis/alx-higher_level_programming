#!/usr/bin/python3
"""This module generates the Pascal's Triangle
"""


def pascal_triangle(n):
    """that returns a list of lists of integers representing the Pascal’s triangle of n:

    Args:
        n (integer): 
    """
    triangle = []

    if n <= 0:
        return triangle
    if n == 1:
        triangle = [[1]]
        return triangle
    if n == 2:
        triangle = [[1], [1, 1]]
        return triangle
    if n > 2:
        triangle = [[1], [1, 1]]
        i = 1
        j = 2
        prev = triangle[i]
        new = [1]

        while(j < n):
            for k in range(len(prev)):
                if k == len(prev) - 1:
                    elem = prev[k]
                else:
                    elem = prev[k] + prev[k + 1]
                new.append(elem)
            triangle.append(new)
            new = [1]
            i += 1
            j += 1
            prev = triangle[i]
    return triangle
