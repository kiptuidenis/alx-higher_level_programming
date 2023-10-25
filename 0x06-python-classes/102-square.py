#!/usr/bin/python3
"""This module contains Square class"""


class Square:
    """Template for square objects"""

    def __init__(self, size=0):
        """Initializes the size field"""

        self.size = size

    @property
    def size(self):
        """Retrieves the size field"""

        return self.__size

    @size.setter
    def size(self, value):
        """Assigns value to size"""

        if value < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        self.__size = value

    def area(self):
        """Finds the area of the square"""

        self.__area = self.__size ** 2
        return self.__area

    def __eq__(self, other):
        """Allows for '==' operator usage"""

        return self.area() == other.area()

    def __lt__(self, other):
        """Allows for '<' operator usage"""

        return self.area() < other.area()

    def __le__(self, other):
        """Allows for '<=' operator usage"""

        return self.area() <= other.area()

    def __gt__(self, other):
        """Allows for '>' operator usage"""

        return self.area() > other.area()

    def __ge__(self, other):
        """Allows for '>=' operator usage"""

        return self.area() >= other.area()

    def __ne__(self, other):
        """Allows for '!=' operator usage"""

        return self.area() != other.area()
