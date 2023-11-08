#!/usr/bin/python3
"""This module creates a square of size @size
It can also calculate the area of the square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits from Rectangle class

    Args:
        Rectangle (class): Parent class
    """
    def __init__(self, size):
        """Initialises a Square instance

        Args:
            size (int): Size of one side of the square
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculates the area of the square
        """
        self.area = self.__size ** 2
        return self.area

    def __str__(self):
        """Prints out the dimensions of the Square
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)