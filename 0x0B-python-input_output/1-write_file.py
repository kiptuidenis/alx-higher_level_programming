#!/usr/bin/python3
"""This module writes to file"""


def write_file(filename="", text=""):
    """Writes to file

    Args:
        filename (str, optional): Name of file. Defaults to "".
        text (str, optional): String to be written to file. Defaults to "".
    """
    with open(filename, 'w', encoding='utf8') as f:
        return f.write(text)
