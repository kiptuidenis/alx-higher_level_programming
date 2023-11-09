#!/usr/bin/python3
"""This modue contains the base class
"""


class Base:
    """This is the base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor.
        if id is not None, assign the public instance
        attribute id with this argument value -
        id is always an integer

        otherwise, __nb_objects is incremented and assigned
        to the public instance attribute id

        Args:
            id (int, optional): Id of the class Instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
