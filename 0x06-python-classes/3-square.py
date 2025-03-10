#!/usr/bin/python3
"""This module contains a class"""

class Square:
    """Initializes the size of the square and calculates area"""
    def __init__(self, size=0):
        self.__size = size
        
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2