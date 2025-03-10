#!/usr/bin/python3
"""This module contains a class"""

class Square:
    """Initializes the size of the square and calculates area"""
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2
    
    @property
    def size(self):
        """Getter for size"""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Setter for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
    
        self.__size = value