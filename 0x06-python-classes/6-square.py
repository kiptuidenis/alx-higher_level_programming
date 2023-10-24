#!/usr/bin/python3
"""This module contains a class Square"""


class Square:
    """This is a Square class that has attribute size with conditions"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes an instance of Square"""
        self.__size = size
        self.__position = position

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
    @property
    def position(self):
        """This method gets position attribute"""
        return self.__position
    @position.setter
    def position(self, value):
        """This method sets position attribute"""
        if isinstance(value, tuple):
            for item in self.__position:
                if not isinstance(item, int):
                    raise TypeError("position must be a tuple of 2 positive integers")
                else:
                    self.__postion = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Calculates the area of square instance"""
        self.__area = self.__size * self.__size

        return self.__area

    def my_print(self):
        """Prints in stdout the square character '#' """

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    if j < self.__size - 1:
                        print("#", end="")
                    if j == self.__size - 1:
                        print("#")
