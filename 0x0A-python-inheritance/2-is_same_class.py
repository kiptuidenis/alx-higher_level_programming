#!/usr/bin/python3
"""This module contains a function is_same_class
"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an
    instance of the specified class ; otherwise False

    Args:
        obj : Object to be checked
        a_class : Class to be checked against
    """

    if type(obj) is a_class:
        return True
    else:
        return False
