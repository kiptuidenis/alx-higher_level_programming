#!/usr/bin/python3
"""This module defines a square"""


class Square:
    """This class defines a square by
    1. Private instance attribute size
    2. Instantiation with size (no type/value verification)
    """
    def __init__(self, size):
        self.__size = size
