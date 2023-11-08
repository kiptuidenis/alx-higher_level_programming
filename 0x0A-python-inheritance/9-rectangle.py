#!/usr/bin/python3
"""This module has blueprints for Rectangle instance
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class inherits from BaseGeometry

    Args:
        BaseGeometry (class): Parent class
    """
    def __init__(self, width, height):
        """Initialises an instance of this class

        Args:
            width (int): Width of the rectangle instance
            height (int): Height of the rectangle instance
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Finds the area of a Rectangle
        """
        self.area = self.__height * self.__width
        return self.area
    
    def __str__(self):
        """prints an instance of a rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
