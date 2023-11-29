#!/usr/bin/python3
"""This module contains the base class for this project
"""


class Base:
    """This will be the 'base' class in this project
       The goal of it is to manage 'id' attribute in 
       all future classes and to avoid duplicating the
       same code(by extension, same bugs)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """This is the constructor of this class

       Args:
           id (int, optional): Defaults to None.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
