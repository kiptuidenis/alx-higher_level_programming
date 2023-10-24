#!/usr/bin/python3
"""This module contains a class Square"""


class Square:
    """This is a Square class that has attribute size with conditions"""
    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
    def area(self):
        return self.__size * self.__size
