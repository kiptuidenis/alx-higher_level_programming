#!/usr/bin/python3
"""This module creates an Object from JSON file"""

import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”:

    Args:
        filename (string): Name of JSON file
    """
    with open(filename, 'r', encoding='utf8') as f:
        return json.loads(f.read())
