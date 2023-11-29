#!/usr/bin/python3
"""This module contains the Rectangle class
"""
from models.base import Base

class Rectangle(Base):
    """Defines the dimensions of the rectangle among other parameters

    Args:
        Base (class): Handles the 'id' attribute
    """
    def __init__(self, width=0, height=0, x=0, y=0, id=None):
        """This is the constructor of this class

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
            x (int, optional): Defaults to 0.
            y (int, optional): Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method of width attribute
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """Setter method of width attribute

        Args:
            value (int): 
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method of height attribute
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """Setter method of height attribute

        Args:
            value (int): 
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method of x attribute
        """
        return self.__x
    
    @x.setter
    def x(self, value):
        """Setter method of x attribute

        Args:
            value (int): 
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method of y attribute
        """
        return self.__y
    
    @y.setter
    def y(self, value):
        """Setter method of y attribute

        Args:
            value (int): 
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Finds the area of the rectangle
        """
        self.area = self.__width * self.__height
        return self.area

    def display(self):
        """Prints out the Rectangle instance with character '#'
        """
        print_char = '#'
        print_new_line = '\n'
        print_space = " "

        if self.y != 0:
            print(print_new_line * (self.y - 1)) 
        for i in range(self.height):
            print(print_space * self.x, end="")
            print(print_char * self.width)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

