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
