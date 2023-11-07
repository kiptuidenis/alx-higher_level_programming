#!/usr/bin/python3
"""This modue writes JSON string to file"""

import json

def save_to_json_file(my_obj, filename):
    """ Writes an Object to a text file, using a JSON representation

    Args:
        my_obj (Object): Object to be written to file
        filename (string): name of file
    """
    with open(filename, 'w', encoding='utf8') as f:
        f.write(json.dumps(my_obj))
