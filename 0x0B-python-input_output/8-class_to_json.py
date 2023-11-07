#!/usr/bin/python3
"""This module converts an object to dictionary description with simple
data structure (list, dictionary, string, integer and boolean) for
JSON serialization of an object
"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for
    JSON serialization of an object

    Args:
        obj (Object): Instance of a class to be converted to
                      a dictionary for serialization
    """
    dir_list = dir(obj)
    attr_list = [x for x in dir_list if "__" not in x]
    attr_dict = {attr_list[i]: getattr(obj, attr_list[i]) 
    for i in range(0, len(attr_list))}
    return attr_dict
