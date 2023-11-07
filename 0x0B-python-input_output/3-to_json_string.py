#!/usr/bin/python3
"""This module converts an object to its json representation"""

import json


def to_json_string(my_obj):
    """Generates JSON representation of object

    Args:
        my_obj (object): Object to be converted
    """
    return json.dumps(my_obj)
