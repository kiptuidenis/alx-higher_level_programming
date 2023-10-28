#!/usr/bin/python3
"""
This module multiplies two matrices

"""


def matrix_mul(m_a, m_b):
    """This function multiplies two matrices and returns the result

    Args:
        m_a (list): Matrix A
        m_b (list): Matrix B
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not m_a or (len(m_a) == 1 and not m_a[0]):
        raise ValueError("m_a can't be empty")
    if not m_b or (len(m_b) == 1 and not m_b[0]):
        raise ValueError("m_b can't be empty")

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")

    for row in m_a:
        for ints in row:
            if not isinstance(ints, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for ints in row:
            if not isinstance(ints, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    for i in range(len(m_a)):
        if len(m_a[0]) != len(m_a[i]):
            raise TypeError("each row of m_a must be of the same size")

    for i in range(len(m_b)):
        if len(m_b[0]) != len(m_b[i]):
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    m_c = [[sum(m_a[i][k] * m_b[k][j] for k in range(len(m_a[0])))
            for j in range(len(m_b[0]))] for i in range(len(m_a))]

    return m_c
