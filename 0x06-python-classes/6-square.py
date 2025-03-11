#!/usr/bin/python3
"""This module contains a class"""

class Square:
    """Initializes the size of the square and calculates area"""
    def __init__(self, size=0, position=(0, 0)):
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

    @property
    def position(self):
        """Getter for position"""
        return self.__position
    
    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value


    def my_print(self):
        """Prints the square with #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)

    