#!/usr/bin/python3
"""This module contains a function that adds two numbers
Args: a (int): The first integer
b (int): The second integer
Returns: The sum of the two input integers
"""


def add_integer(a, b=98):
    """Adds two integers and returns the result.
    Args: a , b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
