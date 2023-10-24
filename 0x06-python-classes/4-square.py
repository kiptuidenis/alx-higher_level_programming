#!/usr/bin/python3
"""This module contains a class Square"""


class Square:
    """This is a Square class that has attribute size with conditions"""
    def __init__(self, size=0):
        """Initializes an instance of Square"""
        self.__size = size

    @property
    def size(self):
        """This method gets size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """This method sets the size attribute"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Calculates the area of square instance"""

        return self.__size * self.__size
