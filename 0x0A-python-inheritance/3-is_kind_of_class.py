#!/usr/bin/python3
"""This module contains a function is_same_class
"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is exactly an
    instance of the specified class ; otherwise False

    Args:
        obj : Object to be checked
        a_class : Class to be checked against
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
