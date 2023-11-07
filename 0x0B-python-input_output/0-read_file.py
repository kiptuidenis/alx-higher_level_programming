#!/usr/bin/python3
"""This module reads and prints the contents of a file
"""


def read_file(filename=""):
    """Reads a file

    Args:
        filename (str, optional): Name of fie. Defaults to "".
    """
    with open(filename, 'r', encoding='utf8') as f:
        print(f.read())
