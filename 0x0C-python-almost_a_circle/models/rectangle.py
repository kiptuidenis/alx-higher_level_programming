#!/usr/bin/python3
"""This module contains Rectangle Class
that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle - Inherits from Base

    Args:
        Base (Class): This is the Parent Class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialises a Rectangle instance

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width to value

        Args:
            value (int): Value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height to value

        Args:
            value (int): Value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x to value

        Args:
            value (int): Value of x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y to value

        Args:
            value (int): Value of y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
