#!/usr/bin/python3
"""This module appends text to a file"""


def append_write(filename="", text=""):
    """This functions appends to a file

    Args:
        filename (str, optional): Name of the file. Defaults to "".
        text (str, optional): Text to append. Defaults to "".
    """
    with open(filename, 'a', encoding="utf8") as f:
        return f.write(text)
