#!/usr/bin/python3
"""This is an integer validator
"""


class BaseGeometry():
    """Validates a value
    """
    def area(self):
        """Raises an exception error
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a value

        Args:
            name : Name of the value
            value : Integer to be checked
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
