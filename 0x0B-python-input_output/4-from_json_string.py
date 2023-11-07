#!/usr/bin/python3
"""This module converts JSON string to object"""

import json

def from_json_string(my_str):
    """Converts JSON string to Object

    Args:
        my_str (json string): String to be converted to object
    """

    return json.loads(my_str)
