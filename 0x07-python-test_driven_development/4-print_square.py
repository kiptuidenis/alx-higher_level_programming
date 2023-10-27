#!/usr/bin/python3
"""This module has function that prints a square
using the character '#'
"""


def print_square(size):
    """Prints a square of size 'size'
    raises errors if size is not an integer or if size < 0
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            if j < size - 1:
                print("#", end="")
            if j == size - 1:
                print("#")
