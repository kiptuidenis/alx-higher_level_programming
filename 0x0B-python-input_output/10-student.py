#!/usr/bin/python3
"""This module has a class Student that retrieves
a dictionary representation of a Student instance"""


class Student:
    """Defines a student by first_name,
    last_name, age
    """
    def __init__(self, first_name, last_name, age):
        """Initialises an instance of this class

        Args:
            first_name (str): First name of the student
            last_name (str): Last name of the student
            age (int): Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation
        of a Student instance. Filters wrt "attrs" list
        """
        dir_list = dir(self)
        fields = [name for name in dir_list if not
                  callable(getattr(self, name)) and not name.startswith("__")]
        if attrs is not None:
            fields = [name for name in fields if name in attrs]
        attr_dict = {fields[i]: getattr(self, fields[i])
                     for i in range(0, len(fields))}
        return attr_dict
