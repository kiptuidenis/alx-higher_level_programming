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
    fields = [name for name in dir_list if not callable(getattr(obj, name)) and not name.startswith("__")]
    print(fields)
    attr_dict = {fields[i]: getattr(obj, fields[i]) 
    for i in range(0, len(fields))}
    return attr_dict
