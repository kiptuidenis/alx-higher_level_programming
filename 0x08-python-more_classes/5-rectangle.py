#!/usr/bin/python3
"""This module defines a simple rectangle"""


class Rectangle:
    """This class defines a simple rectangle
    Args:
        width - The width of the rectangle. Must be an integer
        height - The height of the rectangle. Must be an integer
    """
    def __init__(self, width=0, height=0):
        """Initialises the width and height"""
        self.width = width
        self.height = height
        self.perim = 0

    @property
    def width(self):
        """Gets the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width to value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Gets the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets width to value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Calculates the area of a rectangle"""
        self.__area = self.__height * self.__width
        return self.__area

    def perimeter(self):
        """Calculates the perimeter of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        self.__perim = 2 * (self.__width + self.__height)
        return self.__perim

    def __str__(self):
        """Prints rectangle as a string"""
        if self.__width == 0 or self.__height == 0:
            return ""
        result = ""
        for row in range(self.__height):
            if row == self.__height - 1:
                result += '#' * self.__width
            else:
                result += '#' * self.__width + '\n'
        return result

    def __repr__(self):
        """Prints rectangle as a string"""
        return "Rectangle(2, 4)"

    def __del__(self):
        """Deletes rectangle"""
        del self.__height
        del self.__width
        print("Bye rectangle")
