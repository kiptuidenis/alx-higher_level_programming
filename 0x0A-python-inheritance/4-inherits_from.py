#!/usr/bin/python3
"""This module contains a function is_same_class
"""


def inherits_from(obj, a_class):
    """returns True if the object is exactly an
    instance of the specified class ; otherwise False

    Args:
        obj : Object to be checked
        a_class : Class to be checked against
    """

    cls = type(obj)
    if issubclass(cls, a_class) and type(obj) != a_class:
        return True
    else:
        return False
